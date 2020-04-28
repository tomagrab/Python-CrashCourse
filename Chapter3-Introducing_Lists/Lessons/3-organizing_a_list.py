# Lesson 3: Organizing a List

# Sorting a list permanently with the sort() method
# sort() will organize the list alphabetically by default

tab = "\t"
newline = "\n"
space = " "

title = "Lesson 3: Organizing a list"
subtitle = "Sorting a list permanently with the sort() method"

print(title + newline + newline + subtitle + newline)

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

cars.sort()

print("\nHere is the list with the sort() method:")
print(cars)

# Organize the list in reverse alphabetical order:

print("\nOrganize the list in reverse alphabetical order")

cars.sort(reverse=True)

print("\nHere is the list with sort() set to reverse:")
print(cars)

# Sorting a list temporarily with the sorted() method

print("\nSorting a list temporarily with the sorted() method")

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the list with the sorted() method:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Printing a list in reverse order

print("\nPrinting a list in reverse order with the reverse() method")

print("\nHere is the original list:")
print(cars)

print("\nHere is the list with the reverse() method:")
cars.reverse()
print(cars)

# Finding the length of a list

print("\nFind the length of a list using the len() method:")

cars_length = len(cars)
cars_length = str(cars_length)

message = "The length of the 'cars' list is " + cars_length
print(message)