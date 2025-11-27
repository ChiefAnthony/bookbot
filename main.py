import sys

from stats import char_count, get_length, sorted_dict


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()

        return file_contents


def main():
    # book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = get_length(book_text)

    char = char_count(book_text)

    sorted_char = sorted_dict(char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
