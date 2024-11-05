from typing import List


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
    schedules: List[List[List[str]]], periods: List[List[str]], durationMins: int
) -> List[List[str]]:

    # Process: merge overlapping intervals, convert timestamps to minutes,
    # find free time slots using duration and boundaries in period, convert back to timestamps

    free_slots = []

    # Get latest login and earliest logout. This will be the boundaries we will be using.
    latestLogin, earliestLogout = convert_ts_to_mins(periods[0][0]), convert_ts_to_mins(
        periods[0][1]
    )
    for login, logout in periods:
        latestLogin = max(latestLogin, convert_ts_to_mins(login))
        earliestLogout = min(earliestLogout, convert_ts_to_mins(logout))

    latestLogin, earliestLogout = convert_mins_to_ts(latestLogin), convert_mins_to_ts(
        earliestLogout
    )

    print("Latest Login: ", latestLogin)
    print("Earliest Logout: ", earliestLogout)

    busy_slots = []

    # Merge overlapping intervals into one interval
    for schedule in schedules:
        busy_slots += schedule

    busy_slots = merge_intervals(
        [[convert_ts_to_mins(x), convert_ts_to_mins(y)] for x, y in busy_slots]
    )

    print(busy_slots)

    # Find free time slots given the duration of the meeting and boundaries
    # Start at latestLogin and end at earliestLogout and iterate by durationMins

    return free_slots


person1_Schedule = [["7:00", "8:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
person1_DailyAct = ["9:00", "19:00"]
person2_Schedule = [
    ["9:00", "10:30"],
    ["12:20", "13:30"],
    ["14:00", "15:00"],
    ["16:00", "17:00"],
]
person2_DailyAct = ["9:00", "18:30"]
duration_of_meeting = 30

x = matching_group_schedules(
    [person1_Schedule, person2_Schedule],
    [person1_DailyAct, person2_DailyAct],
    duration_of_meeting,
)
print("Output: ", x)
