from ...modbus.register_definition_keys import (
    ProfileKey,
    RegistersKey,
    FunctionCodeKey,
    DataTypeKey,
    EndiannessKey,
)


ferroamp_profile = {
    ProfileKey.REGISTERS: [
        {
            RegistersKey.NAME: "Modbus Major Version",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 1004,
            RegistersKey.NUM_OF_REGISTERS: 1,
            RegistersKey.DATA_TYPE: DataTypeKey.U16,
            RegistersKey.UNIT: "enum",
            RegistersKey.DESCRIPTION: "Modbus major version in use",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Inverter Status",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2000,
            RegistersKey.NUM_OF_REGISTERS: 1,
            RegistersKey.DATA_TYPE: DataTypeKey.U16,
            RegistersKey.UNIT: "enum",
            RegistersKey.DESCRIPTION: "0 => unavailable, 1 =>idle, 2 => running, 3 => fault",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid Frequency",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2016,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Hz",
            RegistersKey.DESCRIPTION: "Grid frequency",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid Voltage L1",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2032,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Vrms",
            RegistersKey.DESCRIPTION: "Grid voltage L1",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },
        {
            RegistersKey.NAME: "Grid Voltage L2",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2036,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Vrms",
            RegistersKey.DESCRIPTION: "Grid voltage L2",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid Voltage L3",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2040,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Vrms",
            RegistersKey.DESCRIPTION: "Grid voltage L3",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid Neutral Voltage",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2044,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Vrms",
            RegistersKey.DESCRIPTION: "Grid neutral voltage (Not implemented yet)",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Energy to DC-Nanogrid",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2064,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kWh",
            RegistersKey.DESCRIPTION: "Incoming Energy from AC Grid to DC-Nanogrid",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Energy from DC-Nanogrid",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2068,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kWh",
            RegistersKey.DESCRIPTION: "Outgoing Energy from DCNanogrid to AC Grid",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Inverter Active Power",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2100,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kW",
            RegistersKey.DESCRIPTION: "Power based on inverter active currents",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Inverter Reactive Power",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2104,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kVAr",
            RegistersKey.DESCRIPTION: "Power based on inverter reactive currents",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },
        {
            RegistersKey.NAME: "Inverter Apparent Power",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2108,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kVA",
            RegistersKey.DESCRIPTION: "Power based on inverter RMS currents",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Inverter Active Current L1",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2112,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using internal current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Inverter Active Current L2",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2116,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using internal current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Inverter Active Current L3",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2120,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using internal current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Inverter Reactive Current L1",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2124,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using internal current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Inverter Reactive Current L2",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2128,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using internal current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Inverter Reactive Current L3",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2132,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using internal current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Inverter RMS Current L1",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2136,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using internal current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Inverter RMS Current L2",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2140,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using internal current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Inverter RMS Current L3",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 2144,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using internal current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },
        {
            RegistersKey.NAME: "Energy Exported To Grid",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3064,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kWh",
            RegistersKey.DESCRIPTION: "Outgoing Energy from facility to AC Grid",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Energy Imported From Grid",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3068,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kWh",
            RegistersKey.DESCRIPTION: "Incoming Energy from AC Grid to facility",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid Active Power",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3100,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kW",
            RegistersKey.DESCRIPTION: "Power based on grid active currents",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid Reactive Power",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3104,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kVAr",
            RegistersKey.DESCRIPTION: "Power based on grid reactive currents",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid Apparent Power",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3108,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kVA",
            RegistersKey.DESCRIPTION: "Power based on grid RMS currents",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid Active Current L1",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3112,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using external current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid Active Current L2",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3116,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using external current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid Active Current L3",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3120,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using external current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid Reactive Current L1",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3124,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using external current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },
        {
            RegistersKey.NAME: "Grid Reactive Current L2",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3128,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using external current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid Reactive Current L3",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3132,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using external current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid RMS Current L1",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3136,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using external current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid RMS Current L2",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3140,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using external current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Grid RMS Current L3",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 3144,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "Current measured using external current sensors",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Load Production Energy",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 4064,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kWh",
            RegistersKey.DESCRIPTION: "Outgoing Energy from facility to AC Grid",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Load Consumption Energy",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 4068,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kWh",
            RegistersKey.DESCRIPTION: "Incoming Energy from AC Grid to facility loads",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },
        {
            RegistersKey.NAME: "Load Active Power",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 4100,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kW",
            RegistersKey.DESCRIPTION: "Power based on load active currents",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Load Reactive Power",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 4104,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kVAr",
            RegistersKey.DESCRIPTION: "Power based on load reactive currents",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Load Active Current L1",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 4112,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Load Active Current L2",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 4116,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Load Active Current L3",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 4120,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Load Reactive Current L1",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 4124,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Load Reactive Current L2",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 4128,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Load Reactive Current L3",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 4132,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "Arms",
            RegistersKey.DESCRIPTION: "",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },
        {
            RegistersKey.NAME: "Number of idle SSOs",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 5000,
            RegistersKey.NUM_OF_REGISTERS: 1,
            RegistersKey.DATA_TYPE: DataTypeKey.U16,
            RegistersKey.UNIT: "number",
            RegistersKey.DESCRIPTION: "Number of SSOs not producing any energy",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Number of running SSOs",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 5002,
            RegistersKey.NUM_OF_REGISTERS: 1,
            RegistersKey.DATA_TYPE: DataTypeKey.U16,
            RegistersKey.UNIT: "number",
            RegistersKey.DESCRIPTION: "Number of running SSOs",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Number of faulty SSOs",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 5004,
            RegistersKey.NUM_OF_REGISTERS: 1,
            RegistersKey.DATA_TYPE: DataTypeKey.U16,
            RegistersKey.UNIT: "number",
            RegistersKey.DESCRIPTION: "Number of SSOs not working properly",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Energy produced",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 5064,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kWh",
            RegistersKey.DESCRIPTION: "Outgoing Energy from PV panels to DC-Nanogrid",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Solar Output Power",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 5100,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kW",
            RegistersKey.DESCRIPTION: "Outgoing power from PV panels to the DC-Nanogrid",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },
        {
            RegistersKey.NAME: "Battery Mode",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6000,
            RegistersKey.NUM_OF_REGISTERS: 1,
            RegistersKey.DATA_TYPE: DataTypeKey.U16,
            RegistersKey.UNIT: "enum",
            RegistersKey.DESCRIPTION: "0 => Default; 1=> Power-mode Power from batteries to DC-Nanogrid",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Battery Power Reference",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6064,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kW",
            RegistersKey.DESCRIPTION: "-ve power implies charging",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Number of idle batteries",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6000,
            RegistersKey.NUM_OF_REGISTERS: 1,
            RegistersKey.DATA_TYPE: DataTypeKey.U16,
            RegistersKey.UNIT: "number",
            RegistersKey.DESCRIPTION: "Number of batteries not configured for operation",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Number of running batteries",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6002,
            RegistersKey.NUM_OF_REGISTERS: 1,
            RegistersKey.DATA_TYPE: DataTypeKey.U16,
            RegistersKey.UNIT: "number",
            RegistersKey.DESCRIPTION: "Number of running batteries",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Number of faulty batteries",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6068,
            RegistersKey.NUM_OF_REGISTERS: 1,
            RegistersKey.DATA_TYPE: DataTypeKey.U16,
            RegistersKey.UNIT: "number",
            RegistersKey.DESCRIPTION: "Number of batteries not working properly",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Rated capacity",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6008,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kWh",
            RegistersKey.DESCRIPTION: "Aggregated Rated Capacity of all connected batteries",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "State of Health",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6012,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "%",
            RegistersKey.DESCRIPTION: "Aggregated State of Health of all connected batteries",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },
        {
            RegistersKey.NAME: "State of Charge",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6016,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "%",
            RegistersKey.DESCRIPTION: "Aggregated State of Charge of all connected batteries",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Energy from battery",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6064,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kWh",
            RegistersKey.DESCRIPTION: "Outgoing Energy from Discharging Batteries to DC-Nanogrid",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Energy to battery",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6068,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kWh",
            RegistersKey.DESCRIPTION: "Incoming Energy from DC-nanogrid to Charging Batteries",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Battery Output Power",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6100,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kWh",
            RegistersKey.DESCRIPTION: "Power from all batteries to the DC-Nanogrid -ve power implies charging",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Battery Mode System Value",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6104,
            RegistersKey.NUM_OF_REGISTERS: 1,
            RegistersKey.DATA_TYPE: DataTypeKey.U16,
            RegistersKey.UNIT: "enum",
            RegistersKey.DESCRIPTION: "0 => Default; 1=> Power-mode Power from batteries to DC-Nanogrid",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Battery Power Reference System Value",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 6106,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "kWh",
            RegistersKey.DESCRIPTION: "-ve power implies charging",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },
        {
            RegistersKey.NAME: "Limit Import System Value",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 8000,
            RegistersKey.NUM_OF_REGISTERS: 1,
            RegistersKey.DATA_TYPE: DataTypeKey.U16,
            RegistersKey.UNIT: "enum",
            RegistersKey.DESCRIPTION: "0 => Don't limit import, 1 => Limit import",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Import Threshold System Value",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 8002,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "W",
            RegistersKey.DESCRIPTION: "Grid power import threshold, system value",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Limit Export System Value",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 8010,
            RegistersKey.NUM_OF_REGISTERS: 1,
            RegistersKey.DATA_TYPE: DataTypeKey.U16,
            RegistersKey.UNIT: "enum",
            RegistersKey.DESCRIPTION: "0 => Don't limit export, 1 => Limit export",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        },

        {
            RegistersKey.NAME: "Export Threshold System Value",
            RegistersKey.FUNCTION_CODE: FunctionCodeKey.READ_HOLDING_REGISTERS,
            RegistersKey.START_REGISTER: 8012,
            RegistersKey.NUM_OF_REGISTERS: 2,
            RegistersKey.DATA_TYPE: DataTypeKey.F32,
            RegistersKey.UNIT: "W",
            RegistersKey.DESCRIPTION: "Grid power export threshold, system value",
            RegistersKey.SCALE_FACTOR: 1,
            RegistersKey.ENDIANNESS: EndiannessKey.LITTLE
        }
    ]
}
