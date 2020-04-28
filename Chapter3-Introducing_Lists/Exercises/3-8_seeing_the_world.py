# Exercise 3-8: Seeing the World
# Tasks:
# 1: Think of at least five places in the world you would like to visit
# 2: Store the locations in a list, not in alphabetical order
# 3: Print the list in its original order
# 4: Use sorted() to print your list in alphabetical order without modifying
#    the list
# 5: Show the list is in the original order by printing it
# 6: Use sorted() to print the list in reverse alphabetical order
# 7: Show the list is in the original order by printing it again
# 8: Use reverse() to change the order of the list
# 9: Print the list to show that the order has been changed
# 10: Use reverse() to change the order of the list again
# 11: Print the list to show it's back to its original order
# 12: Use sort() to change the order of the list to alphabetical
# 13: Print the list to show its order has changed
# 14: Use sort() to change the order of the list to reverse alphabetical
# 15: Print the list to show its order has changed

locations = ['hawaii', 'machu picchu', 'mexico', 'ireland', 'poland']

print("Original list:")
print(locations)

print("\nsorted() list:")
print(sorted(locations))

print("\nOriginal list:")
print(locations)

print("\nReversed sorted():")
print(sorted(locations, reverse=True))

print("\nOriginal list:")
print(locations)

print("\nreversed() list:")
locations.reverse()
print(locations)

print("\nSecond reversed() list:")
locations.reverse()
print(locations)

print("\nsort() list:")
locations.sort()
print(locations)

print("\n Reversed sort() list:")
locations.sort(reverse=True)
print(locations)