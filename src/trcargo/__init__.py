from trcargo.__about__ import __version__
from trcargo.companies.base import CargoTrackingError
from trcargo.companies.ptt import (
    PTT,
    AcceptanceInfo,
    CargoInfoResult,
    LatestStatus,
    Movement,
)

ptt = PTT()

__all__ = [
    "__version__",
    "CargoTrackingError",
    "AcceptanceInfo",
    "CargoInfoResult",
    "LatestStatus",
    "Movement",
    "PTT",
    "ptt",
]
