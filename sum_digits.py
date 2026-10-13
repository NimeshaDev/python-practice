def sum_digits(numbers):

    total=0

    for number in  str(numbers):
         total= int(number) + total
    
    return total

print (sum_digits(1233))

