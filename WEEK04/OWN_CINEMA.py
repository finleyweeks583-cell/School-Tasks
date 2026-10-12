age = int(input("How old are you? "))
student = input("Are you a student y/n: ")
member = input("Are you a member y/n: ")

PRICE = 12.00

if student == "y":
    PRICE = PRICE - 2.00
elif age < 16:
    PRICE = PRICE - 4.00
elif age > 65:
    PRICE = PRICE - 3.00

if member == "y":
    PRICE = PRICE - 1.50
elif member == "n":
    print("You are not a member")

print(f"Ticket price: £{PRICE:.2f}")