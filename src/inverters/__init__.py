from typing import Dict, Any
from .huawei.huawei import huawei_profile
from .sungrow.sungrow import sungrow_profile
from .goodwe.goodwe import goodwe_profile
from .ferroamp.ferroamp import ferroamp_profile
from .fronius.fronius import fronius_profile
from .solis.solis import solis_profile
from .solis.solis_hybrid import solis_hybrid_profile
from .sma.sma import sma_profile
from .growatt.growatt import growatt_profile
from .sofar.sofar import sofar_profile


# Registry of supported inverter profiles
INVERTER_PROFILES: Dict[str, Dict[str, Any]] = {
    'huawei': huawei_profile,
    'sungrow': sungrow_profile,
    'goodwe': goodwe_profile,
    'ferroamp': ferroamp_profile,
    'fronius': fronius_profile,
    'solis': solis_profile,
    'solis_hybrid': solis_hybrid_profile,
    'sma': sma_profile,
    'growatt': growatt_profile,
    'sofar': sofar_profile,
    # Add more profiles here as they are supported
}
