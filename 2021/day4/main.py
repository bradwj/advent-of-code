import time
import re
import numpy as np

def parse_input(file):

    nums = [int(n) for n in file.readline().split(',')]
    file.readline()

    boards = []
    board = []
    for line in file.readlines():
        if line == '\n':
            boards.append(board)
            board = []
        else:
            # each number has boolean value corresponding to if it has been marked
            row = [ [int(n), False] for n in line.split() ]
            board.append(row)

    return np.array(nums), np.array(boards)


def mark_board(board, num):

    for row in board:
        for col in row:
            if col[0] == num:
                col[1] = True
    

def check_for_bingo(board):

    bingo = False

    # check rows for bingo
    for row in board:
        if not bingo:
            bingo = all(value[1] for value in row)

    # check columns for bingo
    for col in range(len(board)):
        if not bingo:
            bingo = all(value[1] for value in board[:, col])
    
    return bingo


def calculate_score(board, num):
    unmarked_sum = 0
    for row in board:
        for col in row:
            if col[1] == False: # only sum numbers that are not marked
                unmarked_sum += col[0]

    return unmarked_sum * num


def solution_1():

    with open('input.txt') as file:
        nums, boards = parse_input(file)

        for num in nums:
            for board in boards:
                mark_board(board, num)
                bingo = check_for_bingo(board)
                if bingo: 
                    return calculate_score(board, num)


def solution_2():
    pass


def main():

    print("\n* Advent of Code 2021: Day 3 *\n")

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