import os

def read_input(filename="input.txt", day=None, year=None):
    """
    Read the input file for a given day and year.
    """
    if day and year:
        path = f"{year}/day{str(day)}/{filename}"
    else:
        path = filename

    if not os.path.exists(path):
        raise FileNotFoundError(f"Input file not found: {path}")
    
    with open(path, "r") as file:
        return file.read().strip().splitlines()
