def word_counter(book_text):
    return len(book_text.split())
def character_counter(book_text):
    result = {}
    for character in book_text:
        character = character.lower()
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result
def sort_characters(char_dict):
    char_list = []
    for char, num in char_dict.items():
        char_list.append({"char": char, "num": num})
    sorted_char = sorted(char_list, reverse=True, key=lambda items: items["num"])
    return sorted_char