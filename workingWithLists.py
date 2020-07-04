# Chapter 4: Working with Lists
# for loop

dogs = ['newfie', 'doberman', 'bernese', 'dane', 'retriever', 'pug']
for dog in dogs:
    print(dog)

print("\n")

for dog in dogs:
    print("Me: Who is a good boy?\n" + dog.title() + ": Me!\n")

print("This is not repeated as it isn't part of the loop above")

# range function

for value in range(26, 51):
    print(value)

numbers = list(range(1, 26))
print(numbers)

# print even numbers
numbers = list(range(2, 51, 2))
print(numbers)

# squares of numbers
squares = []
for value in range(2, 51, 2):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,26):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,26):
    squares.append(value**2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))
print(sorted(squares, reverse=True))

# list comprehension

squares = [value**2 for value in range(1,26)]
print(squares)

evenNums = [value for value in range(2,26,2)]
print(evenNums)

oddNums = [value for value in range(1,26,2)]
print(oddNums)

#exercise
numList = []
for value in range(1,21):
    numList.append(value)
print(numList)

million = []
for value in range(1,1000001):
    million.append(value)
# print(million)
print(min(million))
print(max(million))
print(sum(million))

numList = []
for value in range(1,21,2):
    numList.append(value)
print(numList)

numList = []
for value in range(3,31,3):
    numList.append(value)
print(numList)

numList = [value*3 for value in range(1,11)]
print(numList)


# Slicing Lists
dogs = ['newfie', 'doberman', 'bernese', 'dane', 'retriever', 'pug']
print(dogs[0:3]) #first 3
print(dogs[1:4]) #three starting with second
print(dogs[:3]) #first 3
print(dogs[:4]) #first 4
print(dogs[2:]) #All but first 2
print(million[999990:]) #All but first 999990
print(million[-10:]) #Same as above, can be interpreted as last 10

# looping through slices
print("First 3 dogs: ")
for dog in dogs[:3]:
    print(dog.title())

# copying a List

copyDogs = dogs[:]
print("Original dogs: ")
print(dogs)
print("Copy dogs: ")
print(copyDogs)
copyDogs.append('greyhound')
print("Copy dogs with a new dog: ")
print(copyDogs)
print("Original dogs: ")
print(dogs)

# reference to the original dogs
refDogs = dogs
print(refDogs)
print(id(dogs))
print(id(refDogs))

refDogs.append('hotdog')
print(dogs)

# immutable list: Tuple
# immutable meaning: unchanging over time or unable to be changed.

liberty = (40.6891316, -74.0463653)
print(liberty)
print(type(liberty))

print(liberty[0])
print(liberty[1])
# liberty[0] = 40.6891315 doesn't work, as tuple is immutable

tenFibSeq = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)
print("Original Fibonacci sequence: ")
for fib in tenFibSeq:
    print(fib)

# Tuples are immutable but they are replaceable
tenFibSeq = (55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181)
print("Modified Fibonacci sequence: ")
for fib in tenFibSeq:
    print(fib)
