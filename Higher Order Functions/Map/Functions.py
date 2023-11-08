import math
# Convert list of strings to integers
strings = ['1', '2', '3', '4']
li=list(map(int,strings))
print(li)
# Calculate the length of strings in a list
words = ['apple', 'banana', 'cherry']
lengths = list(map(len, words))
print(lengths)
# Finding the square root of a list of numbers
numbers = [9, 16, 25, 36]
square_roots = list(map(math.sqrt, numbers))
print(square_roots)
# Square Also
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)
#Converting Fahrenheit to Celsius:
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

temperatures_in_fahrenheit = [32, 68, 100, 212]
temperatures_in_celsius = map(fahrenheit_to_celsius, temperatures_in_fahrenheit)
print(list(temperatures_in_celsius)) 