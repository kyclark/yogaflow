# Yoga Flow

Use [Markov chain](https://en.wikipedia.org/wiki/Markov_chain) to create yoga sequences.
The "inputs" directory contains 20 yoga sequences which are read as the training files:

```
$ ./yogaflow.py -h
usage: yogaflow.py [-h] [-m int] [-s int] FILE [FILE ...]

Markov chain to create yoga sequence

positional arguments:
  FILE                  Input file(s)

optional arguments:
  -h, --help            show this help message and exit
  -m int, --max_poses int
                        Maximum number of poses (default: 5)
  -s int, --seed int    Random seed value (default: None)
```

The program will generate a new sequence by randomly choosing a pose and then using Markov chains to select the next move up to a `--max_poses` value (or sooner if a chosen pose creates a deadend).

```
$ ./yogaflow.py inputs/*
Side Reclining Leg Lift
Snake
Locust
Downward Facing Dog
Warrior I
Reverse Warrior
```

Given that the program uses random selections, a `--seed` value can be used to reproduce output and test:

```
$ ./yogaflow.py inputs/* -s 1
Locust
Downward Facing Dog
Warrior I
Reverse Warrior
Extended Triangle
Intense Leg Stretch
```

To test:

```
$ pytest -xv test.py unit.py
============================= test session starts ==============================
...

test.py::test_exists PASSED                                              [ 11%]
test.py::test_usage PASSED                                               [ 22%]
test.py::test_bad_file PASSED                                            [ 33%]
test.py::test_bad_seed PASSED                                            [ 44%]
test.py::test_bad_max_poses PASSED                                       [ 55%]
test.py::test_01 PASSED                                                  [ 66%]
test.py::test_02 PASSED                                                  [ 77%]
unit.py::test_pairs PASSED                                               [ 88%]
unit.py::test_read_training PASSED                                       [100%]

============================== 9 passed in 0.38s ===============================
```

The source code uses many annotations from the `typing` module to assist in program verification with tools like `mypy`.
I also include both unit tests (in `unit.py`) and an integration test (in `test.py`).

# Author

Ken Youens-Clark <kyclark@gmail.com>
