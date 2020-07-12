#!/usr/bin/env python3
""" tests for flow.py """

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './yogaflow.py'


# --------------------------------------------------
def test_exists():
    """ exists """

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """ usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file():
    """ bad file """

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_seed():
    """ not int for seed """

    bad = random_string()
    opt = random.choice(['-s', '--seed'])
    rv, out = getstatusoutput(f'{prg} {opt} {bad} ./inputs/*')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_max_poses():
    """ negative value for max_poses """

    bad = random.choice(range(-10, 0))
    opt = random.choice(['-m', '--max_poses'])
    rv, out = getstatusoutput(f'{prg} {opt} {bad} ./inputs/*')
    assert rv != 0
    assert re.search(f'--max_poses "{bad}" must be > 0', out)


# --------------------------------------------------
def test_01():
    """ works """

    rv, out = getstatusoutput(f'{prg} -s 1 inputs/*')
    assert rv == 0
    expected = [
        'Locust', 'Downward Facing Dog', 'Warrior I', 'Reverse Warrior',
        'Extended Triangle', 'Intense Leg Stretch'
    ]
    assert out.strip() == '\n'.join(expected)


# --------------------------------------------------
def test_02():
    """ works """

    rv, out = getstatusoutput(f'{prg} --seed 2 inputs/*')
    assert rv == 0
    expected = [
        'Bowing Yoga Mudra', 'Twisted', 'Bound Angle Forward Bend',
        'Seated Forward Bend', 'Twisted', 'Rabbit'
    ]
    assert out.strip() == '\n'.join(expected)


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
