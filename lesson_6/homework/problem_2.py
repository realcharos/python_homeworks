import os
import string
from collections import Counter


def get_text():
    """Read 'sample.txt' or create it if missing."""
    if not os.path.exists("sample.txt"):
        text = input("Enter text for 'sample.txt':\n")
        with open("sample.txt", "w") as file:
            file.write(text)
    with open("sample.txt", "r") as file:
        return file.read()


def count_words(text):
    """Count word frequency, ignoring punctuation and capitalization."""
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return Counter(words)


def main():
    text = get_text()
    word_counts = count_words(text)

    total_words = sum(word_counts.values())
    common_words = word_counts.most_common(5)

    print(f"Total words: {total_words}")
    print("Top 5 words:")
    for word, count in common_words:
        print(f"{word}: {count}")

    with open("word_count_report.txt", "w") as file:
        file.write(f"Total words: {total_words}\n")
        file.write("Top 5 words:\n")
        for word, count in common_words:
            file.write(f"{word}: {count}\n")


if __name__ == "__main__":
    main()
