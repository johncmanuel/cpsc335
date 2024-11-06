from typing import List
from ast import literal_eval


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    new_interval = []
    intervals = sorted(intervals, key=lambda x: x[0])
    for x, y in intervals:
        if not new_interval or new_interval[-1][1] < x:
            new_interval.append([x, y])
        else:
            new_interval[-1][1] = max(new_interval[-1][1], y)
    return new_interval


# Helper functions for calculating between timestamps and minutes for easier calculations


def convert_ts_to_mins(ts: str) -> int:
    h, m = map(int, ts.split(":"))
    return h * 60 + m


def convert_mins_to_ts(mins: int) -> str:
    h, m = divmod(mins, 60)
    return f"{h:02d}:{m:02d}"


# Input:
# 1. List of lists representing people's schedules
# 2. Working period for all people. Only contains (login, logout)
# 3. Duration of the meeting
# Output:
# Array of compatible schedules
def matching_group_schedules(
    schedules: List[List[List[str]]], periods: List[List[str]], duration_mins: int
) -> List[List[str]]:

    # Process: merge overlapping intervals, convert timestamps to minutes,
    # find free time slots using the merged interval, duration, and boundaries, then convert back to timestamps

    free_slots = []

    print(periods, periods[0])
    # Get latest login and earliest logout. This will be the boundaries we will be using.
    latest_login, earliest_logout = convert_ts_to_mins(
        periods[0][0]
    ), convert_ts_to_mins(periods[0][1])

    for login, logout in periods:
        latest_login = max(latest_login, convert_ts_to_mins(login))
        earliest_logout = min(earliest_logout, convert_ts_to_mins(logout))

    busy_slots = []

    # Merge overlapping intervals into one interval
    for schedule in schedules:
        busy_slots += schedule

    busy_slots = merge_intervals(
        [[convert_ts_to_mins(x), convert_ts_to_mins(y)] for x, y in busy_slots]
    )

    # print(latest_login, earliest_logout, busy_slots, duration_mins)

    # Find free time slots given the duration of the meeting and boundaries
    # by checking the difference between the current slot's end value
    # and the next slot's start value
    for i in range(len(busy_slots[1:])):
        curr_slot, next_slot = busy_slots[i], busy_slots[i + 1]
        if (
            next_slot[0] - curr_slot[1] >= duration_mins
            and curr_slot[0] >= latest_login
        ):
            free_slots.append([curr_slot[1], next_slot[0]])

    # Check if last slot's end value can work
    last_val = busy_slots[-1][1]
    if earliest_logout - last_val >= duration_mins:
        free_slots.append([last_val, earliest_logout])

    free_slots = [[convert_mins_to_ts(x), convert_mins_to_ts(y)] for x, y in free_slots]

    return free_slots


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        test_cases = f.read().strip().split("\n\n")

    output = []

    for test_case in test_cases:
        lines = test_case.split("\n")
        schedules = literal_eval(lines[0])
        periods = literal_eval(lines[1])
        duration_of_meeting = int(lines[2].strip())

        res = matching_group_schedules(schedules, periods, duration_of_meeting)
        output.append(res)

    # Write output to file
    with open("output.txt", "w") as f:
        for slots in output:
            f.write(str(slots) + "\n")
