books_path = './books/frankenstein.txt'


def main():
    content = get_book_content(books_path)
    char_report = count_Chars(content)
    print(f"---Printing Report from {books_path}---")
    print(f"Total {len(split_string(content))} words found \n")
    print_each_word_with_count(char_report)


def get_book_content(path):
    with open(path) as f:
        return f.read()


def split_string(string):
    return string.split()


def count_Chars(string):
    chars = {}
    for text in string:
        converted_string = text.lower()
        if converted_string in chars:
            chars[converted_string] += 1
        else:
            chars[converted_string] = 1
    return chars


def print_each_word_with_count(dictionary):
    keys = list(dictionary.keys())
    keys.sort()
    for key in keys:
        if key.isalpha():
            print(f"The char {key} was found {dictionary[key]} times")


main()
