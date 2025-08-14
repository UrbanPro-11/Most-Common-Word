from collections import Counter

# Functions for finding the most common word(s)
def max_count(words):
    counts = Counter(words)
    return max(counts.values()) if counts else 0

def most_common_words(words):
    counts = Counter(words)
    max_count = max(counts.values())
    return [word for word, count in counts.items() if count == max_count]
