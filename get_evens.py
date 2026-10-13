def get_evens(numbers):

    results =[]

    for number in numbers:

        if number % 2 ==0:

            results.append(number)

    return results


print (get_evens([1, 2, 3, 4, 6]))
print (get_evens([1, 3, 5]))
print (get_evens([]))
print (get_evens([2, 2, 4]))