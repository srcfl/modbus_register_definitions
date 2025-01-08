from src.inverters import INVERTER_PROFILES
from src.modbus.register_definition_keys import RegistersKey
from typing import List, Tuple, Dict


def find_register_intervals(registers: List[Dict]) -> List[Tuple[int, int]]:
    if not registers:
        return []

    # Sort registers by start register
    sorted_regs = sorted(
        registers, key=lambda x: x[RegistersKey.START_REGISTER])

    intervals = []
    current_start = sorted_regs[0][RegistersKey.START_REGISTER]
    current_end = current_start + \
        sorted_regs[0][RegistersKey.NUM_OF_REGISTERS] - 1

    for reg in sorted_regs[1:]:
        start = reg[RegistersKey.START_REGISTER]
        end = start + reg[RegistersKey.NUM_OF_REGISTERS] - 1

        # If this register starts right after the previous interval ends
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            # Gap found, store the current interval and start a new one
            intervals.append((current_start, current_end))
            current_start = start
            current_end = end

    # Add the last interval
    intervals.append((current_start, current_end))
    return intervals


def get_profile_intervals(profile: Dict) -> int:
    """Return the number of intervals needed to read all registers in a profile."""
    return len(find_register_intervals(profile.get('registers', [])))


def analyze_registers():
    POLL_TIME_MS = 200  # Time per interval in milliseconds
    print("Register analysis for each inverter profile:")
    print("-" * 70)

    for profile_name, profile in INVERTER_PROFILES.items():
        registers = profile.get('registers', [])
        intervals = find_register_intervals(registers)
        num_intervals = len(intervals)
        total_poll_time_ms = num_intervals * POLL_TIME_MS
        total_poll_time_s = total_poll_time_ms / 1000

        print(f"\n{profile_name}:")
        print(f"Number of intervals: {num_intervals}")
        print(f"Total polling time: {total_poll_time_s:.1f} seconds")
        print("Register intervals:")
        for start, end in intervals:
            size = end - start + 1
            print(f"  {start:>6} - {end:<6} ({size:>4} registers)")


if __name__ == "__main__":
    analyze_registers()
