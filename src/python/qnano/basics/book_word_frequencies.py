from collections import Counter
from pathlib import Path
import pkg_resources
import re


def get_book_word_frequencies(book_file_name):

    with open(book_file_name, 'r') as opened_file:
        words = re.findall(r'\w+', open(book_file_name).read().lower())
        words_dict = Counter(words)

    return words_dict


# 10 unique words, 5 repeated

book_file_name = Path(pkg_resources.resource_filename(
            "qnano", "data/small_book.txt"))

book_words = get_book_word_frequencies(str(book_file_name))

print("Number of words: ", len(book_words))
print("word freqs: ", book_words)

# Longer book

book_file_name = Path(pkg_resources.resource_filename(
            "qnano", "data/book.txt"))

book_word_frequencies = get_book_word_frequencies(str(book_file_name))

print("Number of words: ", len(book_word_frequencies))


