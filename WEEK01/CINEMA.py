age = int(input("How old are you? "))
member = input("Are you a member? (y/n) ")

price = 12.00
   
if age < 16:
      price = price - 4.00
elif age >= 65:
     price = price - 3.00
  
if member.strip().lower() == "y":
     price = price - 1.50

print(f"Ticket price: £{price:.2f}")