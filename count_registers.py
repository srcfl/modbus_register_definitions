from src.inverters import INVERTER_PROFILES
from src.modbus.register_definition_keys import RegistersKey


def count_registers():
    print("Number of defined registers per inverter:")
    print("-" * 50)

    for profile_name, profile in INVERTER_PROFILES.items():
        total_registers = sum(reg[RegistersKey.NUM_OF_REGISTERS]
                              for reg in profile.get('registers', []))
        print(f"{profile_name:<15} : {total_registers:>5} registers")


if __name__ == "__main__":
    count_registers()
