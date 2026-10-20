import time

price = 0
payed = False

minutes = int(input("Please enter the total minutes "))
print()
docked = input("Has it been docked Y/N: ")
print()

if minutes <= 30:
    price = price + 0

elif minutes <= 60:
    price = price + 2

elif minutes <= 120:
    price = price + 4

elif minutes > 120:
    price = price + 7

if docked == "N":
    price = price + 5

if price <= 0:
    print("Thank you for using Bike Hire")

elif price > 0:
   while (not payed):
    print(f"Cost is £{price}")
    print()
    payment = int(input("Please input payment: £"))
    print()

    if payment == price:
        print("Authorising....")
        print()
        time.sleep(1)
        print("Authorising...")
        print()
        time.sleep(1)
        print("Authorising..")
        print()
        time.sleep(3)
        print("Payment accepted!")
        print()
        time.sleep(1.5)
        print("Thank you for using Bike Hire")
        print()
        payed = True
        # quit()

        if payment < price:
            print("Insufficent funds, Please try again")
            payed = False

    elif payment > price:
        change = payment - price
        print("Authorising....")
        print()
        time.sleep(1)
        print("Authorising...")
        print()
        time.sleep(1)
        print("Authorising..")
        print()
        time.sleep(3)
        print("Payment accepted!")
        print()
        time.sleep(1.5)
        print(f"Your change is £{change:.2f}")
        print()
        time.sleep(1.5)
        print("Thank you for using Bike Hire")
        payed = True