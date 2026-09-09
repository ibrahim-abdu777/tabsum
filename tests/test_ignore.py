import unittest
from src.tabsum import summarize


class TestIgnore(unittest.TestCase):
    def test_non_numeric_ignored(self):
        self.assertEqual(summarize(["count=x bad", "plain"]), {})


if __name__ == "__main__":
    unittest.main()
