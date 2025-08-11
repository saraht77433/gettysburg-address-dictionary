# DSC510
# Programming Assignment Week 7
# Sarah Theriot
# 7/17/2024

# Changelog
# Change Made: Added new functions to assist in opening and writing files
# Date of Change: 7/23/2024
# Author: Sarah Theriot

import string


def add_word(word, word_dict):
    """Add each word to the dictionary."""
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


def process_line(line, word_dict):
    """Process a single line of text. Strip off various characters, split into words, clean, and add to dictionary."""
    line = line.strip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    words = line.lower().split()

    for word in words:
        add_word(word, word_dict)


def process_file(file_name, word_dict):
    """Process each line in the file and list word frequencies to a text file."""
    with open(file_name, 'r') as gba_file:
        for line in gba_file:
            process_line(line, word_dict)


def write_report(file_name, word_dict):
    """Write the dictionary length and word frequencies to a text file."""
    with open(file_name, 'w') as report_file:
        report_file.write(f"Length of dictionary: {len(word_dict)}\n")
        report_file.write(f"Word---Count\n")
        report_file.write("------------")
        sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_words:
            report_file.write(f'{word}: {count}'"\n")


def main():
    word_dict = {}
    file_name = input("Enter file name: ")

    try:
        process_file('Gettysburg.txt', word_dict)
        write_report(file_name, word_dict)
        print(f'Report written to {file_name}')
    except FileNotFoundError:
        print('Error. File not found')


if __name__ == '__main__':
    main()
