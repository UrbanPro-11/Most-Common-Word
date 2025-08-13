import re
import os
from collections import Counter

# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'myText.txt')

# Functions + setup
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

def max_count(words):
    counts = Counter(words)
    return max(counts.values()) if counts else 0

def most_common_words(words):
    counts = Counter(words)
    max_count = max(counts.values())
    return [word for word, count in counts.items() if count == max_count]

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
else:
    common = most_common_words(words)
    print("Most common word(s):", ", ".join(common))
    print("Count:", max_count(words))
