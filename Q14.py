def factorial(n):
    if n < 0:
        return "not exist  "
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("The factorial is ", factorial(num))