def first_non_repeating(text):
    count= {}

    for letter in text:
        if letter in count:
            count[letter] =count[letter]+1 
        else:
            count[letter]= 1

    for letter in text:
       if count[letter] == 1:
        return letter

    return None
    

print(first_non_repeating("banana"))    # b
print(first_non_repeating("aabbcd"))    # c
print(first_non_repeating("aabb"))      # None
print(first_non_repeating("")) 