# 1. Functions Testing
from django.test import TestCase

# Create function to perform concat
def concat_string(txt1, txt2):
    return txt1 + txt2

# Create class for Test Scenario and function for Test Cases
class test_scenario(TestCase):
    def test_cases_1(self):
        # Assert - Actual Result with Expected Result
        self.assertEqual(concat_string("Python", "Program"), "Python Program")
# ========================================================================================================
