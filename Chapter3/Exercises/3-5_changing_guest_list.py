# Exercise 3-5: Changing Guest List
# Tasks:
# 1: Start with the program from 3-4
# 2: Add a print statement at the end of the program stating the name of
#    the guest who can't make it
# 3: Modify the list, replacing the name of the guest who can't make it
#    with the name of the new person you are inviting
# 4: Print a second set of invitation messages, one for each person who is
#    still in the list

guests = ["robby", "bobby", "sarah", "stephen", "kelly"]

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


cannot_attend = guests.pop().title() + " is not able to come."

print(cannot_attend)
