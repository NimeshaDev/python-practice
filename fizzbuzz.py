def fizzbuzz(n):

    result=[]

    for number in range(1, n+1):
        if number % 15 ==0:
            result.append("fizzbuzz")

        elif number % 3 ==0:
            result.append("fizz")
        
        elif number % 5 ==0:
            result.append("buzz")
        
        else:
            result.append(number)

    return result

print (fizzbuzz(15))
