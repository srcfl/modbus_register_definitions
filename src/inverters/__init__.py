from typing import Dict, Any

from .huawei import huawei_profile

# Registry of supported inverter profiles
INVERTER_PROFILES: Dict[str, Dict[str, Any]] = {
    'huawei': huawei_profile,
    # Add more profiles here as they are supported
}
