test_input = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


class InfiniteLoop(Exception):
    """Not related to Apple Inc HQ"""


def parse_instructions(data):
    lines = [line for line in data.split("\n") if line]
    instructions = [line.split() for line in lines]
    return [(op, int(amt)) for op, amt in instructions]


def parse_instruction(instructions, inst):
    """Return a tuple of (amount to increment, next instruction index)."""
    instruction = instructions[inst]
    if instruction[0] == "nop":
        return (0, inst + 1)
    if instruction[0] == "acc":
        return (instruction[1], inst + 1)
    # jmp
    return (0, inst + instruction[1])


def p1(data):
    instructions = parse_instructions(data)
    seen = set()  # Indexes we've seen already
    acc = 0  # Counter
    next_inst = 0  # Pointer to index of current instruction
    while True:
        inc, next_inst = parse_instruction(instructions, next_inst)
        if next_inst in seen:
            return acc
        seen.add(next_inst)
        acc += inc


def test_variation(instructions):
    seen = set()  # Indexes we've seen already
    acc = 0  # Counter
    next_inst = 0  # Pointer to index of current instruction
    while True:
        inc, next_inst = parse_instruction(instructions, next_inst)
        if next_inst in seen:
            raise InfiniteLoop()
        seen.add(next_inst)
        acc += inc
        if next_inst == len(instructions):
            return acc


def get_instructions_permutations(instructions):
    for i in range(len(instructions)):
        if instructions[i][0] == "jmp":
            result = instructions.copy()
            result[i] = ("nop", result[i][1])
            yield result
        elif instructions[i][0] == "nop":
            result = instructions.copy()
            result[i] = ("jmp", result[i][1])
            yield result


def p2(data):
    instructions = parse_instructions(data)
    for permutation in get_instructions_permutations(instructions):
        try:
            return test_variation(permutation)
        except InfiniteLoop:
            continue


if __name__ == "__main__":
    with open("8-input.txt") as f:
        data = f.read()
    assert(p1(test_input) == 5)
    print(p1(data))
    assert(p2(test_input) == 8)
    print(p2(data))
