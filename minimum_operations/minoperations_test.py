import unittest

minOperations = __import__('0-minoperations').minOperations


class TestMinOperations(unittest.TestCase):
    def test_simple_examples(self):
        self.assertEqual(minOperations(2), 2)
        self.assertEqual(minOperations(4), 4)
        self.assertEqual(minOperations(6), 5)
        self.assertEqual(minOperations(9), 6)
        self.assertEqual(minOperations(18), 8)

    def test_prime_number(self):
        self.assertEqual(minOperations(3), 3)
        self.assertEqual(minOperations(7), 7)
        self.assertEqual(minOperations(13), 13)
        self.assertEqual(minOperations(29), 29)
        self.assertEqual(minOperations(97), 97)


if __name__ == "__main__":
    unittest.main()
