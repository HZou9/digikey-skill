#!/usr/bin/env python3
"""DigiKey component search CLI - called by the /digikey skill."""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from digikey_api.client import DigiKeyClient
from digikey_api.config import Config


def format_table(products: list, verbose: bool = False) -> str:
    """Format search results as a readable table."""
    if not products:
        return "No results found."

    lines = []
    header = f"{'#':<3} {'MFR Part':<22} {'Manufacturer':<20} {'Price':<8} {'Stock':<8} {'Package':<12} {'Description'}"
    lines.append(header)
    lines.append("-" * len(header))

    for i, p in enumerate(products, 1):
        pkg = ""
        for param in p.get("Parameters", []):
            if "Package" in param.get("Name", ""):
                pkg = param["Value"][:11]
                break

        lines.append(
            f"{i:<3} {p.get('ManufacturerPartNumber', 'N/A'):<22} "
            f"{p.get('Manufacturer', 'N/A')[:19]:<20} "
            f"${p.get('UnitPrice', 0):<7.2f} "
            f"{p.get('QuantityAvailable', 0):<8} "
            f"{pkg:<12} "
            f"{p.get('Description', '')[:50]}"
        )

        if verbose:
            if p.get("DatasheetUrl"):
                lines.append(f"    Datasheet: {p['DatasheetUrl']}")
            key_params = []
            for param in p.get("Parameters", []):
                name = param.get("Name", "")
                if any(k in name for k in ["Voltage", "Current", "Rds", "Capacitance", "Resistance", "Gate Charge"]):
                    key_params.append(f"{name}: {param['Value']}")
            if key_params:
                lines.append(f"    Specs: {' | '.join(key_params[:4])}")
            lines.append("")

    return "\n".join(lines)


def format_details(product: dict) -> str:
    """Format product details."""
    p = product.get("Product", product)
    lines = [
        f"{'='*60}",
        f"Part: {p.get('ManufacturerPartNumber', 'N/A')}",
        f"Manufacturer: {p.get('Manufacturer', 'N/A')}",
        f"DigiKey PN: {p.get('DigiKeyPartNumber', 'N/A')}",
        f"Description: {p.get('Description', 'N/A')}",
        f"Price: ${p.get('UnitPrice', 0):.2f}",
        f"Stock: {p.get('QuantityAvailable', 0)}",
        f"RoHS: {p.get('RoHSStatus', 'N/A')}",
        f"Datasheet: {p.get('DatasheetUrl', 'N/A')}",
        f"{'='*60}",
        "Parameters:",
    ]
    for param in p.get("Parameters", []):
        lines.append(f"  {param.get('Name', '')}: {param.get('Value', '')}")

    return "\n".join(lines)


def format_pricing(pricing: dict) -> str:
    """Format pricing tiers."""
    lines = [f"Pricing for: {pricing.get('DigiKeyPartNumber', 'N/A')}", ""]
    header = f"{'Qty':<10} {'Unit Price':<12} {'Total':<12}"
    lines.append(header)
    lines.append("-" * 34)
    for tier in pricing.get("PricingTiers", []):
        lines.append(
            f"{tier['BreakQuantity']:<10} "
            f"${tier['UnitPrice']:<11.3f} "
            f"${tier['TotalPrice']:<11.2f}"
        )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="DigiKey Component Search")
    sub = parser.add_subparsers(dest="command", help="Command")

    # search
    sp = sub.add_parser("search", help="Keyword search")
    sp.add_argument("keywords", nargs="+", help="Search keywords")
    sp.add_argument("-n", "--limit", type=int, default=10, help="Max results")
    sp.add_argument("-v", "--verbose", action="store_true", help="Show details")
    sp.add_argument("--json", action="store_true", help="Output raw JSON")

    # details
    dp = sub.add_parser("details", help="Product details")
    dp.add_argument("part_number", help="DigiKey part number")
    dp.add_argument("--json", action="store_true", help="Output raw JSON")

    # pricing
    pp = sub.add_parser("pricing", help="Pricing tiers")
    pp.add_argument("part_number", help="DigiKey part number")
    pp.add_argument("--json", action="store_true", help="Output raw JSON")

    # substitutions
    ssp = sub.add_parser("subs", help="Find substitutions")
    ssp.add_argument("part_number", help="DigiKey part number")
    ssp.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    client = DigiKeyClient()

    if args.command == "search":
        keywords = " ".join(args.keywords)
        result = client.keyword_search(keywords, limit=args.limit)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            mock_tag = " [MOCK DATA]" if result.get("_mock") else ""
            print(f"\nDigiKey Search: \"{keywords}\"{mock_tag}")
            print(f"Found: {result.get('ProductsCount', 0)} results\n")
            print(format_table(result.get("Products", []), verbose=args.verbose))

    elif args.command == "details":
        result = client.product_details(args.part_number)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_details(result))

    elif args.command == "pricing":
        result = client.get_pricing(args.part_number)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_pricing(result))

    elif args.command == "subs":
        result = client.search_substitutions(args.part_number)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"\nSubstitutions for: {args.part_number}")
            for s in result.get("Substitutions", []):
                print(f"  - {s['ManufacturerPartNumber']} ({s['Manufacturer']}): {s.get('Description', '')}")


if __name__ == "__main__":
    main()
