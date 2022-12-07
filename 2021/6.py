from collections import defaultdict

from utils import parse_as_ints

test_input = "3,4,3,1,2"


def p1(school: list, days: int) -> int:
    if days:
        new = []
        for fish in school:
            if fish == 0:
                new.extend([6, 8])
            else:
                new.append(fish - 1)
        return p1(new, days - 1)
    else:
        return len(school)


def p2(school: list, days: int) -> int:
    # First attempt at optimization, using two tactics:
    # 1. Replace recursion with a loops, to prevent function call overhead
    # 2. Group similarly-timered fish in a batch.
    # This doesn't get the job done fast enough, though, which is puzzling.
    def nonrecursive(school: list, days: int) -> int:
        while days:
            new = []
            for fish in school:
                if fish == 0:
                    new.extend([6, 8])
                else:
                    new.append(fish - 1)
            days -= 1
            school = new
        return len(school)

    uniques = set(school)
    result = 0
    for fish in uniques:
        result += nonrecursive([fish], days) * school.count(fish)
    return result


def p2_2(school: list, days: int) -> int:
    result = 0
    # We track fish as a dict of (timer, days): occurrences
    new_school = defaultdict(int)
    for fish in school:
        new_school[(fish, days)] += 1
    while new_school:
        (timer, days), occurrences = new_school.popitem()
        # print(f"NEW LOOP: {timer}, {days}, {occurrences}")
        if days >= timer and timer > 0:
            days -= timer
            # print(f"- (Priming) Days: {days}")
            if days > 7:
                new_school[(8, days)] += occurrences
            else:
                # Rather than append these new fish that won't have time to
                # mature, just count them now.
                result += occurrences
            #     print(f"- result: {result} (up by {occurrences} short-circuit)")
            # print(f"- new_school: {new_school}")
        while days >= 7:
            days -= 7
            if days > 7:
                new_school[(8, days)] += occurrences
            else:
                # Rather than append these new fish that won't have time to
                # mature, just count them now.
                result += occurrences
            #     print(f"- result: {result} (up by {occurrences} short-circuit)")
            # print(f"- Days: {days}")
            # print(f"- new_school: {new_school}")
        result += occurrences
        # print(f"- result: {result} (up by {occurrences})")
    return result


# Stolen from https://www.reddit.com/r/adventofcode/comments/r9z49j/comment/hnv54q3/?utm_source=share&utm_medium=web2x&context=3
# I don't really understand it.
def solve(data, days):
    tracker = [data.count(i) for i in range(9)]
    for day in range(days):
        tracker[(day + 7) % 9] += tracker[day % 9]
    return sum(tracker)


if __name__ == "__main__":
    test_school = [int(x) for x in test_input.split(",")]
    assert(p1(test_school, days=18) == 26)
    assert(p1(test_school, days=80) == 5934)
    print(p1(parse_as_ints("6-input.txt", ","), days=80))
    try:
        expected = 26
        received = solve(test_school, days=18)
        assert(expected == received)
        expected = 5934
        received = solve(test_school, days=80)
        assert(expected == received)
        expected = 26984457539
        received = solve(test_school, days=256)
        assert(expected == received)
    except AssertionError:
        print(f"Expected: {expected}; received: {received}")
        raise
    print("Assertions passed")
    print(solve(parse_as_ints("6-input.txt", ","), days=256))
