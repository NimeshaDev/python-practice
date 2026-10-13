def find_largest(numbers):
    n = numbers[0]


    for number in numbers:

        if number >= n:
            n = number
    return n

print (find_largest([1,2,8,4,]))
