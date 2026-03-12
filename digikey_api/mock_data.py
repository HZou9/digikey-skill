"""Realistic mock data for DigiKey API development."""


def mock_keyword_search(keywords: str, limit: int = 10) -> dict:
    """Return mock search results based on keywords."""
    kw = keywords.lower()
    products = []

    if any(w in kw for w in ["mosfet", "sic", "fet", "transistor"]):
        products = _mosfet_products()
    elif any(w in kw for w in ["gate driver", "driver", "ucc", "adum"]):
        products = _gate_driver_products()
    elif any(w in kw for w in ["capacitor", "cap", "mlcc", "ceramic", "film"]):
        products = _capacitor_products()
    elif any(w in kw for w in ["resistor", "res", "ohm"]):
        products = _resistor_products()
    else:
        products = _mosfet_products() + _gate_driver_products()

    return {
        "Products": products[:limit],
        "ProductsCount": len(products),
        "ExactManufacturerProductsCount": 0,
        "FilterOptions": [],
        "SearchLocaleUsed": {"Site": "US", "Language": "en", "Currency": "USD"},
        "_mock": True,
    }


def mock_product_details(part_number: str) -> dict:
    """Return mock product details."""
    all_products = (
        _mosfet_products() + _gate_driver_products() + _capacitor_products()
    )
    for p in all_products:
        if p["DigiKeyPartNumber"] == part_number or p["ManufacturerPartNumber"] in part_number:
            return {"Product": p, "_mock": True}
    return {"Product": all_products[0], "_mock": True}


def mock_pricing(part_number: str) -> dict:
    """Return mock pricing tiers."""
    return {
        "DigiKeyPartNumber": part_number,
        "PricingTiers": [
            {"BreakQuantity": 1, "UnitPrice": 12.50, "TotalPrice": 12.50},
            {"BreakQuantity": 10, "UnitPrice": 10.80, "TotalPrice": 108.00},
            {"BreakQuantity": 25, "UnitPrice": 9.50, "TotalPrice": 237.50},
            {"BreakQuantity": 100, "UnitPrice": 8.20, "TotalPrice": 820.00},
            {"BreakQuantity": 500, "UnitPrice": 7.10, "TotalPrice": 3550.00},
        ],
        "_mock": True,
    }


def mock_substitutions(part_number: str) -> dict:
    """Return mock substitution suggestions."""
    return {
        "DigiKeyPartNumber": part_number,
        "Substitutions": [
            {"ManufacturerPartNumber": "C3M0032120K", "Manufacturer": "Wolfspeed",
             "Description": "MOSFET SIC 1200V 32MOHM TO247-3"},
            {"ManufacturerPartNumber": "IMZ120R025M1HXKSA1", "Manufacturer": "Infineon",
             "Description": "MOSFET SIC 1200V 25MOHM TO-247"},
        ],
        "_mock": True,
    }


def _mosfet_products() -> list:
    return [
        {
            "DigiKeyPartNumber": "C3M0025065K-ND",
            "ManufacturerPartNumber": "C3M0025065K",
            "Manufacturer": "Wolfspeed",
            "Description": "MOSFET SIC N-CH 650V 25MOHM TO247-3",
            "UnitPrice": 8.50,
            "QuantityAvailable": 4523,
            "DatasheetUrl": "https://assets.wolfspeed.com/uploads/2024/01/Wolfspeed_C3M0025065K_data_sheet.pdf",
            "ProductUrl": "https://www.digikey.com/en/products/detail/wolfspeed/C3M0025065K/9947719",
            "PhotoUrl": "https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/2829/TO-247-3.jpg",
            "Parameters": [
                {"Name": "FET Type", "Value": "N-Channel"},
                {"Name": "Technology", "Value": "SiC (Silicon Carbide)"},
                {"Name": "Drain-Source Voltage (Vdss)", "Value": "650V"},
                {"Name": "Current - Continuous Drain (Id) @ 25°C", "Value": "97A"},
                {"Name": "Rds On (Max) @ Id, Vgs", "Value": "25mΩ @ 50A, 15V"},
                {"Name": "Vgs(th) (Max) @ Id", "Value": "4.5V @ 10mA"},
                {"Name": "Gate Charge (Qg) (Max) @ Vgs", "Value": "95nC @ 15V"},
                {"Name": "Input Capacitance (Ciss) (Max) @ Vds", "Value": "2253pF @ 400V"},
                {"Name": "Power Dissipation (Max)", "Value": "211W"},
                {"Name": "Operating Temperature", "Value": "-55°C ~ 175°C"},
                {"Name": "Mounting Type", "Value": "Through Hole"},
                {"Name": "Package / Case", "Value": "TO-247-3"},
                {"Name": "Supplier Device Package", "Value": "TO-247-3"},
            ],
            "RoHSStatus": "RoHS Compliant",
            "LeadStatus": "Lead Free",
        },
        {
            "DigiKeyPartNumber": "IPW65R019C7FKSA1-ND",
            "ManufacturerPartNumber": "IPW65R019C7",
            "Manufacturer": "Infineon Technologies",
            "Description": "MOSFET N-CH 650V 19MOHM TO247-3",
            "UnitPrice": 6.75,
            "QuantityAvailable": 8901,
            "DatasheetUrl": "https://www.infineon.com/dgdl/Infineon-IPW65R019C7-DataSheet-v02_01-EN.pdf",
            "ProductUrl": "https://www.digikey.com/en/products/detail/infineon/IPW65R019C7/5930928",
            "PhotoUrl": "https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/2829/TO-247-3.jpg",
            "Parameters": [
                {"Name": "FET Type", "Value": "N-Channel"},
                {"Name": "Technology", "Value": "MOSFET (Metal Oxide)"},
                {"Name": "Drain-Source Voltage (Vdss)", "Value": "650V"},
                {"Name": "Current - Continuous Drain (Id) @ 25°C", "Value": "59A"},
                {"Name": "Rds On (Max) @ Id, Vgs", "Value": "19mΩ @ 31A, 10V"},
                {"Name": "Vgs(th) (Max) @ Id", "Value": "4.5V @ 1.6mA"},
                {"Name": "Gate Charge (Qg) (Max) @ Vgs", "Value": "160nC @ 10V"},
                {"Name": "Input Capacitance (Ciss) (Max) @ Vds", "Value": "6800pF @ 400V"},
                {"Name": "Power Dissipation (Max)", "Value": "278W"},
                {"Name": "Operating Temperature", "Value": "-55°C ~ 150°C"},
                {"Name": "Mounting Type", "Value": "Through Hole"},
                {"Name": "Package / Case", "Value": "TO-247-3"},
            ],
            "RoHSStatus": "RoHS Compliant",
            "LeadStatus": "Lead Free",
        },
        {
            "DigiKeyPartNumber": "SCT3022ALGC11-ND",
            "ManufacturerPartNumber": "SCT3022ALGC11",
            "Manufacturer": "ROHM Semiconductor",
            "Description": "MOSFET SIC N-CH 650V 22MOHM TO247N",
            "UnitPrice": 7.90,
            "QuantityAvailable": 3200,
            "DatasheetUrl": "https://fscdn.rohm.com/en/products/databook/datasheet/discrete/sic/mosfet/sct3022al-e.pdf",
            "ProductUrl": "https://www.digikey.com/en/products/detail/rohm/SCT3022ALGC11/13994951",
            "PhotoUrl": "https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/2829/TO-247N.jpg",
            "Parameters": [
                {"Name": "FET Type", "Value": "N-Channel"},
                {"Name": "Technology", "Value": "SiC (Silicon Carbide)"},
                {"Name": "Drain-Source Voltage (Vdss)", "Value": "650V"},
                {"Name": "Current - Continuous Drain (Id) @ 25°C", "Value": "93A"},
                {"Name": "Rds On (Max) @ Id, Vgs", "Value": "22mΩ @ 50A, 18V"},
                {"Name": "Vgs(th) (Max) @ Id", "Value": "5.6V @ 10mA"},
                {"Name": "Gate Charge (Qg) (Max) @ Vgs", "Value": "120nC @ 18V"},
                {"Name": "Input Capacitance (Ciss) (Max) @ Vds", "Value": "2720pF @ 400V"},
                {"Name": "Power Dissipation (Max)", "Value": "165W"},
                {"Name": "Operating Temperature", "Value": "-55°C ~ 175°C"},
                {"Name": "Package / Case", "Value": "TO-247-3"},
            ],
            "RoHSStatus": "RoHS Compliant",
            "LeadStatus": "Lead Free",
        },
        {
            "DigiKeyPartNumber": "NTBGS1D5N65S1HF-ND",
            "ManufacturerPartNumber": "NTBGS1D5N65S1HF",
            "Manufacturer": "onsemi",
            "Description": "MOSFET SIC N-CH 650V 15MOHM D2PAK",
            "UnitPrice": 5.60,
            "QuantityAvailable": 12500,
            "DatasheetUrl": "https://www.onsemi.com/download/data-sheet/pdf/ntbgs1d5n65s1-d.pdf",
            "ProductUrl": "https://www.digikey.com/en/products/detail/onsemi/NTBGS1D5N65S1HF/16809642",
            "PhotoUrl": "https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/1702/D2PAK.jpg",
            "Parameters": [
                {"Name": "FET Type", "Value": "N-Channel"},
                {"Name": "Technology", "Value": "SiC (Silicon Carbide)"},
                {"Name": "Drain-Source Voltage (Vdss)", "Value": "650V"},
                {"Name": "Current - Continuous Drain (Id) @ 25°C", "Value": "79A"},
                {"Name": "Rds On (Max) @ Id, Vgs", "Value": "15mΩ @ 40A, 18V"},
                {"Name": "Gate Charge (Qg) (Max) @ Vgs", "Value": "85nC @ 18V"},
                {"Name": "Input Capacitance (Ciss) (Max) @ Vds", "Value": "2100pF @ 400V"},
                {"Name": "Power Dissipation (Max)", "Value": "192W"},
                {"Name": "Package / Case", "Value": "D²Pak (TO-263-3)"},
            ],
            "RoHSStatus": "RoHS Compliant",
            "LeadStatus": "Lead Free",
        },
    ]


def _gate_driver_products() -> list:
    return [
        {
            "DigiKeyPartNumber": "296-UCC21530QDWRQ1-ND",
            "ManufacturerPartNumber": "UCC21530QDWRQ1",
            "Manufacturer": "Texas Instruments",
            "Description": "IC GATE DRVR HALF-BRIDGE 16SOIC",
            "UnitPrice": 3.25,
            "QuantityAvailable": 15600,
            "DatasheetUrl": "https://www.ti.com/lit/ds/symlink/ucc21530-q1.pdf",
            "ProductUrl": "https://www.digikey.com/en/products/detail/ti/UCC21530QDWRQ1/7589044",
            "PhotoUrl": "https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/2345/16-SOIC.jpg",
            "Parameters": [
                {"Name": "Driver Type", "Value": "Half Bridge"},
                {"Name": "Gate Driver Type", "Value": "Isolated"},
                {"Name": "Number of Outputs", "Value": "2"},
                {"Name": "Peak Output Current (Source, Sink)", "Value": "4A, 6A"},
                {"Name": "Propagation Delay (Max)", "Value": "19ns"},
                {"Name": "Rise Time", "Value": "6ns"},
                {"Name": "Fall Time", "Value": "6ns"},
                {"Name": "Voltage - Supply", "Value": "9.2V ~ 25V"},
                {"Name": "Package / Case", "Value": "16-SOIC"},
                {"Name": "Isolation Voltage", "Value": "5700Vrms"},
                {"Name": "CMTI", "Value": "100V/ns"},
            ],
            "RoHSStatus": "RoHS Compliant",
            "LeadStatus": "Lead Free",
        },
        {
            "DigiKeyPartNumber": "ADUM4121-1BRIZ-ND",
            "ManufacturerPartNumber": "ADUM4121-1BRIZ",
            "Manufacturer": "Analog Devices",
            "Description": "IC GATE DRVR ISO 8SOIC",
            "UnitPrice": 4.85,
            "QuantityAvailable": 6200,
            "DatasheetUrl": "https://www.analog.com/media/en/technical-documentation/data-sheets/ADuM4121-1.pdf",
            "ProductUrl": "https://www.digikey.com/en/products/detail/analog-devices/ADUM4121-1BRIZ/4930261",
            "PhotoUrl": "https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/2345/8-SOIC.jpg",
            "Parameters": [
                {"Name": "Driver Type", "Value": "High Side or Low Side"},
                {"Name": "Gate Driver Type", "Value": "Isolated"},
                {"Name": "Number of Outputs", "Value": "1"},
                {"Name": "Peak Output Current (Source, Sink)", "Value": "2A, 4A"},
                {"Name": "Propagation Delay (Max)", "Value": "55ns"},
                {"Name": "Rise Time", "Value": "13ns"},
                {"Name": "Fall Time", "Value": "7ns"},
                {"Name": "Voltage - Supply", "Value": "3.3V ~ 5V (input), 9.5V ~ 18V (output)"},
                {"Name": "Package / Case", "Value": "8-SOIC"},
                {"Name": "Isolation Voltage", "Value": "5000Vrms"},
                {"Name": "CMTI", "Value": "150V/ns"},
            ],
            "RoHSStatus": "RoHS Compliant",
            "LeadStatus": "Lead Free",
        },
        {
            "DigiKeyPartNumber": "SI8271AB-IS-ND",
            "ManufacturerPartNumber": "SI8271AB-IS",
            "Manufacturer": "Skyworks Solutions (Silicon Labs)",
            "Description": "IC GATE DRVR ISO 8SOIC",
            "UnitPrice": 2.95,
            "QuantityAvailable": 9800,
            "DatasheetUrl": "https://www.skyworksinc.com/-/media/SkyWorks/SL/documents/public/data-sheets/si827x.pdf",
            "ProductUrl": "https://www.digikey.com/en/products/detail/skyworks/SI8271AB-IS/14649574",
            "PhotoUrl": "https://mm.digikey.com/Volume0/opasdata/d220001/medias/images/2345/8-SOIC.jpg",
            "Parameters": [
                {"Name": "Driver Type", "Value": "High Side or Low Side"},
                {"Name": "Gate Driver Type", "Value": "Isolated"},
                {"Name": "Number of Outputs", "Value": "1"},
                {"Name": "Peak Output Current (Source, Sink)", "Value": "4A, 4A"},
                {"Name": "Propagation Delay (Max)", "Value": "38ns"},
                {"Name": "Rise Time", "Value": "9ns"},
                {"Name": "Fall Time", "Value": "9ns"},
                {"Name": "Voltage - Supply", "Value": "6.5V ~ 24V"},
                {"Name": "Package / Case", "Value": "8-SOIC"},
                {"Name": "Isolation Voltage", "Value": "5000Vrms"},
                {"Name": "CMTI", "Value": "200V/ns"},
            ],
            "RoHSStatus": "RoHS Compliant",
            "LeadStatus": "Lead Free",
        },
    ]


def _capacitor_products() -> list:
    return [
        {
            "DigiKeyPartNumber": "1276-1123-1-ND",
            "ManufacturerPartNumber": "CL21B104KBCNNNC",
            "Manufacturer": "Samsung Electro-Mechanics",
            "Description": "CAP CER 100NF 50V X7R 0805",
            "UnitPrice": 0.015,
            "QuantityAvailable": 458000,
            "DatasheetUrl": "https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5068/CL21B104KBCNNNC.pdf",
            "ProductUrl": "https://www.digikey.com/en/products/detail/samsung/CL21B104KBCNNNC/3886902",
            "Parameters": [
                {"Name": "Capacitance", "Value": "100nF"},
                {"Name": "Voltage - Rated", "Value": "50V"},
                {"Name": "Temperature Coefficient", "Value": "X7R"},
                {"Name": "Package / Case", "Value": "0805 (2012 Metric)"},
                {"Name": "Tolerance", "Value": "±10%"},
                {"Name": "Mounting Type", "Value": "Surface Mount"},
            ],
            "RoHSStatus": "RoHS Compliant",
            "LeadStatus": "Lead Free",
        },
        {
            "DigiKeyPartNumber": "445-5304-1-ND",
            "ManufacturerPartNumber": "C3225X7R1H106K250AE",
            "Manufacturer": "TDK Corporation",
            "Description": "CAP CER 10UF 50V X7R 1210",
            "UnitPrice": 0.35,
            "QuantityAvailable": 125000,
            "DatasheetUrl": "https://product.tdk.com/system/files/dam/doc/product/capacitor/ceramic/mlcc/catalog/mlcc_commercial_midvoltage_en.pdf",
            "ProductUrl": "https://www.digikey.com/en/products/detail/tdk/C3225X7R1H106K250AE/1589678",
            "Parameters": [
                {"Name": "Capacitance", "Value": "10µF"},
                {"Name": "Voltage - Rated", "Value": "50V"},
                {"Name": "Temperature Coefficient", "Value": "X7R"},
                {"Name": "Package / Case", "Value": "1210 (3225 Metric)"},
                {"Name": "Tolerance", "Value": "±10%"},
                {"Name": "Mounting Type", "Value": "Surface Mount"},
            ],
            "RoHSStatus": "RoHS Compliant",
            "LeadStatus": "Lead Free",
        },
    ]


def _resistor_products() -> list:
    return [
        {
            "DigiKeyPartNumber": "RMCF0805FT10K0CT-ND",
            "ManufacturerPartNumber": "RMCF0805FT10K0",
            "Manufacturer": "Stackpole Electronics",
            "Description": "RES 10K OHM 1% 1/8W 0805",
            "UnitPrice": 0.008,
            "QuantityAvailable": 950000,
            "DatasheetUrl": "https://www.seielect.com/catalog/sei-rmcf_rmcp.pdf",
            "ProductUrl": "https://www.digikey.com/en/products/detail/stackpole/RMCF0805FT10K0/1760393",
            "Parameters": [
                {"Name": "Resistance", "Value": "10kΩ"},
                {"Name": "Tolerance", "Value": "±1%"},
                {"Name": "Power (Watts)", "Value": "0.125W"},
                {"Name": "Package / Case", "Value": "0805 (2012 Metric)"},
                {"Name": "Mounting Type", "Value": "Surface Mount"},
            ],
            "RoHSStatus": "RoHS Compliant",
            "LeadStatus": "Lead Free",
        },
    ]
