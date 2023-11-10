import argparse
import re
from collections import Counter

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    return len(text)

def count_lines(text):
    lines = text.splitlines()
    return len(lines)

def find_most_common_words(text, num_words=10):
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    common_words = word_counts.most_common(num_words)
    return common_words

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text Analysis Tool")
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("--count-words", action="store_true", help="Count the number of words")
    parser.add_argument("--count-characters", action="store_true", help="Count the number of characters")
    parser.add_argument("--count-lines", action="store_true", help="Count the number of lines")
    parser.add_argument("--common-words", type=int, help="Find the most common words")
    
    args = parser.parse_args()
    
    try:
        with open(args.input_file, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: The specified input file does not exist.")
        exit(1)
    
    if args.count_words:
        word_count = count_words(text)
        print(f"Number of words: {word_count}")
    
    if args.count_characters:
        char_count = count_characters(text)
        print(f"Number of characters: {char_count}")
    
    if args.count_lines:
        line_count = count_lines(text)
        print(f"Number of lines: {line_count}")
    
    if args.common_words:
        common_words = find_most_common_words(text, args.common_words)
        print(f"Most common words:")
        for word, count in common_words:
            print(f"{word}: {count}")

