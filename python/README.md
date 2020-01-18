# Project Euler 

This project is me using Project Euler (https://projecteuler.net/) to learn Python.
* Start but not solved: 100, 493
* 10% problems remaining: 493, 650


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
