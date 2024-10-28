
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters

def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")

from collections import Counter





#exercise.

#most unique words in text.

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

# Run the analysis
analyze_text('sample.txt')


from collections import Counter

#most unique words in text.

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def count_lines(content):
    return len(content.split('\n'))

def count_words(content):
    return len(content.split())

def count_unique_words(content):
    words = content.lower().split()
    unique_words = set(words)
    return len(unique_words)

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

#longest word in text.

def longest_word(content):
    words = content.split()
    return max(words, key=len)

def count_specific_word(content, specific_word):
    words = content.lower().split()
    return words.count(specific_word.lower())

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def percentage_longer_than_average(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_words = [word for word in words if len(word) > avg_length]
    return (len(longer_words) / len(words)) * 100

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    num_unique_words = count_unique_words(content)
    common_word, count = most_common_word(content)
    longest = longest_word(content)
    avg_length = average_word_length(content)
    percentage_longer = percentage_longer_than_average(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Longest word: '{longest}'")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Percentage of words longer than the average length: {percentage_longer:.2f}%")

# Test with a specific word count
def test_specific_word_count(filename, word):
    content = read_file(filename)
    specific_word_count = count_specific_word(content, word)
    print(f"The word '{word}' appears {specific_word_count} times.")

# Run the analysis
analyze_text('sample.txt')
test_specific_word_count('sample.txt', 'engineering')  # Replace 'your_word_here' with the word you want to count
