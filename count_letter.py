def count_letter(text, letter_to_find):
    count = 0

    for letter in text:
        if letter == letter_to_find:
            count = count + 1

    return count


print(count_letter("banana", "a"))