from stats import (
    get_book_text,
    words_count,
    letters_text_count
)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = words_count(book_text)
    print(f"{num_words} words found in the document")
    print(letters_text_count(book_text))

main()
