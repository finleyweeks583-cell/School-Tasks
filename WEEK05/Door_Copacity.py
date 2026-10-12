CAPACITY = 250

sold = int(input("Tickets sold so far: "))
waiting = int(input("People waiting at the door: "))

space = CAPACITY - sold

if space == 0:
    print("Venue full")
else:
    if waiting <= space:
        print("Let them all in")
    else:
        print("Let in", space)
        print("Turn away", waiting - space)        