# Day 3 – Python Basic Exercises 1-50
print("Hello, bu mening 30 kunlik sayohatim!")

# 1. Write a Python program to print "Twinkle, twinkle, little star" formatted poem
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are")

# 2 Write a Python program to find out what version of Python you are using.
import sys
print('Python version' +sys.version)

#3 Write a Python program to display the current date and time.
import datetime
now = datetime.datetime.now()
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

#4 Write a Python program that calculates the area of a circle based on the radius entered by the user.
import math
radius = float(input('Enter the radius of the circle: '))
area = math.pi * radius ** 2
print(f'The area of the circle with radius {radius} is: {area}')

#5 Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print(f'Reversed name: {last_name} {first_name}')

#6 Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
numbers = input('Enter a sequence of comma-separated numbers: ')
number_list = numbers.split(',')
number_tuple = tuple(number_list)
print(f'List: {number_list}')
print(f'Tuple: {number_tuple}')

#8 Write a Python program to display the first and last colors from the following list.
color_list = ["Red", "Green", "White", "Black"]
print(f'First color: {color_list[0]} and Last color: {color_list[-1]}')

#9 Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
print(f'Examination date: {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}')

#10 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n = int(input('Enter an integer: '))
nn = int(f"{n}{n}")
nnn = int(f"{n}{n}{n}")
result = n+nn+nnn
print(f"the result of n + nn++nnn is : {result}")

#11 Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
print(abs.__doc__)
print(int.__doc__)

