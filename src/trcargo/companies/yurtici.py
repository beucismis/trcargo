from trcargo.companies.base import BaseCompaine


class Yurtici(BaseCompaine):
    NAME: str = "Yurtiçi Kargo"
    BASE_URL: str = "https://yurticikargo.com"

    def get_search(self, query: str) -> None:
        raise NotImplementedError()
