import sys
import os.path as osp
import numpy as np
from copy import deepcopy
from argparse import ArgumentParser
# TODO: add logger


def read_list(path, ret_type, do_strip=False):
    with open(path, 'r') as f:
        data = f.readlines()
    if do_strip:
        return list(map(ret_type, map(lambda x: x.strip(), data)))
    else:
        return list(map(ret_type, data))


def day_0(task, file_name):
    return 'Be prepared! This time I feel, I am. :)'


def day_1(task, file_name):
    depth = read_list(file_name, int)

    if task == 1:
        depth_diff = np.diff(depth)
    else:
        arr = np.array(depth).cumsum()
        arr[3:] = arr[3:] - arr[:-3]
        depth_diff = np.diff(arr[2:])

    increasing_steps = sum(x > 0 for x in depth_diff)
    return increasing_steps


def day_2(task, file_name):

    def split_command(c):
        d, v = c.split()
        return d, int(v)

    commands = read_list(file_name, str, do_strip=True)
    commands = list(map(split_command, commands))

    is_aim = True if task == 2 else False

    pos = {'forward': 0, 'depth': 0}
    aim = 0

    for command in commands:
        if command[0] == 'forward':
            pos['forward'] += command[1]
            pos['depth'] += aim * command[1] if is_aim else 0
        elif command[0] == 'down':
            if is_aim:
                aim += command[1]
            else:
                pos['depth'] += command[1]
        elif command[0] == 'up':
            if is_aim:
                aim -= command[1]
            else:
                pos['depth'] -= command[1]
        else:
            print(f'Unknown command: {command[0]}')
            raise ValueError
    return pos['forward'] * pos['depth']


def day_3(task, file_name):

    def transpose_1d_array(np_array):
        np_array = np.array(list(map(list, np_array)))
        return np_array.transpose()

    def calculate_gamma(data):
        gamma = ''
        length = len(data[0])
        for element in data:
            if np.count_nonzero(element == '1') > length/2:
                gamma += '1'
            else:
                gamma += '0'
        return gamma

    def find_most_common(arr, i):
        counter = 0
        for num in arr:
            counter += num[i] == '1'
        return '1' if counter >= len(arr)/2 else '0'

    def find_least_common(arr, i):
        return '0' if find_most_common(arr, i) == '1' else '1'

    data = np.array(read_list(file_name, str, do_strip=True))
    if task == 1:
        data = transpose_1d_array(data)

        gamma = calculate_gamma(data)
        power = len(gamma)
        gamma = int(gamma, 2)
        epsilon = (2**power - 1) - gamma
        return gamma * epsilon

    else:
        oxygen = read_list(file_name, str, do_strip=True)
        co2 = read_list(file_name, str, do_strip=True)

        for index in range(len(data)):
            if len(oxygen) > 1:
                mc = find_most_common(oxygen, index)
                oxygen = list(filter(lambda x: x[index] == mc, oxygen))
            if len(co2) > 1:
                lc = find_least_common(co2, index)
                co2 = list(filter(lambda x: x[index] == lc, co2))
            if len(oxygen) == 1 and len(co2) == 1:
                break

        o_rating = int(oxygen[0], 2)
        co2_rating = int(co2[0], 2)
        return o_rating * co2_rating


def main(raw_args):
    print('Welcome to the Advent of Code in 2021')
    parser = ArgumentParser()
    parser.add_argument('-d', '--day', type=int, required=True, help='on the day you are trying to help Santa')
    parser.add_argument('-t', '--task', type=int, default=1, help='task of the day: 1 or 2')
    parser.add_argument('-f', '--file', type=str, help='input file name')
    args = parser.parse_args(raw_args)
    print(f'Day:{args.day:3}, Task:{args.task:2}')

    day_map = {
        0: day_0,
        1: day_1,
        2: day_2,
        3: day_3
    }
    input_dir = 'inputs'
    file_path = osp.join(input_dir, args.file if args.file else f'input_{args.day:02d}.txt')
    answer = day_map[args.day](args.task, file_path)
    print(answer)


if __name__ == '__main__':
    main(sys.argv[1:])
