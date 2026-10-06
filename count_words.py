def count_words(sentence):
    count= {}

    for word in sentence.split():
        if word in count:
            count[word] = count[word]+ 1
        else:
            count[word] = 1
    return count 

print (count_words("test the test"))