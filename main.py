import sys
from stats import get_num_words, get_num_letters, create_list

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def print_report(numbers, chars, text_path):
    header = "============ BOOKBOT ============"
    message_one = f"Analyzing book found at {text_path}"
    header_two = "----------- Word Count ----------"
    message_word_count = f"Found {numbers} total words"
    header_three = "--------- Character Count -------"
    message_end = "============= END ==============="

    print(header)
    print(message_one)
    print(header_two)
    print(message_word_count)
    print(header_three)

    for char in chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print (message_end)


def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
    
    path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    text_data = get_num_letters(text)
    print_report(get_num_words(text), create_list(text_data), path_to_book)

main()


