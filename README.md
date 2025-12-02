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

## CLI Usage

```
$ trcargo ptt 271*******038

CargoInfoResult(
│   shipment_info=ShipmentInfo(receiver='*** ***', sender='*** ***', origin_office='BOĞAZ KDM', acceptance_date=datetime.date(2024, 2, 13), tracking_number='271*******038', weight_kg=1.0, fee=17.5, declared_value=384.02),
│   movements=[
│   │   Movement(date=datetime.date(2024, 2, 13), time=datetime.time(16, 51, 31), description='KABUL EDİLDİ', office='BOĞAZ KDM', city='İSTANBUL(AVR)', district='SARIYER', status_code=1, is_domestic=True),
│   │   Movement(date=datetime.date(2024, 2, 14), time=datetime.time(21, 10, 17), description='TRANSFER SÜRECİNDE', office='İSTANBUL AVRUPA YAKASI KİM', city='İSTANBUL(AVR)', district='ARNAVUTKÖY', status_code=3, is_domestic=True),
│   │   Movement(date=datetime.date(2024, 2, 16), time=datetime.time(10, 10, 39), description='İL İÇİ AKTARMADA', office='*** PKİDM', city='='***', district='MERKEZ', status_code=3, is_domestic=True),
│   │   Movement(date=datetime.date(2024, 2, 16), time=datetime.time(12, 8, 7), description='İL İÇİ AKTARMADA', office='='*** PKDM', city='='***', district='MERKEZ', status_code=44, is_domestic=True),
│   │   Movement(date=datetime.date(2024, 2, 17), time=datetime.time(8, 27, 1), description='DAĞITIMDA', office='='*** PKDM', city='='***', district='MERKEZ', status_code=7, is_domestic=True),
│   │   Movement(date=datetime.date(2024, 2, 17), time=datetime.time(8, 58, 47), description='TESLİM EDİLEMEDİ', office='='*** PKDM', city='='***', district='MERKEZ', status_code=195, is_domestic=True),
│   │   Movement(date=datetime.date(2024, 2, 17), time=datetime.time(14, 1, 29), description='İL İÇİ AKTARMADA', office='='*** PKDM', city='='***', district='MERKEZ', status_code=44, is_domestic=True),
│   │   Movement(date=datetime.date(2024, 2, 19), time=datetime.time(8, 42, 22), description='DAĞITIMDA', office='='*** PKDM', city='='***', district='MERKEZ', status_code=7, is_domestic=True),
│   │   Movement(date=datetime.date(2024, 2, 19), time=datetime.time(9, 48, 42), description='TESLİM EDİLDİ', office='='*** PKDM', city='='***', district='MERKEZ', status_code=100, is_domestic=True)
│   ],
│   latest_update=LatestUpdate(latest_status_description='TESLİM EDİLDİ', latest_operation_date=datetime.date(2024, 2, 19), latest_operation_time=None)
)
```

## License

`trcargo` is distributed under the terms of the [MIT](LICENSE.txt) license.
