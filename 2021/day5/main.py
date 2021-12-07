import time
import itertools
from collections import Counter

def parse_input(input):

    vectors = []

    for line in input:
        vector = [ (int(x),int(y)) for (x,y) in tuple([ point.split(',') for point in line.split(' -> ') ])]
        vectors.append(vector)

    return vectors


def points_from_vector(vector, include_diag):

    ((x1,y1),(x2,y2)) = vector
    if x1 == x2:
        return [ (x1,y) for y in range( min(y1,y2), max(y1,y2)+1) ]
    elif y1 == y2:
        return [ (x,y1) for x in range( min(x1,x2), max(x1,x2)+1) ]
    elif include_diag:
        slope = round((y2 - y1) / (x2 - x1))
        y_intercept = y2 - slope * x2   # y = mx + b
        return [ (x, slope * x + y_intercept) for x in range(min(x1,x2), max(x1,x2)+1) ]
    else:
        return []


def calculate_intersection(vectors, include_diag=False):

    points = itertools.chain( *[points_from_vector(vector, include_diag) for vector in vectors] )
    intersection_count = len([ x for x in Counter(points).values() if x > 1])
    return intersection_count


def solution_1():

    with open('input.txt') as file:
        vectors = parse_input(file)
        return calculate_intersection(vectors)


def solution_2():

    with open('input.txt') as file:
        vectors = parse_input(file)
        return calculate_intersection(vectors, include_diag=True)


def main():

    print("\n* Advent of Code 2021: Day 5 *\n")

    tic = time.perf_counter()
    s1 = solution_1()
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2()
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")


if __name__ == '__main__':
    main()