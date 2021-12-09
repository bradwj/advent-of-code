import time

# the naive approach...
def solution_1(days):

    with open('ex_input.txt') as file:

        fish_list = [ int(n) for n in file.readline().split(',') ]

        for day in range(1,days+1):
            for i in range(len(fish_list)):
                if fish_list[i] == 0:
                    fish_list[i] = 6
                    fish_list.append(8)
                else:
                    fish_list[i] -= 1
        
        return len(fish_list)
    

def solution_2(days):

        data = [open('input.txt').read().count(str(i)) for i in range(0, 9)]

        for day in range(days):
            data[(day + 7) % 9] += data[day % 9]
        
        return sum(data)


def main():

    print("\n* Advent of Code 2021: Day 6 *\n")

    tic = time.perf_counter()
    s1 = solution_1(days=80)
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1}, acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(days=256)
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2}, acquired in: {toc-tic:0.4f} seconds")


if __name__ == '__main__':
    main()