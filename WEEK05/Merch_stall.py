TSHIRT = 15
HOODIE = 30
DISCOUNT_FROM = 50

tshirts = int(input("How many t-shirts? "))
hoodies = int(input("How many hoodies? "))

total = tshirts * TSHIRT + hoodies * HOODIE

if total >= DISCOUNT_FROM:
    total = total - 5

print("Total:", total)