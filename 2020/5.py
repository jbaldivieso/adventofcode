test_input = [
    ("FBFBBFFRLR", 357),
    ("BFFFBBFRRR", 567),
    ("FFFBBBFRRR", 119),
    ("BBFFBBFRLL", 820),
    ]

# row 44,  column 5, seat ID 357.
# row 70,  column 7, seat ID 567.
# row 14,  column 7, seat ID 119.
# row 102, column 4, seat ID 820.


def process_char(char, window):
    """Given a character in {b, f, r, l}, return either the narrowed window it
    results in (2-tuple), or the value it specifies, if the window has fully
    closed.
    """
    # f & l: lower half of window; b & r: upper half
    start, end = window
    if end - start == 1:
        # final choice
        if char in {"F", "L"}:
            return start
        else:
            return end
    midpoint = (start + end) // 2
    if char in {"F", "L"}:
        window = (start, midpoint)
    else:
        window = (midpoint + 1, end)
    return window


def get_seat_id(bp, debug=False):
    row_data = bp[:7]
    col_data = bp[7:]
    row_window = (0, 127)
    col_window = (0, 7)
    for char in row_data:
        row_window = process_char(char, row_window)
        if debug:
            print(f"Char was: {char}.  New window: {row_window}")
    row = row_window
    for char in col_data:
        col_window = process_char(char, col_window)
    col = col_window
    result = row * 8 + col
    if debug:
        print(f"Input: {bp}, Result: {row}, {col}. Result: {result}.")
    return result


def p1(data):
    return max([get_seat_id(bp) for bp in data])


def p2(data):
    existing = [get_seat_id(bp) for bp in data]
    existing.sort()
    for i, bp in enumerate(existing):
        if existing[i + 1] - bp != 1:
            print(f"{bp}, {existing[i + 1]}")
            break


if __name__ == "__main__":
    for bp, seat_id in test_input:
        assert(get_seat_id(bp) == seat_id)
    with open("5-input.txt") as f:
        data = [l.strip() for l in f.readlines()]
    print(p1(data))
    p2(data)
