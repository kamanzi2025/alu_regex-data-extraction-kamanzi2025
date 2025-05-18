import re
from typing import List

class DataExtractor:
    """Extracts structured data from unstructured text using regex patterns."""
    
    @staticmethod
    def extract_emails(text: str) -> List[str]:
        """
        Extracts email addresses from text.
        Matches: user@domain.com, first.last@sub.domain.co.uk
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_urls(text: str) -> List[str]:
        """
        Extracts complete URLs including paths.
        Matches: 
        - http://sub.example.org/path
        - https://example.com/page.html
        - http://example.co.uk/path/subdir
        """
        pattern = r'https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+(?:/[^\s]*)?'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_phone_numbers(text: str) -> List[str]:
        """
        Extracts phone numbers in multiple formats.
        Matches: (123) 456-7890, 123-456-7890, 123.456.7890
        """
        pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_hashtags(text: str) -> List[str]:
        """
        Extracts social media hashtags.
        Matches: #hello, #Python3, #ALUMarch2023
        """
        pattern = r'#\w+'
        return re.findall(pattern, text)

def display_results(data_type: str, results: List[str]) -> None:
    """Formats extraction results for CLI display."""
    print(f"\n{'='*50}")
    print(f"{data_type.upper()} ANALYSIS".center(50))
    print(f"{'='*50}")
    if results:
        print(f"Found {len(results)} {data_type}(s):")
        for i, item in enumerate(results, 1):
            print(f"  {i}. {item}")
    else:
        print(f"No {data_type} found.")
    print(f"{'-'*50}")

if __name__ == "__main__":
    sample_text = """
    Contact us at support@example.com or sales@company.co.uk.
    Visit https://www.example.com or call (123) 456-7890.
    Follow #ExampleCompany on social media. Invalid data: $1.234, @test.
    """

    print("\n" + "="*50)
    print("TEXT DATA EXTRACTION REPORT".center(50))
    print("="*50)
    
    display_results("email address", DataExtractor.extract_emails(sample_text))
    display_results("URL", DataExtractor.extract_urls(sample_text))
    display_results("phone number", DataExtractor.extract_phone_numbers(sample_text))
    display_results("hashtag", DataExtractor.extract_hashtags(sample_text))
    
    print("\n" + "="*50)
    print("ANALYSIS COMPLETE".center(50))
    print("="*50)