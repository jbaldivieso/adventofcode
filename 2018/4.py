from collections import defaultdict, Counter
import re

from utils import parse_as_str


test_data = [
    "[1518-11-01 00:00] Guard #10 begins shift",
    "[1518-11-01 00:05] falls asleep",
    "[1518-11-01 00:25] wakes up",
    "[1518-11-01 00:30] falls asleep",
    "[1518-11-01 00:55] wakes up",
    "[1518-11-01 23:58] Guard #99 begins shift",
    "[1518-11-02 00:40] falls asleep",
    "[1518-11-02 00:50] wakes up",
    "[1518-11-03 00:05] Guard #10 begins shift",
    "[1518-11-03 00:24] falls asleep",
    "[1518-11-03 00:29] wakes up",
    "[1518-11-04 00:02] Guard #99 begins shift",
    "[1518-11-04 00:36] falls asleep",
    "[1518-11-04 00:46] wakes up",
    "[1518-11-05 00:03] Guard #99 begins shift",
    "[1518-11-05 00:45] falls asleep",
    "[1518-11-05 00:55] wakes up",
]


timestamp = r"\[\d+-\d\d-\d\d \d\d:(?P<minutes>\d\d)\]"
shift_pattern = re.compile(timestamp + r" Guard #(?P<id>\d+) begins shift")
action_pattern = re.compile(timestamp + r" (?P<action>.*)$")

data = parse_as_str("4-input.txt")
data.sort()


def get_sleep_data(data):
    # dict mapping guard id to the list of minutes that he was asleep, all
    # combined
    guards = defaultdict(list)
    for line in data:
        shift_attempt = re.match(shift_pattern, line)
        if shift_attempt:
            this_guard = shift_attempt.groupdict()["id"]
        else:
            action_match = re.match(action_pattern, line).groupdict()
            minutes = int(action_match["minutes"])
            if action_match["action"] == "falls asleep":
                sleep_start = minutes
            else:
                guards[this_guard].extend(range(sleep_start, minutes))
    return guards


def part1(data):
    guards = get_sleep_data(data)
    # The guard that slept the most minutes is the one who has the longest
    # list! (We're assuming that, at least for the who slept the most, the
    # total minutes will be a unique number.)
    by_sleep_minutes = {len(v): k for k, v in guards.items()}
    biggest_total = sorted(by_sleep_minutes, reverse=True)[0]
    winner_id = by_sleep_minutes[biggest_total]
    counter = Counter(guards[winner_id])
    return int(winner_id) * counter.most_common(1)[0][0]


assert part1(test_data) == 240
print("Made it through part1 tests")
print(f"Part 1: {part1(data)}")


def part2(data):
    guards = get_sleep_data(data)
    by_sleep_minutes = {k: Counter(v).most_common(1)[0] for k, v in guards.items()}
    by_sleep_minutes = sorted(by_sleep_minutes.items(), key=lambda t: t[1][1])
    winner_id, minute_counter = by_sleep_minutes[-1]  # minute_counter: tuple
    return int(winner_id) * minute_counter[0]


assert part2(test_data) == 4455
print("Made it through part2 tests")
print(f"Part 2: {part2(data)}")
