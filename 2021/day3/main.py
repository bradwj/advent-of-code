import time
from numpy import loadtxt

def get_bit_freq(data):
    # each key in the map corresponds to a 2-value array. 
    # Index 0 correspondes to count of 0s, Index 1 corresponds to count of 1s.

    bit_freq_map = dict()
    # get frequency of each character in data
    for num in data:
        for digit,bit in enumerate(num):
            if digit in bit_freq_map:
                if bit == '0':
                    # increment count of 0s 
                    bit_freq_map[digit] = [ bit_freq_map[digit][0] + 1, bit_freq_map[digit][1] ]
                else:
                    # increment count of 1s
                    bit_freq_map[digit] = [ bit_freq_map[digit][0], bit_freq_map[digit][1] + 1 ]
            else:
                bit_freq_map[digit] = [0, 0]
    
    return bit_freq_map



def get_oxygen_generator_rating(data):
    data_list = data.tolist()
    i = 0
    while len(data_list) > 1:
        common_bit = ''
        count_0 = 0
        count_1 = 0
        for num in data_list:
            if num[i] == '0': 
                count_0 += 1
            else: 
                count_1 += 1
        
        if count_1 >= count_0:
            common_bit = '1'
        else:
            common_bit = '0'
        
        for num in data_list[:]:
            if num[i] != common_bit:
                data_list.remove(num)
        
        i += 1

    return int(data_list[0],2)


def get_co2_generator_rating(data):
    data_list = data.tolist()
    i = 0
    while len(data_list) > 1:
        common_bit = ''
        count_0 = 0
        count_1 = 0
        for num in data_list:
            if num[i] == '0': 
                count_0 += 1
            else: 
                count_1 += 1
        
        if count_0 <= count_1:
            common_bit = '0'
        else:
            common_bit = '1'
        
        for num in data_list[:]:
            if num[i] != common_bit:
                data_list.remove(num)
        
        i += 1

    return int(data_list[0],2)


def solution_1(data):
    bit_freq_map = get_bit_freq(data)
    
    gamma = ''
    epsilon = ''

    for freq in bit_freq_map.values():
        if freq[0] > freq[1]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def solution_2(data):

    return get_oxygen_generator_rating(data) * get_co2_generator_rating(data)


def main():
    print("\n* Advent of Code 2021: Day 3 *\n")

    data = loadtxt('input.txt', dtype='str')

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