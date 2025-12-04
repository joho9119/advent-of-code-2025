from copy import copy

try:
    from puzzle_03_raw_list import RAW_EXAMPLE_LIST, REAL_PUZZLE_LIST
except ImportError:
    RAW_EXAMPLE_LIST = []
    REAL_PUZZLE_LIST = []


def find_highest_joltage_for(battery: str):
    jolts = [int(jolt) for jolt in battery]
    max_jolt = max(jolts)

    cached = copy(jolts)
    cached.remove(max_jolt)     # remove first instance
    second_max = max(cached)    # then get the max

    if max_jolt == second_max:  # found double max path - early break
        return str(max_jolt) + str(second_max)
    else:
        # check indexes of each
        max_idx = jolts.index(max_jolt)
        second_idx = jolts.index(second_max)

        # if first larger came before second larger, then return.
        if max_idx < second_idx:
            return str(max_jolt) + str(second_max)
        # If max is at last idx, then flip
        if max_idx == len(jolts) - 1:
            return str(second_max) + str(max_jolt)
        # Last, find the largest --after-- the first max
        new_second_max = max(jolts[max_idx+1:])
        return str(max_jolt) + str(new_second_max)


def get_max_jolts_for(batteries: list[str]) -> list[int]:
    max_jolts_per_battery = []
    print(batteries)

    for battery in batteries:
        jolts = find_highest_joltage_for(battery)
        joltage = int(jolts)
        max_jolts_per_battery.append(joltage)

    return max_jolts_per_battery


def display_total_jolts(joltage_list: list[str]):
    max_jolts_per_battery = get_max_jolts_for(joltage_list)
    print(max_jolts_per_battery)
    total_jolts = sum(max_jolts_per_battery)
    print(f"Total JOLTS! {total_jolts}")


def main():
    print("Example")
    display_total_jolts(RAW_EXAMPLE_LIST)
    print("Exercise 1")
    display_total_jolts(REAL_PUZZLE_LIST)

main()
