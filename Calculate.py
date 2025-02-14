# Calculate.py

# Programmer: Mason Shipton
# Description: Calculates the sum, difference, product, and quotient of two user-entered integers.
# Date Created: 2025-02-13
# Date Last Revised: 2025-02-13

def sum(a, b):
    sum = a + b
    return sum

def difference(a, b):
    difference = a - b
    return difference

def product(a, b):
    product = a * b
    return product

def quotient(a, b):
    quotient = a / b
    return quotient

a = input("Enter a number")
b = input("Enter another number")

print("Sum of " + a + " and " + b + " is " + sum(a, b))
