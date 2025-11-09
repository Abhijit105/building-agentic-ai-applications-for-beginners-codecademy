def odd_or_even(number):
    return "odd" if number % 2 != 0 else "even"

print(odd_or_even(120))

# def factorial(number):
#     if number == 0:
#         return 1
# 
#     return number * factorial(number - 1)

def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i

    return result

print(factorial(5))
print(factorial(25))

def print_odd(min, max):
    for num in range(min, max, 2):
        if(num % 2 != 0):
            print(num)
        else:
            num += 1
            print(num)

print_odd(2, 20)
