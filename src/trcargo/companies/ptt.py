import json
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

import requests

from trcargo.companies.base import BaseCompaine, CargoTrackingError


@dataclass
class AcceptanceInfo:
    receiver: str
    sender: str
    origin_office: str
    acceptance_date: datetime.date
    tracking_number: str
    weight_kg: Optional[float]
    fee: Optional[float]
    declared_value: Optional[float]


@dataclass
class Movement:
    date: datetime.date
    time: datetime.time
    description: str
    office: str
    city: str
    district: str
    status_code: int
    is_domestic: bool


@dataclass
class LatestStatus:
    latest_status_description: str
    latest_operation_date: datetime.date
    latest_operation_time: datetime.time


@dataclass
class CargoInfoResult:
    acceptance_info: Optional[AcceptanceInfo]
    movements: List[Movement]
    latest_status: Optional[LatestStatus]


class PTT(BaseCompaine):
    NAME: str = "PTT"
    BASE_URL: str = "https://ptt.gov.tr"
    API_URL: str = "https://api.ptt.gov.tr"

    def get_search(self, query: str) -> CargoInfoResult:
        request = requests.Request("POST", f"{self.API_URL}/api/ShipmentTracking", json=[query])
        json_response = json.loads(self._request_page(request).text)[0]

        if not json_response["errorState"]:
            raise CargoTrackingError(json_response["errorMessage"])

        def safe_float(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return None

        acceptance_data = json_response.get("kabul")
        acceptance_info = None

        if acceptance_data:
            acceptance_info = AcceptanceInfo(
                receiver=acceptance_data.get("alici"),
                sender=acceptance_data.get("gonderici"),
                origin_office=acceptance_data.get("kabul_isyeri"),
                acceptance_date=datetime.strptime(str(acceptance_data.get("kabul_tarihi")), "%Y%m%d").date(),
                tracking_number=acceptance_data.get("barkod_no"),
                weight_kg=safe_float(acceptance_data.get("desi")),
                fee=safe_float(acceptance_data.get("ucret")),
                declared_value=safe_float(acceptance_data.get("deger_konulmus_bedeli")),
            )

        movements_data = json_response.get("hareketDongu", [])
        movements = [
            Movement(
                date=datetime.strptime(h["tarih"], "%d/%m/%Y").date(),
                time=datetime.strptime(h["saat"], "%H:%M:%S").time(),
                description=h["aciklama"],
                office=h["isyeri"],
                city=h["il"],
                district=h["ilce"],
                status_code=h["durum"],
                is_domestic=bool(h["yurtIciMi"]),
            )
            for h in movements_data
        ]
        latest_status_data = json_response.get("sondurum")
        latest_status = None

        if latest_status_data:
            latest_status = LatestStatus(
                latest_status_description=latest_status_data.get("son_durum_aciklama"),
                latest_operation_date=datetime.strptime(latest_status_data.get("son_islem_tarihi"), "%Y%m%d").date(),
                latest_operation_time=datetime.strptime(latest_status_data.get("son_islem_saati"), "%H:%M:%S").time(),
            )

        return CargoInfoResult(
            acceptance_info=acceptance_info,
            movements=movements,
            latest_status=latest_status,
        )
