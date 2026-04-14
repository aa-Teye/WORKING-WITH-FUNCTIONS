def add_add(num1: int, num2: int):
    return num1 + num2


num1 = int(input ("Enter the first number: "))
num2 = int(input ("Enter the second number: "))
result = add_add(num1, num2)

if result >= 20:
    print("Successfully nailed the code!")