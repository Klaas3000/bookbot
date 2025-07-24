def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def character_counter(text):
    words = text.split()
    counter_dict ={}
    for letter in text:
        if letter.lower() in counter_dict:
            counter_dict[letter.lower()] += 1
        else:
            counter_dict[letter.lower()] = 1
    return counter_dict

def sort_on(items):
    return items["num"]

def chracter_sorter(count_dict):
    new_dict = []
    for charecter in count_dict:
        new_dict.append({"char":charecter,"num":count_dict[charecter]})
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict 