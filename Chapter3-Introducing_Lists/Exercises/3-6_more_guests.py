# Exercise 3-6: More Guests
# Tasks:
# 1: Start with the program from 3-5
# 2: Add a print statement at the end of the program informing people
#    that you have found a bigger dinner table
# 3: Modify the list, replacing the name of the guest who can't make it
#    with the name of the new person you are inviting
# 4: Print a second set of invitation messages, one for each person who is
#    still in the list

guests = ["robby", "bobby", "sarah", "stephen", "daniel"]

guests.insert(0, 'ragina')
guests.insert(6//2, 'rachel')
guests.append('johnny')

message = "Hello " + guests[0].title() + ", I am writing to you because I would like to " \
                                         "invite you to dinner. Please RSVP."
print(message)

message = "Hello " + guests[1].title() + ", I am writing to you because I would like to " \
                                         "invite you to dinner. Please RSVP."
print(message)

message = "Hello " + guests[2].title() + ", I am writing to you because I would like to " \
                                         "invite you to dinner. Please RSVP."
print(message)

message = "Hello " + guests[3].title() + ", I am writing to you because I would like to " \
                                         "invite you to dinner. Please RSVP."
print(message)

message = "Hello " + guests[4].title() + ", I am writing to you because I would like to " \
                                         "invite you to dinner. Please RSVP."
print(message)

message = "Hello " + guests[5].title() + ", I am writing to you because I would like to " \
                                         "invite you to dinner. Please RSVP."
print(message)

message = "Hello " + guests[6].title() + ", I am writing to you because I would like to " \
                                         "invite you to dinner. Please RSVP."
print(message)

message = "Hello " + guests[7].title() + ", I am writing to you because I would like to " \
                                         "invite you to dinner. Please RSVP.\n"
print(message)

message = "Hello " + guests[0].title() + ", I have found a bigger dinner table."
print(message)

message = "Hello " + guests[1].title() + ", I have found a bigger dinner table."
print(message)

message = "Hello " + guests[2].title() + ", I have found a bigger dinner table."
print(message)

message = "Hello " + guests[3].title() + ", I have found a bigger dinner table."
print(message)

message = "Hello " + guests[4].title() + ", I have found a bigger dinner table."
print(message)

message = "Hello " + guests[5].title() + ", I have found a bigger dinner table."
print(message)

message = "Hello " + guests[6].title() + ", I have found a bigger dinner table."
print(message)

message = "Hello " + guests[7].title() + ", I have found a bigger dinner table.\n"
print(message)