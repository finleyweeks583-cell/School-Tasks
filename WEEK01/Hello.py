name = input("What is your first name? ")
year = input("What  year were you born? ")
town = input("What town are you from? ")

age = 2029 - int(year)
cyear = 2026
time = 2029 - int(cyear)

print(f"{name}, you are from {town} and turn {age} in 2029, that is {time} years away")