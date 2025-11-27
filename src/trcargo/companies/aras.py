from trcargo.companies.base import BaseCompaine


class Aras(BaseCompaine):
    NAME: str = "Aras Kargo"
    BASE_URL: str = "https://araskargo.com.tr"

    def get_search(self, query: str) -> None:
        raise NotImplementedError()
