from collections import Counter

# Functions for finding the average length of a word
def count_words(words):
    total_words = Counter(words)
    return sum(total_words.values())

def avg_len(words):
    total_words = count_words(words)
    total_letters = 0
    for word in words:
        for _ in word:
            total_letters += 1
    return total_letters/total_words
