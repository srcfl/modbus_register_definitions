from typing import Dict, Any, Tuple, List
import jwt
import base64
import json
from .modbus.register_definition import RegisterDefinition
from .inverters import INVERTER_PROFILES
from .modbus.register_definition_keys import ProfileKey, RegistersKey

def decode_jwt_to_json(jwt_token: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Decode a JWT token to get both header and payload without verifying the signature.
    
    Args:
        jwt_token (str): The JWT token string
        
    Returns:
        Tuple[Dict[str, Any], Dict[str, Any]]: A tuple containing (header, payload)
        
    Raises:
        ValueError: If the JWT token is invalid
    """
    try:
        # Split the JWT into parts
        header_b64, payload_b64, _ = jwt_token.split('.')
        
        # Decode header
        header_pad = header_b64 + '=' * (-len(header_b64) % 4)
        header = json.loads(base64.urlsafe_b64decode(header_pad).decode('utf-8'))
        
        # Decode payload
        decoded_payload = jwt.decode(jwt_token, algorithms=['ES256'], options={"verify_signature": False}, key=None)
        
        return header, decoded_payload
    except Exception as e:
        raise ValueError(f"Invalid JWT token: {str(e)}")

def create_register_values_from_jwt(header: Dict[str, Any], payload: Dict[str, Any]) -> List[Tuple[RegisterDefinition, Any]]:
    """
    Create RegisterValue objects from JWT data based on the model type.
    
    Args:
        header: JWT header containing model information
        payload: JWT payload containing register values
        
    Returns:
        List[Tuple[RegisterValue, Any]]: List of tuples containing (RegisterValue object, interpreted value)
    """
    model = header.get('model', '').lower()
    if model not in INVERTER_PROFILES:
        raise ValueError(f"Unsupported model type: {model}. Supported models: {', '.join(INVERTER_PROFILES.keys())}")
    
    # Get the first timestamp's data (most recent)
    first_timestamp = next(iter(payload.keys()))
    register_data = payload[first_timestamp]
    
    register_values = []
    
    # Get register definitions from the profile
    profile = INVERTER_PROFILES[model]
    registers = profile[ProfileKey.REGISTERS]
    
    # Create RegisterValue objects for each register in the profile that exists in the JWT
    for reg_def in registers:
        start_reg = reg_def[RegistersKey.START_REGISTER]
        num_regs = reg_def[RegistersKey.NUM_OF_REGISTERS]
        unit = reg_def[RegistersKey.UNIT]
        description = reg_def[RegistersKey.DESCRIPTION]
        name = reg_def.get(RegistersKey.NAME, "")
        
        # Check if this register exists in the JWT data
        if str(start_reg) in register_data:
            register_value = RegisterDefinition(
                name=name,
                description=description,
                unit=unit,
                address=start_reg,
                size=num_regs,
                function_code=reg_def[RegistersKey.FUNCTION_CODE],
                data_type=reg_def[RegistersKey.DATA_TYPE],
                scale_factor=reg_def[RegistersKey.SCALE_FACTOR],
                endianness=reg_def[RegistersKey.ENDIANNESS]
            )
            
            # Convert the raw values to bytes
            raw_bytes = bytearray()
            for i in range(num_regs):
                reg_addr = str(start_reg + i)
                if reg_addr in register_data:
                    # Each register is 2 bytes in big-endian format
                    reg_value = register_data[reg_addr]
                    raw_bytes.extend(reg_value.to_bytes(2, 'big', signed=False))
            
            # Interpret the value using the RegisterValue's _interpret_value method
            _, interpreted_value = register_value._interpret_value(raw_bytes)
            register_values.append((register_value, interpreted_value))
    
    return register_values 