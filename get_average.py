def get_average(numbers):

    total = 0
    for number in numbers:
        total = total + number
    return total / len(numbers)


print (get_average([]))