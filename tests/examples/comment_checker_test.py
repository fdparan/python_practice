import unittest

from examples import comment_checker


class MyTestCase(unittest.TestCase):

    def test_get_comment_returns_list_when_given_comment(self):

        sample = ["# a comment we'll get", "x = 3", "print x"]

        self.assertEqual(["# a comment we'll get"], comment_checker.get_comment(sample))
        self.assertEqual(2, len(comment_checker.get_comment(sample + ["# another comment"])))


if __name__ == '__main__':
    unittest.main()