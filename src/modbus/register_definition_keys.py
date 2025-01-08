from enum import Enum


class ProfileKey(str, Enum):
    NAME = 'name'
    VERSION = 'version'
    VERBOSE_ALWAYS = 'verbose_always'
    MODEL_GROUP = 'model_group'
    DISPLAY_NAME = 'display_name'
    PROTOCOL = 'protocol'
    DESCRIPTION = 'description'
    REGISTERS_VERBOSE = 'registers_verbose'
    REGISTERS = 'registers'
    BASE_URL = 'base_url'
    ENDPOINTS = 'endpoints'
    KEYWORDS = 'keywords'


class ProtocolKey(str, Enum):
    MODBUS = 'modbus'
    SOLARMAN = 'solarman'
    SUNSPEC = 'sunspec'
    REST = 'rest'


class RegistersKey(str, Enum):
    NAME = 'name'
    FUNCTION_CODE = 'function_code'
    START_REGISTER = 's∑tart_register'
    NUM_OF_REGISTERS = 'num_of_registers'
    DATA_TYPE = 'data_type'
    UNIT = 'unit'
    DESCRIPTION = 'description'
    SCALE_FACTOR = 'scale_factor'
    ENDIANNESS = 'endianness'


class DataTypeKey(str, Enum):
    U16 = 'U16'    # Unsigned 16-bit integer
    I16 = 'I16'    # Signed 16-bit integer
    U32 = 'U32'    # Unsigned 32-bit integer
    I32 = 'I32'    # Signed 32-bit integer
    F32 = 'F32'    # 32-bit floating point
    U64 = 'U64'    # Unsigned 64-bit integer
    I64 = 'I64'    # Signed 64-bit integer
    STR = 'STR'    # String
    BITFIELD16 = 'BITFIELD16'  # 16-bit bitfield
    BITFIELD32 = 'BITFIELD32'  # 32-bit bitfield
    MLD = 'MLD'  # Multi-level data / Multi-level Definition ?
    BYTES = 'BYTES'  # Bytes
    ENUM16 = 'ENUM16'  # 16-bit enumeration
    SUNSSF = 'SUNSSF'  # SunSpec Scale Factor Field


class EndiannessKey(str, Enum):
    BIG = 'big'
    LITTLE = 'little'


class FunctionCodeKey(int, Enum):
    READ_HOLDING_REGISTERS = 0x03
    READ_INPUT_REGISTERS = 0x04


class DeviceCategoryKey(str, Enum):
    INVERTERS = 'inverters'
    METERS = 'meters'
