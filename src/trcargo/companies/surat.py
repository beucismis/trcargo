from trcargo.companies.base import BaseCompaine


class Surat(BaseCompaine):
    NAME: str = "Sürat Kargo"
    BASE_URL: str = "https://suratkargo.com.tr/"

    def get_search(self, query: str) -> None:
        raise NotImplementedError()
