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