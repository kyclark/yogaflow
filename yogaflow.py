#!/usr/bin/env python3
""" Markov chain to create yoga sequence """

import argparse
import random
from collections import defaultdict
from typing import Any, NamedTuple, List, TextIO, Dict, Tuple, TypeVar


class Args(NamedTuple):
    file: List[TextIO]
    max_poses: int
    seed: int


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Markov chain to create yoga sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-m',
                        '--max_poses',
                        help='Maximum number of poses',
                        metavar='int',
                        type=int,
                        default=5)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.max_poses < 1:
        parser.error(f'--max_poses "{args.max_poses}" must be > 0')

    return Args(args.file, args.max_poses, args.seed)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    random.seed(args.seed)
    poses = read_training(args.file)
    seq = [random.choice(list(poses.keys()))]

    # We may not get to the max if we run out of options
    for _ in range(args.max_poses):
        prev = seq[-1]

        # There may not be any poses following this one
        if choices := poses.get(prev):
            pose = random.choice(choices)

            # Don't get stuck in an infinite loop w/same pose
            if pose != prev:
                seq.append(pose)
            else:
                break
        else:
            break

    print('\n'.join(seq))


# --------------------------------------------------
def read_training(fhs: List[TextIO]) -> Dict[str, List[str]]:
    """ Read training files, return dict of pose chains """

    poses = defaultdict(list)
    for fh in fhs:
        lines = list(map(str.rstrip, fh.readlines()))
        for p1, p2 in pairs(lines):
            poses[p1].append(p2)

    return poses


# --------------------------------------------------
def pairs(xs: List[Any]) -> List[Tuple[(Any, Any)]]:
    """ Create a list of pair/tuples from a list """

    return [(xs[i], xs[i + 1]) for i in range(0, len(xs) - 1)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
