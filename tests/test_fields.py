import unittest
from src.tabsum import summarize


class TestFields(unittest.TestCase):
    def test_sums_count_fields(self):
        self.assertEqual(summarize(["count=1 ok", "count=2 two", "count=1 again"]), {"1": 2, "2": 1})


if __name__ == "__main__":
    unittest.main()
