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

print("Press '1' for Cereal Bar   ")
print("Press '2' for Crisps       ")
print("Press '3' for Chocolate Bar")
print("Press '4' for Bottled Water")

print()

input("Please input your chosen number ")

if input == "1":
    item = "Cereal Bar"
    price = CEREAL_BAR

elif input == "2":
    item = "Crisps"
    price = CRISPS

elif input == "3":
    item = "Chocolate Bar"
    price = CHOCOLATE_BAR

elif input == "4":
    item = "Bottled Water"
    price = BOTTLED_WATER

coins = input("Please insert coins £")

if coins == price:
    print("Thank you for your purchase")

elif coins < price:
    print("Not enough Coins")
