import sys
# This file contains code mostly written as I read through Python Crash Course book
# Chapter 1 and 2
# Using Python 3 with Atom and Script
print("Hello World!")
print(sys.version)
# print(sys.version_info)

message = "Hello World!"
print(message)

message = "Python Crash Course!"
print(message)

message = "Some dumb statement!"
# print(mesage) intentional error

# Traceback (most recent call last):
#   File "/dev/edu/python/PythonCrashCourse/helloWorld.py", line 13, in <module>
#     print(mesage)
# NameError: name 'mesage' is not defined

mesage = "Another dumb statement!"
print(mesage) #compilers don't care about spellings, obviously!

#types of string
str1 = "Gandalf exclaimed, 'You shall not pass!'"
print(str1)

str1 = 'Gandalf exclaimed, "You shall not pass!"'
print(str1)

str1 = "Jay is dumb and Jay's code is dumber"
print(str1)

name = "prof. alAn turing"
print(name.title())
print(name.lower())
print(name.upper())

#concatenation
title = "dr."
first = "srinivasa"
last = "ramanujan"
name = title + " " + first + " " + last
print(name)
print(name.title())

#tabs and newlines
british = title + " " + last + ", " + first
print("\t" + british.title())

print("hello\nit's me\nadele")
print("Songs:\n\tHello\n\tPumped up kicks\n\tRain Plans")

#strip whitespace
favourite_language = ' Julia '
print(favourite_language.lstrip())
print(favourite_language.rstrip())
print(favourite_language.strip())
favourite_language = favourite_language.strip()
print(favourite_language)

#be careful when using quotes inside quotes

dennis_quote = 'Dennis Ritchie once said, "I am not now, nor have I ever been, a member of the demigodic party."'
print(dennis_quote)
name = "Dennis Ritchie"
quote = '"I am not now, nor have I ever been, a member of the demigodic party."'
print(name + ' once said, ' + quote)

print(2+3)
print(3**2)
print(9**9)
print(2**4086)
# print(4/0)
print(10%3)
print(10/3)
print(10*0.1)
print(0.2+0.1)

age = 23
# message = "Happy " + age + "rd birthday!" gives an error as age is not a string
# print(message)

message = "Happy " + str(age) + "rd birthday!"
print(message)

print(2/3)
print(3/2)

googol = 10**100
print("Google derived from googol whose value is " + str(googol))

import this
