def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = char_count(text)
    report(num_words,num_chars)
    

def report(wordcount,chars):
    alpha = []
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount} words found in the document")
    for char in chars:
        if char.isalpha() == True:
            alpha.append({char : chars[char]})
            #print(f"{char} has {chars[char]}")
    def sort_on(item):
        return list(item.values())[0]
    alpha.sort(reverse=True, key=sort_on)
    for i in range (len(alpha)):
        for char, count in alpha[i].items(): 
            print(f"The '{char}' character was found {count} times")



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
