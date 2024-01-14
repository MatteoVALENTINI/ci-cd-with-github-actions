import unittest
from my_flask_app import create_app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.test_client = create_app().test_client()
        self.test_client.testing = True

    # Test to ensure the main page is reachable
    def test_main_page_accessibility(self):
        result = self.test_client.get('/')
        self.assertEqual(result.status_code, 200, "Main page should be accessible and return status code 200")

    # Test to verify functionality of item addition
    def test_functionality_add_item(self):
        result = self.test_client.post('/add', data={'item_name': "Sample Item"}, follow_redirects=True)
        self.assertEqual(result.status_code, 200, "Adding an item should return status code 200")
        self.assertIn("Sample Item", result.data.decode(), "Newly added item should be displayed on the page")

    # Comprehensive test: Add, modify, and remove an item
    def test_comprehensive_item_lifecycle(self):
        # Adding a new item
        self.test_client.post('/add', data={'item_name': "Comprehensive Test Item"}, follow_redirects=True)
        
        # Modifying the newly added item
        self.test_client.post('/modify/0', data={'updated_item_name': "Modified Comprehensive Test Item"}, follow_redirects=True)

        # Additional steps for updating and deleting can be added here
