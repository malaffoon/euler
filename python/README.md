# Project Euler 

This project is me using Project Euler (https://projecteuler.net/) to learn Python.
* TODO - get Numba working with some of the utils modules
* TODO - use problem interface, clean up runner
* Started but not solved: 650
* 5% problems remaining: 719
* 10% problems remaining: 650, 710
* Prime Obsession: 103, 109, 113, 127, 131, 137, ...
    * 103, 105, 106 are closely related dealing with "special subset sums"

## Running

### Running - IDE

I run everything from the IDE (PyCharm or IntelliJ). The IDE adds paths to 
PYTHONPATH so we don't have to worry about that. But you may have to set the
working directory; particularly when running `EulerTestRunner` set the working
directory to the `problems` folder.

### Running - Command Line

Running from the command-line is a bit trickier (i despise Python's import scheme).
Setting PYTHONPATH explicitly works fine for tests and resource-free problems:
```bash
euler/python$ PYTHONPATH=. python tests/test_collatz.py
euler/python$ PYTHONPATH=. python problems/problem2.py
```
However, some tests load resources and they look for the resources files in 
`../../resources`. That means you *have* to run from the problems folder and 
set PYTHONPATH appropriately:
```bash
cd problems
euler/python/problems$ PYTHONPATH=.. python problem22.py
```

Of course, you should be using the test runner 'cause that times things for you.
Same general rules apply so the easiest way to do it is from problems package:
```bash
cd problems
euler/python/problems$ PYTHONPATH=.. python ../EulerTestRunner.py

# to run just a couple problems:
euler/python/problems$ PYTHONPATH=.. python ../EulerTestRunner.py 2 7
```

## Performance - Numba
Many of the solutions involve looping and some non-native math. As such they
can benefit GREATLY from Numba (https://numba.pydata.org/). Note that the test
runner doesn't warm up the methods, so the JIT compilation is included in the
performance numbers. Usually not a big deal.

As an example, i first used Numba for problem 686. Apart from using range() 
instead of count() i made no code changes. Before Numba it took almost 40s to
run the tests (three trivial tests and the final solution). With Numba, the
final solution took 240ms ... yes, 120x faster. 

Obviously you need Numba in the python environment, to install:
```
pip install numba
```
