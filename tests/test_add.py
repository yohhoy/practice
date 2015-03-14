from add import add
import unittest

class AddTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)


if __name__ == '__main__':
    unittest.main()

