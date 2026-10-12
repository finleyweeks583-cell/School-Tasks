import time
total = 0 

print("Accepted coins 10p, 20p ,50p and £1")
print()
time.sleep(1.25)
while total < 0.60:
    coins = float(input("Please input coins £"))
    total = total + coins
    print(f"Your total is £{total:.2f}")


if total > 0.60:
    change = total - 0.60
    print(f"Your total is £{total:.2f} and your change is £{change:.2f}")
