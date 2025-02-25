from stats import (
    get_book_text,
    words_count,
    letters_text_count
)

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = words_count(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ---------- ")
    print(f"Found {num_words} total words")
    print("----------- Character Count ---------- ")
    letters_text_count(book_text)
    print("============= END ===============")


main()
