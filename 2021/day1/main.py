import copy
import time
from numpy import loadtxt


def solution_1(data):
    count = 0
    prev = -1
    for x in data:
        if x > prev:
            count += 1
        prev = x
    return count - 1


def solution_2(data):
    count = 0
    prev_sum = -1
    for i in range(len(data)-2):
        sliding_sum = sum(data[i:i+3])
        if sliding_sum > prev_sum:
            count += 1
        prev_sum = sliding_sum
    return count - 1


def main():
    print("\n* Advent of Code 2021: Day 1 *\n")
    
    data = loadtxt('input.txt', dtype='int')

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