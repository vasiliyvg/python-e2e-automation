def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1

    return num * factorial(num - 1)

num = 5
print(factorial(num))
