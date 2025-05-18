import unittest
from extractor import DataExtractor  # Fixed: Removed space after "import"

class TestDataExtractor(unittest.TestCase):
    def test_extract_emails(self):  # Fixed: Changed "emails" (original had typo)
        self.assertEqual(
            DataExtractor.extract_emails("Contact user@example.com"),
            ["user@example.com"]
        )
        self.assertEqual(
            DataExtractor.extract_emails("Invalid: user@.com"),
            []
        )

    def test_extract_urls(self):
    # Test full URL with path
        self.assertEqual(
        DataExtractor.extract_urls("Visit http://sub.example.org/path"),
        ["http://sub.example.org/path"]  # Now matches full URL with path
    )
    
    # Still rejects invalid URLs
        self.assertEqual(
        DataExtractor.extract_urls("Invalid: http://.com"),
        []
    )
    def test_extract_phone_numbers(self):
        self.assertEqual(
            DataExtractor.extract_phone_numbers("Call (123) 456-7890"),
            ["(123) 456-7890"]
        )
        self.assertEqual(
            DataExtractor.extract_phone_numbers("123.456.7890"),
            ["123.456.7890"]
        )

    def test_extract_hashtags(self):
        self.assertEqual(
            DataExtractor.extract_hashtags("#Hello #World"),
            ["#Hello", "#World"]
        )
        self.assertEqual(
            DataExtractor.extract_hashtags("No tags here"),
            []
        )

if __name__ == '__main__':
    unittest.main()