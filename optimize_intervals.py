from src.inverters import INVERTER_PROFILES
from src.modbus.register_definition_keys import RegistersKey
from typing import List, Tuple, Dict
import argparse
from interval_counter import get_profile_intervals as get_original_intervals
from tabulate import tabulate

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


def print_legend():
    legend = """
Legend:
- Profile: Name of the inverter manufacturer/model
- Actual Regs: Number of actual registers being read from the inverter
- Total Regs: Total number of registers covered (including gaps between registers)
- Original Reads: Number of Modbus register blocks that need to be read individually
- Optimized Reads: Number of Modbus register blocks after optimization (combining adjacent registers into blocks of 125)
- Original Time (s): Time taken to read all blocks using original method (assuming 200ms per block)
- Optimized Time (s): Time taken to read all blocks using optimized method (assuming 200ms per block)
- Time Saved (s): Difference between original and optimized read times

Note: All timing calculations assume a hypothetical read time of 200ms per Modbus register block. 
      Actual read times may vary depending on network conditions and inverter response times.
"""
    print(legend)


def analyze_optimized_intervals(show_intervals: bool = False):
    POLL_TIME_MS = 200  # Time per block in milliseconds
    print("Register Block Analysis:")
    print("Comparing read timings between original register blocks (as defined) vs")
    print("optimized blocks (combining adjacent registers into blocks of 125) to reduce total reads")
    print("-" * 70)

    table_data = []
    headers = ["Profile", "Actual Regs", "Total Regs", "Original Reads",
               "Optimized Reads", "Original Time (s)", "Optimized Time (s)", "Time Saved (s)"]

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

        # Add row to table data
        table_data.append([
            profile_name,
            actual_registers,
            total_registers,
            num_original_intervals,
            num_optimized_intervals,
            f"{original_poll_time:.1f}",
            f"{optimized_poll_time:.1f}",
            f"{original_poll_time - optimized_poll_time:.1f}"
        ])

        if show_intervals:
            print(f"\n{profile_name} register blocks:")
            intervals_data = [(start, end, end - start + 1)
                              for start, end in optimized_intervals]
            print(tabulate(intervals_data,
                           headers=["Start", "End", "Size"],
                           tablefmt="grid",
                           numalign="right"))
            print()

    # Print the main results table
    print("\n" + tabulate(table_data, headers=headers,
          tablefmt="grid", numalign="right"))

    # Print the legend
    print_legend()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Analyze Modbus register intervals')
    parser.add_argument('--show-intervals', '-i', action='store_true',
                        help='Show detailed interval information')
    args = parser.parse_args()

    analyze_optimized_intervals(args.show_intervals)
