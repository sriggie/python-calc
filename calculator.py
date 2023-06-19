import math

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def logarithm(a):
    return math.log10(a)

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))

# Displaying the interactive menu
while True:
    print("Scientific Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Logarithm")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Exiting the calculator...")
        break

    if choice < 1 or choice > 11:
        print("Invalid choice. Please try again.")
        continue

    if choice == 7 or choice == 8:
        num1 = float(input("Enter the number: "))
    else:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    result = 0

    if choice == 1:
        result = addition(num1, num2)
    elif choice == 2:
        result = subtraction(num1, num2)
    elif choice == 3:
        result = multiplication(num1, num2)
    elif choice == 4:
        result = division(num1, num2)
    elif choice == 5:
        result = modulus(num1, num2)
    elif choice == 6:
        result = power(num1, num2)
    elif choice == 7:
        result = square_root(num1)
    elif choice == 8:
        result = logarithm(num1)
    elif choice == 9:
        result = sine(num1)
    elif choice == 10:
        result = cosine(num1)
    elif choice == 11:
        result = tangent(num1)

    print("Result:", result)
    print()
