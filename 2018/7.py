import re

from utils import parse_as_str


def parse_input(raw):
    pattern = re.compile(r"Step (\w) must be finished before step (\w) can")
    return [pattern.match(s).groups() for s in raw]


class Node(object):
    def __init__(self, name):
        self.name = name
        # "dependencies" can be thought of as "parents"
        self.dependencies = []
        self.children = []

    def __repr__(self):
        return "{name} (Parents: {parents}; Children: {children})".format(
            name=self.name,
            parents=", ".join([d.name for d in self.dependencies]),
            children=", ".join([d.name for d in self.children]),
            )


test_input = [
    "Step C must be finished before step A can begin.",
    "Step C must be finished before step F can begin.",
    "Step A must be finished before step B can begin.",
    "Step A must be finished before step D can begin.",
    "Step B must be finished before step E can begin.",
    "Step D must be finished before step E can begin.",
    "Step F must be finished before step E can begin.",
    ]
test_input = parse_input(test_input)
data = parse_input(parse_as_str("7-input.txt"))


def parse_nodes(data):
    # Create tree
    nodes = {}  # For easy look ups
    for pair in data:
        for letter in pair:
            if letter not in nodes:
                nodes[letter] = Node(letter)
        parent = nodes[pair[0]]
        child = nodes[pair[1]]
        child.dependencies.append(parent)
        parent.children.append(child)
    return nodes


def part1(data):
    nodes = parse_nodes(data)
    # Iterate over tree, creating a queue (sorted alphabetically) and
    # the result string.
    results = ""
    finished = set()  # letters for "completed" nodes
    queue = [n for n in nodes.values() if not n.dependencies]
    while nodes:
        # Which is next?
        queue.sort(key=lambda n: n.name)
        current = None  # Just to indicate if next loop fails.
        for i in range(len(queue)):
            if all([d.name in finished for d in queue[i].dependencies]):
                current = queue.pop(i)
                break

        results += current.name
        finished.add(current.name)
        queue.extend([n for n in current.children if n not in queue])
        del nodes[current.name]
    return results


assert part1(test_input) == "CABDFE"
print("Done with part2 part 1 tests!")
print(f"Part 1 result: {part1(data)}")


def part2(data, num_workers, goose=0):
    # Model the workers as a list of tuples: node in process, and count of
    # remaining work. None instead of a tuple means the worker is idle
    workers = [None for n in num_workers]
    nodes = parse_nodes(data)
    timer = 0
    lengths = {
        letter: i + goose + 1 for i, letter in enumerate(string.ascii_uppercase)
        }
    while nodes:
        # Deduct the workers' times; mark finished as appropriate
        for i in range(len(workers)):
            if worker[i]:
                node, timer = worker[i]
                timer -=1
                if timer:
                    worker[i] = (node, timer)
                else:
                    worker[i] = None
                    finished.add(node.name)
                    queue.extend([n for n in node.children if n not in queue])
                    del nodes[node.name]

        # Farm out the queue
        queue.sort(key=lambda n: n.name)
        for i in range(len(queue)):
            if all([d.name in finished for d in queue[i].dependencies]):
                if None in workers:
                    current = queue.pop(i)
                    
                else:
                    break

        timer += 1
    return timer


assert part2(test_input, 2) == 15
print("Done with part2 part 1 tests!")
print(f"Part 2 result: {part2(data, 5, 60)}")
