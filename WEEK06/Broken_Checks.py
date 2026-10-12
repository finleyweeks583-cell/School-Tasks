pin = input("Staff PIN:")
while len(pin) !=4:
    print("Four characters.")
    break

date = input("Date as DD/MM: ")
while len(date) ==5:
    date = input("Date as DD/MM: ")