from typing import Dict, Any

from .huawei.huawei import huawei_profile
from .sungrow.sungrow import sungrow_profile
from .goodwe.goodwe import goodwe_profile

# Registry of supported inverter profiles
INVERTER_PROFILES: Dict[str, Dict[str, Any]] = {
    'huawei': huawei_profile,
    'sungrow': sungrow_profile,
    'goodwe': goodwe_profile,
    # Add more profiles here as they are supported
}
