age = int(input("How old are you? "))
member = input("Are you a member y/n: ")

PRICE = 12.00

if age < 16:
    PRICE = PRICE - 4.00
elif age > 65:
    PRICE = PRICE - 3.00

if member == "y":
    PRICE = PRICE - 1.50
elif member == "n":
    print("You are not a member")

print(f"Ticket price: £{PRICE:.2f}")