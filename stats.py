def get_length(book_text: str) -> int:
    num_words = book_text.split()
    return len(num_words)


def char_count(book_text: str):
    dictionary = {}
    lowered_text = book_text.lower()
    for char in lowered_text:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    return dictionary


def sorted_dict(items):
    result = []

    def get_num(dict):
        return dict["num"]

    for key, value in items.items():
        new_dict = {"char": key, "num": value}
        result.append(new_dict)

    result.sort(key=get_num, reverse=True)

    return result
