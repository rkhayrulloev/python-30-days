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

