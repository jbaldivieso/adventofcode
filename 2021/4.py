from dataclasses import dataclass

from utils import parse_as_str


test_input = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


@dataclass
class Square(object):
    value: int
    selected: bool = False


class Board(object):
    grid = None

    def __init__(self, grid_input):
        self.grid = []
        for row in grid_input:
            # Appending entire rows of Squares at a time
            self.grid.append([Square(value=v) for v in row])

    def play(self, value):
        """For a given @value, mark our board."""
        # We're assuming that a value can appear more than once in our board.
        for row in self.grid:
            for square in row:
                if square.value == value:
                    square.selected = True

    @property
    def has_won(self):
        """Return True if this board has a winning row or col."""
        dim = len(self.grid)
        # By row
        for x in range(dim):
            if all([sq.selected for sq in self.grid[x]]):
                return True
        # By col
        for y in range(dim):
            if all([self.grid[x][y].selected for x in range(dim)]):
                return True
        return False

    def get_score(self, value):
        """Return the sum of the unselected grid values * value
        """
        some = sum([
            sq.value for row in self.grid for sq in row if not sq.selected
        ])
        print(some, value)
        return some * value


def parse_input(data):
    """Return (pot, boards)"""
    # Pot
    pot = data.pop(0)
    if not pot:
        pot = data.pop(0)
    pot = [int(v) for v in pot.split(",")]
    # Blank line is next
    boards = []
    this_grid = []
    for line in data:
        if line:
            this_grid.append([int(v) for v in line.split(" ") if v])
        elif this_grid:
            boards.append(Board(this_grid))
            this_grid = []
    return (pot, boards)


def p1(data):
    # Assumes data is just a list of strings
    pot, boards = parse_input(data)
    for value in pot:
        for board in boards:
            board.play(value)
            if board.has_won:
                return board.get_score(value)


def p2(data):
    # Assumes data is just a list of strings
    pot, boards = parse_input(data)
    for value in pot:
        to_remove = []
        for i, board in enumerate(boards):
            board.play(value)
            if board.has_won:
                if len(boards) == 1:
                    return board.get_score(value)
                to_remove.append(i)
        for i in reversed(to_remove):
            # Do it backwards so we don't screw up the accuracy of
            # higher-indexed items once we delete one of its predecessors.
            del boards[i]


if __name__ == "__main__":
    test_input = test_input.split("\n")
    real_input = parse_as_str("4-input.txt")
    assert(p1(test_input.copy()) == 4512)
    print(p1(real_input.copy()))
    assert(p2(test_input) == 1924)
    print(p2(real_input))
