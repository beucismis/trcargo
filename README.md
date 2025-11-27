# trcargo

Track packages from Turkish cargo companies.

Supported Companies:
- PTT Kargo (tested)
- Aras Kargo (pending development)
- MNG Kargo (pending development)
- Sürat Kargo (pending development)
- UPS Türkiye (pending development)
- Yurtiçi Kargo (pending development)

## Installing

```
git clone https://github.com/beucismis/trcargo
cd trcargo/
pip install .
```

## Usage

```
from trcargo import ptt

ptt.get_search("...")
```

## License

`trcargo` is distributed under the terms of the [MIT](LICENSE.txt) license.
