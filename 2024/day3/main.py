from utils.input import read_input
from utils.benchmark import benchmark
import re

def parse_data_to_string(data):
    return "".join(data)

# first tried it with a stack which works, but then part 2 was too complicated to use this
# so opted for regex instead

# nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# def perform_operation(stack) -> int:
#     slice = stack[4:-1]
#     operands = ("").join(slice).split(",")
#     if (len(operands[0]) > 3 or len(operands[1]) > 3):
#         return 0

#     return int(operands[0]) * int(operands[1])

# def solve_part1(data):
#     str = parse_data_to_string(data)
#     res = 0
#     stack = []

#     for c in str:
#         if (c == "m" and len(stack) == 0):
#             stack.append(c)
#         elif (c == "u" and len(stack) > 0 and stack[-1] == "m"):
#             stack.append(c)
#         elif (c == "l" and len(stack) > 0 and stack[-1] == "u"):
#             stack.append(c)
#         elif (c == "(" and len(stack) > 0 and stack[-1] == "l"):
#             stack.append(c)
#         elif (c in nums and len(stack) > 0 and (stack[-1] == "(" or stack[-1] in nums)):
#             stack.append(c)
#         elif (c == "," and len(stack) > 0 and stack[-1] in nums):
#             stack.append(c)
#         elif (c in nums and len(stack) > 0 and stack[-1] == ","):
#             stack.append(c)
#         elif (c == ")" and len(stack) > 0 and stack[-1] in nums):
#             stack.append(c)
#             res += perform_operation(stack)
#             stack = []
#         else:
#             stack = []
        
#     return res

# with regex
def value_from_corrupt_data(str) -> int:
    res = 0
    matches = re.findall(r"mul\((\d+),(\d+)\)", str)
    for match in matches:
        res += int(match[0]) * int(match[1])
    return res


def solve_part1(data):
    str = parse_data_to_string(data)

    return value_from_corrupt_data(str)



def solve_part2(data):
    str = parse_data_to_string(data)

    # find indexes of all do() and don't() calls
    do_indexes = [m.end() for m in re.finditer(r"do\(", str)]
    dont_indexes = [m.end() for m in re.finditer(r"don't\(", str)]

    # find the searchable indexes between do() and don't()
    searchable_mul_indexes = []
    do = True
    for i in range(len(str)):
        if (i in dont_indexes or i in do_indexes):
            if (i in dont_indexes):
                do = False
            if (i in do_indexes):
                do = True
        else:
            if (do):
                searchable_mul_indexes.append(i)
    
    # split string into substrings based on searchable_mul_indexes
    substrings = []
    start = 0
    for i in searchable_mul_indexes:
        s = str[start:i]
        start = i
        if (len(s) == 1):
            substrings.append(s)
            continue
    searchable_str = "".join(substrings)

    return value_from_corrupt_data(searchable_str)

if __name__ == "__main__":
    data = read_input(day=3, year=2024)
    print(f"Part 1: {solve_part1(data)}")
    benchmark(func=solve_part1, data=data)
    print(f"Part 2: {solve_part2(data)}")
    benchmark(func=solve_part2, data=data)
