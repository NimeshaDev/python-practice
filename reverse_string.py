def reverse_string(text):
    result = ""
    for letter in text:
        result = letter + result
    return result

print(reverse_string("hello"))