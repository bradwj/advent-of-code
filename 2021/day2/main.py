import time

def solution_1(data):
    horizontal_pos = 0
    depth = 0
    for instruction in data:
        instruction = instruction.split(' ')
        direction = instruction[0]
        amount = int(instruction[1])

        if direction == "forward":
            horizontal_pos += amount
        if direction == "up":
            depth -= amount
        if direction == "down":
            depth += amount
        
    return horizontal_pos * depth


def solution_2(data):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for instruction in data:
        instruction = instruction.split(' ')
        direction = instruction[0]
        amount = int(instruction[1])

        if direction == "forward":
            horizontal_pos += amount
            depth += amount * aim
        if direction == "up":
            aim -= amount
        if direction == "down":
            aim += amount
        
    return horizontal_pos * depth


def main():
    print("\n* Advent of Code 2021: Day 2 *\n")
    
    with open("input.txt") as f:

        data = f.readlines()

        tic = time.perf_counter()
        s1 = solution_1(data)
        toc = time.perf_counter()
        print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

        tic = time.perf_counter()
        s2 = solution_2(data)
        toc = time.perf_counter()
        print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")


if __name__ == '__main__':
    main()