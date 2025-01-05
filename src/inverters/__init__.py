from typing import Dict, Any
from .huawei.huawei import huawei_profile
from .sungrow.sungrow import sungrow_profile
from .goodwe.goodwe import goodwe_profile
from .ferroamp.ferroamp import ferroamp_profile
from .fronius.fronius import fronius_profile
from .solis.solis import solis_profile
from .solis.solis_hybrid import solis_hybrid_profile

# Registry of supported inverter profiles
INVERTER_PROFILES: Dict[str, Dict[str, Any]] = {
    'huawei': huawei_profile,
    'sungrow': sungrow_profile,
    'goodwe': goodwe_profile,
    'ferroamp': ferroamp_profile,
    'fronius': fronius_profile,
    'solis': solis_profile,
    'solis_hybrid': solis_hybrid_profile,
    # Add more profiles here as they are supported
}
