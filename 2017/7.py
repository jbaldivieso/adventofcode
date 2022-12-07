from collections import Counter

"""
                gyxo
              /
         ugml - ebii
       /      \
      |         jptl
      |
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |
      |         ktlj
       \      /
         fwft - cntj
              \
                xhth
"""

with open("7-input.txt", "r") as f:
    raw_input_ = [line.strip() for line in f.readlines()]


def parse_input(line):
    parts = [w.strip() for w in line.split("->")]
    name, weight = parts[0].split("(")
    name = name.strip()
    weight = int(weight.replace(")", ""))
    if len(parts) > 1:
        children = [w.strip() for w in parts[1].split(",")]
    else:
        children = []
    return name, weight, children


test_input = [
    "pbga (66)",
    "xhth (57)",
    "ebii (61)",
    "havc (66)",
    "ktlj (57)",
    "fwft (72) -> ktlj, cntj, xhth",
    "qoyq (66)",
    "padx (45) -> pbga, havc, qoyq",
    "tknk (41) -> ugml, padx, fwft",
    "jptl (61)",
    "ugml (68) -> gyxo, ebii, jptl",
    "gyxo (61)",
    "cntj (57)",
    ]


class Node(object):

    parent = None  # another node
    children = None  # other nodes
    weight = None
    name = ""

    def __init__(self, name, weight=None):
        self.name = name
        self.weight = weight
        self.children = []

    def __repr__(self):
        s = "%s (%s)" % (self.name, self.weight)
        if self.children:
            children = [str(c) for c in self.children]
            s += "; children: [%s]" % (", ".join(children))
        return s

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def get_child_by_name(self, name):
        if self.name == name:
            return self
        else:
            for child in self.children:
                res = child.get_child_by_name(name)
                if res:
                    return res
        return None

    def fold(self, node):
        """Given a node, merge it into self and return it.
        """
        self.weight = node.weight
        return self

    @property
    def total_weight(self):
        return self.weight + sum([c.total_weight for c in self.children] or [0])

    def get_unbalanced_node(self):
        if self.children:
            total_weights = [n.total_weight for n in self.children]
            counter = Counter(total_weights)
            val, count = counter.most_common()[-1]
            if count == 1:  # i.e the least common had a single appearance
                for n in self.children:
                    if n.total_weight == val:
                        return n
        return None


def parse_nodes(lines):
    nodes_by_name = {}
    for line in lines:
        name, weight, children = parse_input(line)
        new_node = Node(name=name, weight=weight)
        # Check for:
        # 1. new node already referenced at top level of list or in children of
        #    existing nodes
        # 2. new node's children are pre-exisiting at top level of list; pull
        #    them in
        add_to_top = True
        for node in nodes_by_name.values():
            parent = node.get_child_by_name(new_node.name)
            if parent:
                new_node = parent.fold(new_node)
                add_to_top = False
                break

        if add_to_top:
            nodes_by_name[name] = new_node

        for name in children:
            # Case 2.
            if name in nodes_by_name:
                child = nodes_by_name.pop(name)
                new_node.add_child(child)
            else:
                new_node.add_child(Node(name=name))
    return nodes_by_name


nodes = parse_nodes(raw_input_)
# nodes = parse_nodes(test_input)

# Starting at the top, we know there's a bad node all the way down (well, "up"
# according to the way the puzzle describes it). Keep following the bad nodes
# until they seem clean, then we have the root of the problem.
bad = next(iter(nodes.values()))  # This is the top node
while True:
    next_ = bad.get_unbalanced_node()
    if not next_:
        # bad was the one!
        counter = Counter([c.total_weight for c in bad.parent.children])
        result = counter.most_common(1)[0][0]
        print(counter.most_common())
        print(result)
        print("(This isn't quite the answer; it's what the total_weight should end up being, but you need to subtract the sum of the children's total_weights first!)")
        break
    else:
        bad = next_
