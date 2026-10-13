def is_anagram(first, second):

    if sorted(first)== sorted(second):

        return True

    else:
        return False


print (is_anagram("dormitory", "dirty room"))