from trcargo.companies.base import BaseCompaine


class UPS(BaseCompaine):
    NAME: str = "UPS Türkiye"
    BASE_URL: str = "https://ups.com.tr"

    def get_search(self, query: str) -> None:
        raise NotImplementedError()
