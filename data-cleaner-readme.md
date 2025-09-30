# Reddit Data Cleaning Utility

This script is designed to process the JSON files created by the Reddit scraper. It transforms the raw data into a structured, readable text file that is suitable for analysis or for use with language models.

## Core Functionality

- **Processes JSON Files:** It is built to read the specific JSON structure produced by the accompanying Reddit scraping script.  
- **Organizes Information:** Each post and its associated comments are formatted into a clear, sequential layout, making the conversations easy to follow.  
- **Highlights Key Details:** The script extracts essential metadata for each post, including the title, author, score, and original posting date.  
- **Produces a Text File:** The final result is a `.txt` file, a universal format that can be easily opened, shared, or uploaded to other applications.  

## System Requirements

- Python 3  
- No external libraries are needed; all modules used are part of the standard Python installation.  

## Instructions for Use

1. Make sure this script is located in the same directory as the JSON file you intend to clean.  
2. Open a terminal or command prompt window.  
3. Navigate to the directory containing the script and your data file.  
4. Execute the script using the following command:

   ```bash
   python clean_data.py
