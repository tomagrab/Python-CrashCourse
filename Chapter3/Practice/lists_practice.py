#Python Crash Course

#General information
header = "Python Crash Course"
chapter = "Chapter 3: Introducing lists"
title = header + "\n" + chapter + "\n"

print(title)

#DECLARE VARIABLES

#Whitespace variables
space = " "
tab = "\t"
newLine = "\n"

#CREATING A LIST

#Create a list of dog names
dogs = ["barron", "mickey", "murphy", "dennis"]
print(dogs)

#ACCESSING LIST ITEMS

#List items have an index
#The first item in a list starts with [0]
#The last item in a list can be accessed by [-1]
#Examples:
#"barron" is dogs[0]
#"dennis" is dogs[3] OR dogs[-1]
myFirstDog = dogs[0]
print(tab + myFirstDog)

#Concatenate list item with strings
message = tab + "My first dog was named " + dogs[0].title() + "."
print(message)

#INSERT ITEMS INTO A LIST

dogs.insert(0, "benny")
print(dogs)

#REMOVE ITEMS FROM A LIST

#Using the del method
del dogs[1]
print(dogs)

#Using the pop() method
#pop() removes the last item from a list
#but allows you to use that item
last_dog = dogs.pop()
print(dogs)
print(tab + "Last dog: " + last_dog.title())

#Use pop() to remove any item
first_dog = dogs.pop(0)
print(tab + "First dog: " + first_dog.title())


#Remove list item by value
dogs.remove("mickey")
print(dogs)

#Use value removed by remove()
removed_dog = "murphy"
dogs.remove(removed_dog)
print(dogs)
print(tab + removed_dog.title() + " has been removed.")
