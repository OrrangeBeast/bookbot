import sys
from stats import word_counter
from stats import character_counter
from stats import sort_characters
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main(path):
    text = get_book_text(path)
    num_words = word_counter(text)
    num_characters = character_counter(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for group in sort_characters(num_characters):
        character = group["char"]
        number = group["num"]
        if character.isalpha():
            print(f"{character}: {number}")
    print("============= END ===============")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    main(path)