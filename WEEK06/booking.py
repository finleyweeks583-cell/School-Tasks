name = input("Your name: ")

if name == "":
    print("You must enter a name")
elif name.isdigit() == True:
    print("Name cannot contain numbers")

ref = input("Booking reference: ")

if len(ref) < 4 and len(ref) > 10:
    print("Booking reference must be at least 4 letters long and cannot be more than 10 letters long")

hours = input("Hours needed: ")

if hours.isdigit() == False:
    print("Digits only")
elif hours.isdigit < 1 or hours > 8:
    print("Hours cannot be less than 1 or more than 8")

print("Booked:", name, ref, hours)