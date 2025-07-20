def get_num_words(input_text):
    return len(input_text.split())

def get_num_letters(input_words):
    # list_words = input_words.split() - no
    lower_input_words = input_words.lower()
    letters = {}
    for letter in lower_input_words:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
            
    return letters

def sort_on(items):
    return items["num"]


# Issue List and dict
def create_list(letters):
    formated_dict = {}
    sorted_list = []
    for letter in letters:
        formated_dict = {"char": letter, "num": letters[letter]}
        sorted_list.append(formated_dict)

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list