# Text Analysis Tool

This is a simple Python script for analyzing text files. It provides various functionalities, including counting lines, words, unique words, and calculating statistics such as the average word length, the most common word, and more.

## Features

- Count the number of lines in a text file.
- Count the total number of words in the text file.
- Count the number of unique words.
- Find the most common word and its frequency.
- Find the longest word in the text.
- Calculate the average word length.
- Determine the percentage of words longer than the average word length.
- Count occurrences of a specific word in the text.

## Requirements

- Python 3.x
- No additional libraries are required, as the script uses built-in modules.

## Functions

read_file(filename)
Reads the content of the specified file.

count_lines(content)
Counts the number of lines in the text.

count_words(content)
Counts the total number of words in the text.

count_unique_words(content)
Counts the number of unique words in the text.

most_common_word(content)
Finds the most common word in the text.

longest_word(content)
Finds the longest word in the text.

count_specific_word(content, specific_word)
Counts occurrences of a specific word in the text.

average_word_length(content)
Calculates the average length of words in the text.

percentage_longer_than_average(content)
Calculates the percentage of words longer than the average word length.

analyze_text(filename)
Performs a full analysis of the text file and prints the results.

test_specific_word_count(filename, word)
Tests and prints the occurrence of a specific word in the text file.


