#Python Crash Course

print("Hello world! \nLet's learn some Python!\n")

#DELCARE VARIABLES
print("VARIABLE DECLARATIONS:\n")

#Use random casing for practice with methods such as .lower() 
firstName = "toMmY"
lastName = "gRabOWskI"

print("\tfirstName: " + firstName)
print("\tlastName: " + lastName)

#Create 'space' variable for whitespace
space = " "
age = 21

#Set 'age' type to a string so it can be used in concatenation
age = str(age)

print("\tspace: " + space + "(one space key press)")
print("\tage: " + age)

#CONCATENATION
print("\nCONCATENATION:\n")

#Set fullName by concatenating firstName, space, & lastName
fullName = (firstName + space + lastName)
print("\tfullName: " + fullName)

#METHODS
print("\nMETHODS:\n")

#Set fullName to have all lowercase letters
fullName = fullName.lower()
print("\tfullName.lower(): " + fullName)

#Set fullName to capitalize the first letters
fullName = fullName.title()
print("\tfullName.title(): " + fullName)

#Concatenation and methods can all be done with one line:
fullName = (firstName + space + lastName).lower().title()


print("\nCONCATENATION + METHODS ON ONE LINE:\n")
print("\tfullName: " + fullName)

#COMBINE EVERYTHING

print("\nCOMBINE EVERYTHING:\n")
#Set message to concatenate strings and variables
message = "\tMessage: " + fullName + " is " + age + " years old."

print(message)
