from src.inverters import INVERTER_PROFILES
from src.modbus.register_definition_keys import RegistersKey
from typing import List, Tuple, Dict
import argparse
from interval_counter import get_profile_intervals as get_original_intervals

MAX_REGISTERS_PER_READ = 125


def find_optimized_intervals(registers: List[Dict]) -> List[Tuple[int, int]]:
    if not registers:
        return []

    # Sort registers by start register
    sorted_regs = sorted(
        registers, key=lambda x: x[RegistersKey.START_REGISTER])

    # Find the minimum and maximum register addresses
    min_register = sorted_regs[0][RegistersKey.START_REGISTER]
    max_register = max(
        reg[RegistersKey.START_REGISTER] +
        reg[RegistersKey.NUM_OF_REGISTERS] - 1
        for reg in sorted_regs
    )

    # Split the entire range into chunks of 125 registers
    optimized_intervals = []
    current = min_register
    while current <= max_register:
        chunk_end = min(current + MAX_REGISTERS_PER_READ - 1, max_register)
        optimized_intervals.append((current, chunk_end))
        current = chunk_end + 1

    return optimized_intervals


def get_optimized_intervals_count(profile: Dict) -> int:
    """Return the number of intervals needed to read all registers in a profile using optimized method."""
    return len(find_optimized_intervals(profile.get('registers', [])))


def analyze_optimized_intervals(show_intervals: bool = False):
    POLL_TIME_MS = 200  # Time per interval in milliseconds
    print("Register analysis (reading in blocks of 125):")
    print("-" * 70)

    for profile_name, profile in INVERTER_PROFILES.items():
        registers = profile.get('registers', [])
        optimized_intervals = find_optimized_intervals(registers)

        # Calculate metrics using both methods
        num_optimized_intervals = len(optimized_intervals)
        num_original_intervals = get_original_intervals(profile)

        # Calculate polling times
        optimized_poll_time = num_optimized_intervals * POLL_TIME_MS / 1000
        original_poll_time = num_original_intervals * POLL_TIME_MS / 1000

        # Calculate register counts
        total_registers = sum(end - start + 1 for start,
                              end in optimized_intervals)
        actual_registers = sum(reg[RegistersKey.NUM_OF_REGISTERS]
                               for reg in registers)

        print(f"\n{profile_name}:")
        print(f"Actual registers : {actual_registers}")
        print(f"Total registers : {total_registers} (including gaps)")
        print(f"Original reads  : {num_original_intervals}")
        print(f"Optimized reads : {num_optimized_intervals}")
        print(f"Original time   : {original_poll_time:.1f} seconds")
        print(f"Optimized time  : {optimized_poll_time:.1f} seconds")
        print(
            f"Time saved      : {original_poll_time - optimized_poll_time:.1f} seconds")

        if show_intervals:
            print("\nRead intervals:")
            for start, end in optimized_intervals:
                size = end - start + 1
                print(f"  {start:>6} - {end:<6} ({size:>4} registers)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Analyze Modbus register intervals')
    parser.add_argument('--show-intervals', '-i', action='store_true',
                        help='Show detailed interval information')
    args = parser.parse_args()

    analyze_optimized_intervals(args.show_intervals)
