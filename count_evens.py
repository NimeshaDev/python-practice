def count_evens(numbers):

    count= 0

    for number in numbers:
        if number % 2 == 0 :
            count= count +1


    return count

print(count_evens([1,2,3,4,5,6]))
