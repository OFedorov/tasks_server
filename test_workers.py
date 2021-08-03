import unittest

from workers import revers, permutation, echo


class WorkersTestCase(unittest.TestCase):
    def test_revers(self):
        self.assertEqual(revers("hello"), "olleh")
        self.assertEqual(revers(""), "")

    def test_permutation(self):
        self.assertEqual(permutation("hello"), "ehllo")
        self.assertEqual(permutation("qwerty"), "wqreyt")
        self.assertEqual(permutation(""), "")
        self.assertEqual(permutation("h"), "h")
        self.assertEqual(permutation("he"), "eh")

    def test_echo(self):
        self.assertEqual(echo("hello"), "hello")
        self.assertEqual(echo(""), "")


if __name__ == '__main__':
    unittest.main()
