# File: main.py
from wordlyzer import WordLyzer

# sample text
text = """Python is an amazing programming language. It's widely used for web development, data analysis, and AI.\n\nThis is a second paragraph."""

# Text to analyze
analyzer = WordLyzer(text)

# Result
print("Word Count:", analyzer.word_count())
print("Sentence Count:", analyzer.sentence_count())
print("Paragraph Count:", analyzer.paragraph_count())
print("Character Count:", analyzer.character_count())
print("Most Common Words:", analyzer.most_common_words())
print("Average Word Length:", analyzer.average_word_length())
print("Average Sentence Length:", analyzer.average_sentence_length())
