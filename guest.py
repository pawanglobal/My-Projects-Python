print("Oh I want to create a guest list to invite people to the party.")
print("It is a borint and tedious task to do.")
print("Let me write a python program for that which include the guests name to the guest.txt")

guest_name = input("Plese enter your name if you want to come to the party:\n")

filename = 'guest.txt'
with open(filename,'w') as object_file:
    object_file.write(f"Thank You {guest_name} for coming to the party.\n")

