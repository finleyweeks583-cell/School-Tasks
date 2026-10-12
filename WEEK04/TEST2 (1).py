CEREAL_BAR = 0.50
CRISPS = 0.60
CHOCOLATE_BAR = 0.80
BOTTLED_WATER = 0.90

print("=========   Options   =========")
print("Cereal Bar     :        £0.50  ")                 
print("Crisps         :        £0.60  ") 
print("Chocolate Bar  :        £0.80  ")
print("Bottled Water  :        £0.90  ")
print("===============================")

print()

print("Press 'A' for Cereal Bar   ")
print()
print("Press 'B' for Crisps       ")
print()
print("Press 'C' for Chocolate Bar")
print()
print("Press 'D' for Bottled Water")

print()

input("Please input your chosen letter: ")

if input == "A":
    item = "Cereal Bar"
    price = CEREAL_BAR

elif input == "B":
    item = "Crisps"
    price = CRISPS

elif input == "C":
    item = "Chocolate Bar"
    price = CHOCOLATE_BAR

elif input == "D":
    item = "Bottled Water"
    price = BOTTLED_WATER

coins = float(input("Please incert your coins £  "))

if coins >= price:
    print("Thank you for your purchase")

elif coins < price:
    print("Not enough Coins")
