import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def setUp(self):
        # perform any setup
        print('setup')

    def tearDown(self):
        # perform any tear down
        print('tearDown')

    def testBasic(self):
        r = add(2, 3)
        self.assertEqual(r, 5)

    def testNegative(self):
        r = add(-1, -3)
        self.assertEqual(r, -4)

    # etc...

if __name__ == '__main__':
    unittest.main()

