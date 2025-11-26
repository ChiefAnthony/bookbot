def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()

        return file_contents


def get_length(book_text: str) -> int:
    num_words = book_text.split()
    return len(num_words)


def main():
    book_text = get_book_text("books/frankenstein.txt")

    num_words = get_length(book_text)

    print(f"Found {num_words} total words.")


if __name__ == "__main__":
    main()
