from abc import ABC, abstractmethod
from typing import Optional

import requests
from cargotr.utils import request_page


class CargoTrackingError(Exception):
    pass


class BaseCompaine(ABC):
    NAME: str
    BASE_URL: str

    def __init__(self, base_url_override: Optional[str] = None) -> None:
        if base_url_override is not None:
            self.BASE_URL = base_url_override

        self._generate_new_session()

    def _generate_new_session(self) -> requests.Session:
        if hasattr(self, "session"):
            self.session.close()

        self.session = requests.Session()
        return self.session

    def _request_page(self, request: requests.Request) -> requests.Response:
        try:
            return request_page(self.session, request)
        except requests.ConnectionError:
            return request_page(self._generate_new_session(), request)

    @abstractmethod
    def get_search(self, query: str) -> None:
        pass
