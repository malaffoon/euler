"""Utility for running Euler problems.

A testable problem class shall have two methods:
  | solve(args) - returns a single value, accepts zero or one args
  | get_tests() = returns [(args, expected), ...]
get_tests() should return the problem/solution first, then any examples or extra tests.

Note that a solver that requires multiple arguments cannot be run. The problem solution
can be tested in that case by having default argument values and returning [(None, expected)]
from get_tests().

Note that problems that have external resource files may have some issues.

TODO - parsing of args is rolled into runner and shouldn't be.
"""
import glob
import importlib
import os
import sys
import time


class EulerTimer(object):
    def __init__(self):
        pass

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.perf_counter()
        self.secs = self.stop - self.start

    def __str__(self):
        """Return human-readable elapsed time"""
        return '%f ms' % (1000*self.secs) if self.secs < 1 else '%f secs' % self.secs


class EulerTestRunner(object):
    def __init__(self, argv):
        if len(argv) == 1 or (len(argv) == 2 and argv[1] == '*'):
            self.run_extra_tests = len(argv) == 2
            self.testables = self._discoverAllTestables()
        else:
            self.run_extra_tests = True
            self.testables = self._discoverTestables(argv[1:])

    def run(self):
        failures = 0
        for testable in self.testables:
            failures += self.runTestable(testable())
        if failures and len(self.testables) > 1:
            print("There were FAILURES")

    def runTestable(self, testable):
        """Run a single testable object, emitting results"""
        tests = testable.get_tests()
        if len(tests) == 0:
            print('%s - no tests' % testable.__class__.__name__)
            return 0

        output = ['%s' % (testable.__class__.__name__,)]
        failures = 0
        for test in tests:
            with EulerTimer() as t:
                actual = testable.solve(test[0]) if test[0] else testable.solve()

            if actual == test[1]:
                output.append(' Success in %s: %s = solve(%s)' % (str(t), test[1], test[0] if test[0] else ''))
            else:
                failures += 1
                output.append(' FAILURE: solve(%s) = %s, expected: %s' % (test[0] if test[0] else '', actual, test[1]))

            if not self.run_extra_tests: break
        print('\n'.join(output) if self.run_extra_tests else ' - '.join(output))
        return failures

    def _loadTestablesFromModule(self, module):
        testables = []
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and hasattr(obj, 'solve') and hasattr(obj, 'get_tests'):
                testables.append(obj)
        return testables

    def _discoverTestables(self, modules):
        testables = []
        importlib.import_module('problems', __name__)
        for submodule in modules:
            if submodule.isdigit(): submodule = 'problem'+submodule
            if not submodule.startswith('.'): submodule = '.' + submodule
            module = importlib.import_module(submodule, 'problems')
            testables.extend(self._loadTestablesFromModule(module))
        return testables

    def _discoverAllTestables(self):
        testables = []
        problem_module = importlib.import_module('problems', __name__)
        problem_submodules = list(os.path.basename(filename)[:-3] for filename in glob.glob(problem_module.__path__[0] + '/problem*.py'))
        problem_submodules.sort(key=lambda n: int(n[7:]))
        for submodule in problem_submodules:
            module = importlib.import_module('.'+submodule, 'problems')
            testables.extend(self._loadTestablesFromModule(module))
        return testables


if __name__ == '__main__':
    EulerTestRunner(sys.argv).run()
