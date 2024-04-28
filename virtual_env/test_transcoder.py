import unittest
from transcoder import generate_random_string

class TestGenerateRandomString(unittest.TestCase):
    def test_generate_random_string(self):
        # Test with length 5
        result = generate_random_string(5)
        self.assertEqual(len(result), 5)

        # Test with length 10
        result = generate_random_string(10)
        self.assertEqual(len(result), 10)

        # Test with length 0
        result = generate_random_string(0)
        self.assertEqual(len(result), 0)

        # Test with negative length
        result = generate_random_string(-5)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()