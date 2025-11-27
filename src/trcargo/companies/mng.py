from trcargo.companies.base import BaseCompaine


class MNG(BaseCompaine):
    NAME: str = "MNG Kargo"
    BASE_URL: str = "https://dhlecommerce.com.tr"

    def get_search(self, query: str) -> None:
        raise NotImplementedError()
