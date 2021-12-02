from collections import Counter
from itertools import compress
from IPython.core import debugger
debug = debugger.Pdb().set_trace

test_input1 = """
16
10
15
5
1
11
7
19
6
12
4
"""

test_input2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


def p1(data):
    deltas = []
    for i in range(1, len(data)):
        deltas.append(data[i] - data[i - 1])
    counts = Counter(deltas)
    return counts[1] * counts[3]


def dec_to_mask(dec, length):
    """Given a decimal int @dec, convert it to binary, convert /that/ to a list
    of 0s/1s, and then left pad that list as needed to get its length to
    exactly @length.
    """
    result = [int(i) for i in bin(dec)[2:]]
    if len(result) < length:
        result = [0 for i in range(length - len(result))] + result
    return result


def is_valid_chain(chain):
    for i in range(1, len(chain)):
        if chain[i] - chain[i - 1] > 3:
            return False
    return True


def p2(data):
    # After failing to muddle through the hints here:
    # https://pietroppeter.github.io/adventofnim/2020/day10hints.html
    # I decided to just take his initial strategy of breaking our list into
    # sublists separated by untoggleable entries, and then recycle my old,
    # extremely inefficient method.
    def is_toggleable(i):
        try:
            return data[i + 1] - data[i - 1] <= 3
        except IndexError:
            # Last entry is not toggleable
            return False

    sublists = []
    sublist = [data[0]]
    for i in range(1, len(data)):
        sublist.append(data[i])
        if not is_toggleable(i):
            if len(sublist) > 2:
                sublists.append(sublist)
            sublist = [data[i]]
    result = 1
    for sublist in sublists:
        temp = p2_slow(sublist)
        print(f"sublist: {sublist}; p2_slow: {temp}")
        result *= temp
    return result


def p2_slow(data):
    """This method returns the correct answer for the test_inputs, but
    doesn't return (at least not after a few hours) on the real data set. Need
    a more efficient algorithm.
    """
    # This is a list of indices of our data that are eligible for removal bc
    # the items before and after are within 3.
    candidates_for_toggling = []
    # Iterate through the indices of the non-first/last items
    for i in range(1, len(data) - 1):
        if data[i + 1] - data[i - 1] <= 3:
            candidates_for_toggling.append(i)
    num_candidates = len(candidates_for_toggling)
    count = 0
    for i in range(2 ** num_candidates):
        mask = dec_to_mask(i, num_candidates)
        indices_to_remove = set(compress(candidates_for_toggling, mask))
        combination = [
            d for j, d in enumerate(data) if j not in indices_to_remove
            ]
        if is_valid_chain(combination):
            count += 1
    return count


def clean_up_input(data):
    data = [int(l) for l in data if l]
    data.sort()
    data.insert(0, 0)  # The plug
    data.append(max(data) + 3)  # The device
    return data


if __name__ == "__main__":
    with open("10-input.txt") as f:
        data = [l.strip() for l in f.readlines()]

    test_input1 = [int(l) for l in test_input1.split("\n") if l.strip()]
    test_input2 = [int(l) for l in test_input2.split("\n") if l.strip()]
    data = clean_up_input(data)
    test_input1 = clean_up_input(test_input1)
    test_input2 = clean_up_input(test_input2)
    assert(p1(test_input1) == 7 * 5)
    assert(p1(test_input2) == 22 * 10)
    print(p1(data))
    assert(p2(test_input1) == 8)
    assert(p2(test_input2) == 19208)
    print(p2(data))
