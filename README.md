# Inverter Modbus Registers

A python library for decoding and displaying Modbus registers from solar inverters.

## Setup

1. Create a virtual environment and activate it:

```bash
python -m venv .venv && source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main script:

```bash
python main.py
```

## Example output

```
Huawei Inverter Register Values:
 Register   | Name                            | Value                  | Description
------------+---------------------------------+------------------------+----------------------
 30000      | Model                           | SUN2000-3KTL-L1        | Model
 30015      | Serial Number                   | 101010891010           | Device serial number
 30025      | Part Number                     | 015353535353           | Part number
 30070      | Model ID                        | 348                    | Model identifier
 30071      | Number of PV Strings            | 2                      | Number of PV strings
 30072      | Number of MPP Trackers          | 2                      | Number of MPP tracke
 30073      | Rated Power                     | 3.0 kW                 | Rated power (Pn)
 30075      | Maximum Active Power            | 3.3000000000000003 kW  | Maximum active power
 30077      | Maximum Apparent Power          | 3.3000000000000003 kVA | Maximum apparent pow
 30079      | Maximum Reactive Power Fed      | 1.98 kVar              | Maximum reactive pow
 30081      | Maximum Reactive Power Absorbed | -1.98 kVar             | Maximum reactive pow
 32000      | State 1                         | None                   | Bit 0: standby, Bit
 32002      | State 2                         | None                   | Bit 0: locking statu
 32003      | State 3                         | None                   | Bit 0: off-grid (0:
 32016      | PV1 Voltage                     | 118.80000000000001 V   | PV string 1 voltage
 32017      | PV1 Current                     | 7.96 A                 | PV string 1 current
 32018      | PV2 Voltage                     | 119.0 V                | PV string 2 voltage
 32019      | PV2 Current                     | 8.1 A                  | PV string 2 current
 32020      | PV3 Voltage                     | 0.0 V                  | PV string 3 voltage
 32021      | PV3 Current                     | 0.0 A                  | PV string 3 current
 32022      | PV4 Voltage                     | 0.0 V                  | PV string 4 voltage
 32023      | PV4 Current                     | 0.0 A                  | PV string 4 current
 32064      | Input Power                     | 1.9160000000000001 kW  | Input power
 32066      | Grid Voltage AB                 | 237.60000000000002 V   | Power grid voltage/L
 32067      | Grid Voltage BC                 | 0.0 V                  | Line voltage between
 32068      | Grid Voltage CA                 | 0.0 V                  | Line voltage between
 32069      | Phase A Voltage                 | 118.9 V                | Phase A voltage
 32070      | Phase B Voltage                 | 0.1 V                  | Phase B voltage
 32071      | Phase C Voltage                 | 0.0 V                  | Phase C voltage
 32072      | Phase A Current                 | 0.8270000000000001 A   | Power grid current/P
 32074      | Phase B Current                 | 0.0 A                  | Phase B current
 32076      | Phase C Current                 | 0.0 A                  | Phase C current
 32078      | Peak Active Power               | 2.076 kW               | Peak active power of
 32080      | Active Power                    | 0.168 kW               | Active power
 32082      | Reactive Power                  | -0.001 kVar            | Reactive power
 32084      | Power Factor                    | 1.0                    | Power factor
 32085      | Grid Frequency                  | 50.0 Hz                | Grid frequency
 32086      | Efficiency                      | 100.0 %                | Inverter efficiency
 32087      | Internal Temperature            | 31.1 °C                | Internal temperature
 32088      | Insulation Resistance           | 3.0 MΩ                 | Insulation resistanc
 32089      | Device Status                   | 513                    | Device status codes:
 32090      | Fault Code                      | 0                      | Current fault code
 32091      | Startup Time                    | 1735374392             | Startup time in epoc
 32093      | Shutdown Time                   | 4294967295             | Shutdown time in epo
 32106      | Accumulated Energy Yield        | 3699.03 kWh            | Accumulated energy y
 32114      | Daily Energy Yield              | 1.96 kWh               | Daily energy yield
```
