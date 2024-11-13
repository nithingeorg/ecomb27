# 2. URL Testing
from django.test import TestCase

# Create class for test url
class testURL(TestCase):
    # Create function for test home url
    def testhomeurl(self):
        # Get home url
        home_url_response = self.client.get('/')
        print(home_url_response)
        # Check Actual Result with Expected Result
        self.assertEqual(home_url_response.status_code, 200)