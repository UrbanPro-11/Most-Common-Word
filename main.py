import re, os
from collections import Counter
import wordMode as wm
import wordLength as wl

# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'myText.txt')

def clean_text(text):
    return re.sub(r'[^\w\s]', ' ', text).lower()

def write_to_file(path):
    lines = []
    print("Enter your text (type 'write.end' to stop):")
    while True:
        line = input()
        if line == "write.end":
            break
        lines.append(line)
    with open(path, 'w') as f:
        f.write("\n".join(lines))

def read_from_file(path):
    with open(path, 'r') as f:
        return f.read()

# Main program
if input("Write to file? (yes/no): ").strip().lower() in ['y', 'yes']:
    write_to_file(file_path)
    content = read_from_file(file_path)
else:
    content = read_from_file(file_path)

cleaned = clean_text(content)
words = cleaned.split()
if not words:
    print("No words found.")

def most_common():
    common = wm.most_common_words(words)
    print("Most common word(s):", ", ".join(common))
    print("Count:", wm.max_count(words))

def average_len():
    average_length = wl.avg_len(words)
    total_words = wl.count_words(words)
    print("There were", total_words, "words in total and", int(average_length*total_words), "characters.")
    print("The average word length is:", average_length)

choice = input("Would you like to check the average word length or the most common word? ").strip().lower()

if choice in ['most', 'common', 'mode', 'm', 'c', 'most common word', 'most common', 'common word', 'most word',
              'word most', 'word common']: # I know this is overkill I'm sorry (?)
    most_common()
elif choice in ['average', 'len', 'length', 'avg', 'a', 'l', 'average word length', 'word length']:
    average_len()
else:
    most_common()
    average_len()
