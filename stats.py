def get_book_text(filepath):
    file_content = None
    with open(filepath) as f:
        file_content = f.read()

    return file_content

def words_count(text):
    return len(text.split())

def sort_on(dict):
    return dict["num"]

def letters_text_count(text):
    letters = dict()
    list = []
    for l in text:
        letter = l.lower()
        if letter in letters.keys():
            letters[letter] += 1
        else:
            letters[letter] = 1

    for key in letters:
        list.append({"name": key, "num": letters[key]})

    list.sort(reverse=True, key=sort_on)

    for item in list:
        print(f"{item["name"]}: {item["num"]}")

