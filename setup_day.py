import os
from argparse import ArgumentParser

def scaffold_day(day: int, year: int):
    """
    Scaffold a new day folder with necessary files.
    """
    day_str = f"day{str(day)}"
    day_path = os.path.join(str(year), day_str)

    # Create the day folder
    os.makedirs(day_path, exist_ok=True)

    # Create main.py
    main_file = os.path.join(day_path, "main.py")
    if not os.path.exists(main_file):
        with open(main_file, "w") as f:
            f.write(f"""\
from utils.input import read_input

def solve_part1(data):
    return "Not implemented"

def solve_part2(data):
    return "Not implemented"

if __name__ == "__main__":
    data = read_input(day={day}, year={year})
    print(f"Part 1: {{solve_part1(data)}}")
    print(f"Part 2: {{solve_part2(data)}}")
""")
    
    # Create input.txt and example.txt
    for filename in ["input.txt", "example.txt"]:
        file_path = os.path.join(day_path, filename)
        if not os.path.exists(file_path):
            open(file_path, "w").close()

    print(f"Scaffolded {day_str} for {year}")

if __name__ == "__main__":
    parser = ArgumentParser(description="Scaffold a new Advent of Code day")
    parser.add_argument("--day", type=int, required=True, help="The day number (e.g., 1 for day01)")
    parser.add_argument("--year", type=int, required=True, help="The year (e.g., 2024)")
    args = parser.parse_args()

    scaffold_day(day=args.day, year=args.year)
