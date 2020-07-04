# Chapter 3: Lists

cameraBrands = ['Sony', 'Canon', 'GoPro', 'Nikon']
print(cameraBrands)
print(type(cameraBrands))

print(cameraBrands[0])
print(type(cameraBrands[0]))

print(cameraBrands[1])
print(cameraBrands[-1])
print(cameraBrands[-2])

print("My first camera brand was " + cameraBrands[-1])

cameraBrands[2] = 'Pentax'
print(cameraBrands)

cameraBrands.append('GoPro')
print(cameraBrands)

cameraBrands = []
cameraBrands.append('sony')
cameraBrands.append('canon')
cameraBrands.append('nikon')
cameraBrands.append('pentax')
print(cameraBrands)

cameraBrands.insert(0, 'gopro')
print(cameraBrands)

del cameraBrands[0]
print(cameraBrands)

cameraBrands.insert(0, 'gopro')
print(cameraBrands)
del(cameraBrands[0])
print(cameraBrands)

cameraBrands.insert(0, 'gopro')
print(cameraBrands)
classic = cameraBrands.pop()
print(classic)
print(cameraBrands)
print("A fine camera that I've never owned in my life: " + classic.title())

firstCamera = cameraBrands.pop(-1)
print("My first dslr brand is " + firstCamera.title())

print(cameraBrands)
cameraBrands.remove('gopro')
print(cameraBrands)

cameraBrands.append('gopro')
cameraBrands.insert(1,'gopro')
print(cameraBrands)

cameraBrands.remove('gopro')
print(cameraBrands)

cameraBrands.remove('gopro')
print(cameraBrands)

cameraBrands.append('sony')
cameraBrands.append('canon')
cameraBrands.append('nikon')
cameraBrands.append('pentax')
print(cameraBrands)

cameraBrands.sort()
print(cameraBrands)
cameraBrands.remove('canon')
cameraBrands.remove('sony')
print(cameraBrands)
cameraBrands.sort(reverse=True)
print(cameraBrands)

cameraBrands = []
cameraBrands.append('sony')
cameraBrands.append('canon')
cameraBrands.append('nikon')
cameraBrands.append('pentax')

print("Original list: " + str(cameraBrands))
print("Sorted list: " + str(sorted(cameraBrands)))
print("Sorted list in reverse order: " + str(sorted(cameraBrands, reverse=True)))
print("Original list again: " + str(cameraBrands))

cameraBrands.reverse()
print(cameraBrands)

print(len(cameraBrands))

placeToVisit = ['yosemite', 'vancouver', 'newfoundland', 'amazon', 'bali']
print("Places to visit, if possible: " + str(placeToVisit))
print("Places to visit, sorted: " + str(sorted(placeToVisit)))
print("Places to visit, if possible: " + str(placeToVisit))
print("Places to visit, sorted in reverse: " + str(sorted(placeToVisit, reverse=True)))
print("Places to visit, if possible, in reverse order: " + str(placeToVisit))
placeToVisit.reverse()
print("Places to visit, if possible, in reverse order: " + str(placeToVisit))
placeToVisit.reverse()
print("Places to visit, if possible, in original order: " + str(placeToVisit))
placeToVisit.sort()
print("Places to visit, if possible, alphabetically sorted: " + str(placeToVisit))
placeToVisit.sort(reverse=True)
print("Places to visit, if possible, alphabetically sorted in reverse: " + str(placeToVisit))
print("Number of places to visit: " + str(len(placeToVisit)))

emptyList = []
# print(emptyList[-1]) doesn't work as the list is empty. Otherwise, -1 should always work
