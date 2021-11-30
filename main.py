import sys
from argparse import ArgumentParser


def day_0(task, file_name):
    print('Be prepared! This time I feel, I am. :)')


def main(raw_args):
    print('Welcome to the Advent of Code in 2021')
    parser = ArgumentParser()
    parser.add_argument('-d', '--day', type=int, required=True, help='on the day you are trying to help Santa')
    parser.add_argument('-t', '--task', type=int, default=1, help='task of the day: 1 or 2')
    parser.add_argument('-f', '--file', type=str, help='input file name')
    args = parser.parse_args(raw_args)
    print(f'Day:{args.day:3}, Task:{args.task:2}')

    day_map = {
        0: day_0
    }

    day_map[args.day](args.task, args.file)


if __name__ == '__main__':
    main(sys.argv[1:])
