import unittest
from src.rtf import rtf

TEST_CASES = []

class TestRTF(unittest.TestCase):

    def test_rtf_pattern_to_read_dir(self):
        TEST_CASES.append(
            "rtf_pattern_to_read_dir - wrong path"
        )
        wrong_path = "B500_50_100"
        self.assertFalse(rtf.pattern_to_read_dir(wrong_path), f"{wrong_path} should return False")

        TEST_CASES.append(
            "rtf_pattern_to_read_dir - correct path"
        )
        correct_path = "C500_50_100"
        self.assertTrue(rtf.pattern_to_read_dir(correct_path), f"{correct_path} should return True")

if __name__ == "__main__":
    unittest.main()