from trcargo.__about__ import __version__
from trcargo.companies.aras import Aras
from trcargo.companies.mng import MNG
from trcargo.companies.ptt import PTT
from trcargo.companies.surat import Surat
from trcargo.companies.ups import UPS
from trcargo.companies.yurtici import Yurtici

aras = Aras()
mng = MNG()
ptt = PTT()
surat = Surat()
ups = UPS()
yurtici = Yurtici()

__all__ = [
    "__version__",
    "Aras",
    "aras",
    "MNG",
    "mng",
    "PTT",
    "ptt",
    "Surat",
    "surat",
    "UPS",
    "ups",
    "Yurtici",
    "yurtici",
]
