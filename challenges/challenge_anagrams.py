def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    first_sorted = sorted_string(first_string)
    second_sorted = sorted_string(second_string)

    if not first_sorted or not second_sorted:
        return first_sorted, second_sorted, False
    return first_sorted, second_sorted, first_sorted == second_sorted


def sorted_string(string):
    char_count = [0] * 26  # Contador para as letras do alfabeto (a-z)

    for char in string:
        if char.isalpha():
            index = ord(char) - ord("a")
            char_count[index] += 1

    sorted_str = ""
    for i, count in enumerate(char_count):
        sorted_str += chr(i + ord("a")) * count

    return sorted_str
