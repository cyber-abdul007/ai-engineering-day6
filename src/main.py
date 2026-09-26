# Import all 5 analytical functions from your module
from text_analyzer import (
    word_count,
    character_count,
    sentence_count,
    unique_word_count,
    most_common_word
)

# Define a comprehensive sample sentence to test layout boundaries and repetitions
sample_text = "Learning Python is fun, and data analytics makes Python even more powerful! Are you ready to learn?"

# Run and print the output of each function
print("--- Text Analyzer Test Results ---")
print(f"Sample Text:        \"{sample_text}\"\n")

print(f"Total Words:        {word_count(sample_text)}")        # Expected: 16
print(f"Total Characters:   {character_count(sample_text)}")  # Expected: 97
print(f"Total Sentences:    {sentence_count(sample_text)}")   # Expected: 2
print(f"Unique Words:       {unique_word_count(sample_text)}")# Expected: 14 ("python" and "learn/learning" treated appropriately)
print(f"Most Common Word:   '{most_common_word(sample_text)}'") # Expected: 'python' (appears 2 times)
