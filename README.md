Alu_regex-data-extraction-kamanzi2025

 Project Overview

This Python project implements a robust `DataExtractor` class utilizing regular expressions to extract key data types from unstructured text. Developed as part of the ALU Junior Full Stack Developer program's regular expression task, this tool focuses on accurately identifying and retrieving email addresses, URLs, phone numbers, hashtags, and currency amounts from extensive text data obtained from web APIs. The emphasis is on both the accuracy of the regular expressions and the ability to handle common variations and edge cases within these data formats.

This project aims to demonstrate a strong understanding of regular expressions, clean code practices, proper repository organization, and clear presentation of the project's functionality through well-documented code and illustrative test cases.

Features

This library provides the following data extraction capabilities with a focus on handling multiple formats and common edge cases:

Email Extraction: Extracts valid email addresses, including various subdomain structures and special characters.
URL Extraction:Identifies and extracts complete URLs with `http/https`, optional `www`, subdomains, paths, and basic query parameters.
Phone Number Extraction: Recognizes and extracts phone numbers in several international and domestic formats, including those with parentheses, hyphens, periods, spaces, and optional country codes.
Hashtag Extraction: Extracts social media hashtags, including those with alphanumeric characters and underscores.
Currency Amount Extraction: Identifies currency amounts with a dollar sign ($), handling commas for thousands separators and up to two decimal places.

Getting Started

1.  Prerequisites:
     Python 3.x installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2.  Repository Setup:
    Clone this repository to your local machine using Git:
        ```bash
        git clone [https://github.com/kamanzi2025/alu_regex-data-extraction-kamanzi2025.git](https://github.com/kamanzi2025/alu_regex-data-extraction-kamanzi2025.git)
        cd alu_regex-data-extraction-kamanzi2025
        ```
    * Ensure the `extractor.py` file is in the root of your repository.

3.  Running the Code:
    * You can execute the `extractor.py` script directly from your terminal:
        ```bash
        python extractor.py
        ```
    * This will run the data extraction on the predefined `sample_text` and display the results in the console.

Code Structure

* `DataExtractor` Class:
    `extract_emails(text: str) -> List[str]`: Static method to extract email addresses using a robust regex.
     `extract_urls(text: str) -> List[str]`: Static method to extract URLs, handling various common formats.
     `extract_phone_numbers(text: str) -> List[str]`: Static method to extract phone numbers with support for multiple regional formats.
     `extract_hashtags(text: str) -> List[str]`: Static method to extract hashtags.
     `extract_currency_amounts(text: str) -> List[str]`: Static method to extract currency amounts with dollar signs, commas, and decimal points.
     `display_results(data_type: str, results: List[str]) -> None`: Function to format and display the extracted results in a clear and readable manner in the console.
* `if __name__ == "__main__":`: Block containing the `sample_text` and calls to the extraction and display functions to demonstrate the functionality.

Regular Expression Details and Edge-Case Handling

Here's a breakdown of the regular expressions used and how they attempt to handle common edge cases:

Email:`r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'`
Edge Cases Handled:Handles multiple subdomains, numeric and hyphenated domain names, and various special characters in the local part. The `\b` ensures it matches whole email addresses.

Limitations:May not catch all theoretically valid but extremely unusual email formats.

URL:`r'https?://(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?:[\/#?][^\s]*)?\b'`

Edge Cases Handled:Handles both `http` and `https`, optional `www`, multiple subdomains, paths, and basic query parameters or fragments indicated by `/`, `#`, or `?`. The `\b` helps prevent partial matches.

Limitations:May not perfectly handle very complex URLs with unusual characters or encoding.

Phone Number:`r'(?:\+|00)?[\d\s().-]{7,}'`
Edge Cases Handled:This more flexible regex attempts to capture various international and domestic formats by looking for an optional `+` or `00` (for international prefixes), followed by at least 7 digits with potential spaces, parentheses, periods, or hyphens as separators.
Limitations:Doesn't strictly validate the length or specific structure of phone numbers from all regions.

Hashtag:`r'#\w+'`
Edge Cases Handled:Matches hashtags with alphanumeric characters and underscores.
limitations:** Won't capture hashtags with hyphens or other special characters sometimes used in social media.

Currency Amount:`r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?\b'`
Edge Cases Handled:Handles single and multi-digit dollar amounts, optional thousands separators (commas), and an optional decimal part with exactly two digits. The `\b` ensures it's a standalone amount.
Limitations:Only handles the dollar sign (`$`) and assumes the standard comma as a thousands separator and period as a decimal separator.

Output Presentation and Test Cases

When you run `python extractor.py`, you will see the following output, demonstrating the extraction results from the `sample_text`:
