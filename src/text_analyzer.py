from collections import Counter
import re

def word_count(text: str) -> int:
    """Returns the total number of words in the text."""
    # Split by whitespace, ignoring empty elements caused by multiple spaces
    words = text.split()
    return len(words)

def character_count(text: str) -> int:
    """Returns the total number of characters in the text, including spaces."""
    return len(text)

def sentence_count(text: str) -> int:
    """Returns the total number of sentences based on terminal punctuation (. ! ?)."""
    if not text.strip():
        return 0
    # Splits the text wherever a periods, exclamation, or question marks occurs
    sentences = re.split(r'[.!?]+', text)
    # Remove trailing empty strings resulting from a terminal punctuation mark
    return len([s for s in sentences if s.strip()])

def unique_word_count(text: str) -> int:
    """Returns the number of unique words, ignoring case and punctuation."""
    # Find all sequences of alphanumeric characters, converted to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    return len(set(words))

def most_common_word(text: str) -> str:
    """Returns the most frequent word in the text (case-insensitive).
    Returns an empty string if the text contains no words.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return ""
    
    # Count occurrences and return the top result
    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]
