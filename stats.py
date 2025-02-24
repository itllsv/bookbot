def get_book_text(filepath):
    file_content = None
    with open(filepath) as f:
        file_content = f.read()

    return file_content

def words_count(text):
    return len(text.split())

def letters_text_count(text):
    letters = dict()
    for l in text:
        letter = l.lower()
        if letter in letters.keys():
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters
