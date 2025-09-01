import os
import string
from collections import Counter

def count_words():
    # Get the folder where this script is located
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(base_path, "paragraph.txt")

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()

        # Remove punctuation and convert to lowercase
        translator = str.maketrans("", "", string.punctuation)
        clean_text = text.translate(translator).lower()

        # Split into words
        words = clean_text.split()

        # Count words
        word_count = Counter(words)

        # Display results in alphabetical order
        print("Word Frequencies (Alphabetical Order):\n")
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"Error while processing file: {str(e)}")


if __name__ == "__main__":
    count_words()
