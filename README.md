# Gettysburg Address Dictionary

## Overview  
This Python script analyzes the text of the Gettysburg Address to count word frequencies. It reads the speech from a text file, processes the content by cleaning and splitting it into words, and outputs a report showing how often each word appears.

## Features  
- Cleans input text by removing punctuation and converting all words to lowercase  
- Counts occurrences of each unique word  
- Writes a detailed report of word counts sorted from most to least frequent  
- Handles missing file errors gracefully  

## How It Works  
1. The script reads the entire Gettysburg Address from `Gettysburg.txt` in the working directory.  
2. Each line is stripped of whitespace and punctuation, then split into words.  
3. Each word is added to a dictionary that keeps track of word counts.  
4. After processing all lines, the dictionary is sorted by frequency and written to an output report file.  

## How to Run  
1. Place `Gettysburg.txt` (the text file containing the speech) in the same folder as the script.  
2. Run the Python script (`python gettysburg_word_count.py` or your script name).  
3. When prompted, enter the name of the output file where you want the word frequency report saved (e.g., `report.txt`).  
4. Check the output file to see the word counts and dictionary size.  

## Example Output  
Length of dictionary: 175
Word---Count
the: 45
and: 30
to: 28
freedom: 15
nation: 10
...

## Requirements  
- Python 3.x  
- `Gettysburg.txt` file in the same directory  

## Notes  
- The script will display an error message if `Gettysburg.txt` is not found.  
- The output file will contain the full frequency report of words in the text.  

## Author  
Sarah Theriot
