from utils.input import read_input

unsafe = "Unsafe"
safe = "Safe"

def solve_part1(data):
    safe_count = 0
    for i in data:
        arr = i.split(" ")
        curr = int(arr[0])
        is_going_up = (int(arr[0]) - int(arr[1])) < 0
        
        for j in range(1, len(arr)):
            newVal = int(arr[j])
            res = curr - newVal
            abs_res = abs(res)
            
            if is_going_up and res > 0:
                break
            elif not is_going_up and res < 0:                
                break

            if abs_res > 3:                
                break

            if abs_res < 1:
                break
            
            if j == len(arr) - 1:
                safe_count += 1
                break
            curr = newVal
    
    return safe_count

def solve_part2(data):
    safe_count = 0
    for i in data:
        arr = i.split(" ")
        curr = int(arr[0])
        is_going_up = (int(arr[0]) - int(arr[1])) < 0
        unsafe_count = 0
        for j in range(1, len(arr)):
            newVal = int(arr[j])
            res = curr - newVal
            abs_res = abs(res)
            
            if is_going_up and res > 0:
                unsafe_count += 1
            elif not is_going_up and res < 0:                
                unsafe_count += 1

            if abs_res > 3:                
                unsafe_count += 1

            if abs_res < 1:
                unsafe_count += 1
            if unsafe_count > 1:
                break
            
            if j == len(arr) - 1:
                safe_count += 1
                break
            curr = newVal
    
    return safe_count

if __name__ == "__main__":
    data = read_input(day=2, year=2024)
    print(f"Part 1: {solve_part1(data)}")
    print(f"Part 2: {solve_part2(data)}")
