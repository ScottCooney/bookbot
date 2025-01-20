def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(char_count(get_book_text(book_path)))
    

def char_count(input):
    characters = {}
    for char in input.lower():
        characters[char] = characters.get(char , 0) + 1
    return characters      


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
