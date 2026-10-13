def count_vowels(text):
    text= text.lower()
    count= 0
    vowels=["a", "e", "i", "o", "u"]

    for letter in text:
        if letter in vowels:
            count= count + 1

        
    return count


print (count_vowels("HELLO"))