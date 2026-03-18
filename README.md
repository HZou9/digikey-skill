# DigiKey Skill — Component Search for Claude Code

A [Claude Code](https://claude.com/claude-code) skill for searching electronic components on DigiKey.

## Features

- **Keyword search** — natural language queries ("STM32G4", "SiC MOSFET 650V")
- **Product details** — full specs, parameters, datasheet links
- **Pricing tiers** — quantity breaks and unit prices
- **Substitutions** — find alternative parts

## Install

```bash
git clone https://github.com/HZou9/digikey-skill.git
cd digikey-skill
pip install -r requirements.txt
```

Register in Claude Code:
```
/install-skill /path/to/digikey-skill
```

## DigiKey API Setup

1. Register at https://developer.digikey.com
2. Create an app → get **Client ID** + **Client Secret**
3. Copy `.env.template` to `.env` and fill in credentials

No credentials? Runs in **mock mode** automatically.

## Usage

```bash
# Search
python scripts/search.py search "SiC MOSFET 650V" -n 10 -v

# Product details
python scripts/search.py details "448-IMT65R060M2HXUMA1CT-ND"

# Pricing
python scripts/search.py pricing "448-IMT65R060M2HXUMA1CT-ND"

# Substitutions
python scripts/search.py subs "448-IMT65R060M2HXUMA1CT-ND"

# JSON output
python scripts/search.py search "STM32G4" --json
```

## See Also

- [digikey-skill-pe](https://github.com/HZou9/digikey-skill-pe) — Power electronics specialized version with MOSFET FOM analysis, gate driver matching, capacitor/magnetics search, BOM optimization, and more.

## License

MIT
