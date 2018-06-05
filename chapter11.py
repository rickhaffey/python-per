# # Chapter 11 - Testing, Debugging, Profiling, and Tuning

# ## Documentation Strings and the `doctest` Module

# - if first line of function, class, or module is a string => documentation string
# - often include short examples
# - `doctest` executes examples in docstrings as tests

import doctestdemo
import doctest

nfail, ntests = doctest.testmod(doctestdemo) #, verbose=True)
print("tests: {}".format(ntests))
print("failures: {}".format(nfail))


# >>> **********************************************************************
# >>> File "/Users/rhaffey/Learn/python-learn/python-per/doctestdemo.py", line 15, in doctestdemo.method2
# >>> Failed example:
# >>>     method2()
# >>> Expected:
# >>>     'something interesting'
# >>> Got:
# >>>     'something less interesting'
# >>> **********************************************************************
# >>> 1 items had failures:
# >>>    1 of   1 in doctestdemo.method2
# >>> ***Test Failed*** 1 failures.
# >>> tests: 2
# >>> failures: 1


# for running tests from _within_ a module, the following could be used
if __name__ == '__main__':
    import doctest
    nfail, ntest = doctest.testmod()
    # ...

# - doctest expects output of test to match _exactly_ to that shown in example
# - can be problematic wrt whitespace, rounding, etc.

# - use `doctest` for _primary_ examples
# - use `unittest` for comprehensive testing (corner cases, edge cases, etc.)

# ## Unit Testing and the `unittest` Module

import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def setUp(self):
        # perform any setup
        pass

    def tearDown(self):
        # perform any tear down
        pass

    def testBasic(self):
        r = add(2, 3)
        self.assertEqual(r, 5)

    def testNegative(self):
        r = add(-1, -3)
        self.assertEqual(r, -4)

    # etc...

if __name__ == '__main__':
    unittest.main()
    
# - class inherits from `unittest.TestCase`    
# - test methods named starting with `test`
# - `setUp`: run before _each_ test method
# - `tearDown`: run after _each_ test method
# - `assert`: fails test if expr evaluates to False
# - `assertEqual`: fails test if x <> y
# - `assertNotEqual`: fails test if x == y
# - `assertAlmostEqual`: fails test if x <> y within some tolerance
# - `assertNotAlmostEqual`: fails test if x == y within some tolerance
# - `assertRaises`: fails test if exception isn't raised
# - `fail`: fails always
# - `failIf`: fails if condition holds
# - `failureException`: set to the last exception raised in a test

# RESUME @ ## The Python Debugger and `pdb` Module

        

    
