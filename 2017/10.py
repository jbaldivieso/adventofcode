input_ = [
    130, 126, 1, 11, 140, 2, 255, 207, 18, 254, 246, 164, 29, 104, 0, 224
    ]


def part1():

    def process1(list_size, lengths):
        """This seems to work for the test input but doesn't deliver the
        correct answer; not sure why.
        """
        l = list(range(list_size))
        start = 0
        for skip, length in enumerate(lengths):
            if length:
                # Four cases:
                #    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                # 1. [                 ][--twist--]
                # 2. [--twist--][                 ]
                # 3.      ][---twist--][
                # 4. ------][          ][---twist-
                # if start == 0:
                #     # Case 1
                #     twist = l[:length]
                #     remainder = l[length:]
                #     twist.reverse()
                #     l = twist + remainder
                # elif start + length == list_size:
                #     # Case 2 (similar to above)
                #     print("2")
                #     twist = l[start:]
                #     remainder = l[:start]
                #     twist.reverse()
                #     l = remainder + twist
                if start + length <= list_size:
                    # Cases 1 & 2 & 3
                    pre = l[:start]
                    twist = l[start:start+length]
                    post = l[start+length:]
                    twist.reverse()
                    l = pre + twist + post
                else:
                    # Case 4
                    r0 = length + start - list_size  # remainder start
                    r1 = start
                    twist = l[r1:] + l[:r0]
                    remainder = l[r0:r1]
                    twist.reverse()
                    twist_breakpoint = list_size - start
                    l = twist[twist_breakpoint:] + remainder + twist[:twist_breakpoint]
            # Prepare for next round
            start = (start + length + skip) % list_size
        return l[0] * l[1]

    def process2(list_size, lengths):
        """This is pirated from a subreddit user's algorithm"""
        l = list(range(list_size))
        start = 0
        for skip, length in enumerate(lengths):
            sublist = []
            for i in range(start, start+length):
                index = i
                if index >= list_size:
                    index -= list_size
                sublist.append(l[index])
            sublist.reverse()
            for i in range(start, start+length):
                index = i
                if index >= list_size:
                    index -= list_size
                l[index] = sublist.pop(0)
            # Prepare for next round
            start = (start + length + skip) % list_size
        return l[0] * l[1]

    print("Test: expecting 12, got %s" % process2(5, [3, 4, 1, 5]))
    print("Solution: %s" % process2(255, input_))


part1()
