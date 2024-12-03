from utils.input import read_input
from utils.benchmark import benchmark

def format_data_into_lists(data):
    list1 = []
    list2 = []

    for i in data:
        s = i.split("   ")
        t = s[0]
        u = s[1]
        list1.append(int(t))
        list2.append(int(u))

    return list1, list2

def solve_part1(data):
    list1, list2 = format_data_into_lists(data)

    list1.sort()
    list2.sort()

    res = []

    for i in range(len(list1)):
        r = abs(list1[i] - list2[i])
        res.append(r)
        
    return sum(res)

def solve_part2(data):
    list1, list2 = format_data_into_lists(data)
    list2_dict = { i: list2.count(i) for i in list2 }

    similarity_score = 0

    for i in list1:
        exists = list2_dict.get(i)
        if exists:
            similarity_score += i * exists


    return similarity_score

if __name__ == "__main__":
    data = read_input(day=1, year=2024)
    print(f"Part 1: {solve_part1(data)}")
    print(f"Part 2: {solve_part2(data)}")
    benchmark(func=solve_part1, data=data)
    benchmark(func=solve_part2, data=data)
