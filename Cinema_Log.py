import time 
input_film = False 


with open ("bookings.txt", "r") as BOOKING_TXT:
    PRINT_FILMS = BOOKING_TXT.read()

films = []

for line in PRINT_FILMS.splitlines():
    parts = line.split(" - ")

    film = parts[0]
    tickets = parts[1]

    films.append((film, tickets))

films.sort()

time.sleep(0.25)

print("1 - Add new Film")
print("2 - View list")
print()

user_input = input("Please type your chosen option: ")
print()

if user_input == "1":
    time.sleep(0.25)
    print()
    while (not input_film):
        film_input = input("Enter title of film and type 'done' when finished: ")
        print()
        time.sleep(0.15)
        done_input = input(f"You have entered {film_input}, if this is correct enter 'done': ").upper()
        print()

        if done_input == "DONE":
            with open ("bookings.txt", "a") as BOOKING_TXT:
                BOOKING_TXT.write(film_input + " - ")
                input_film = True
        else:
            input_film = False

    ticket_input =  input("Enter how many tickets : ")
    print()
    with open ("bookings.txt", "a") as BOOKING_TXT:
        BOOKING_TXT.write(ticket_input + "\n")

elif user_input == "2":
    print(f"| {'film':<18} | {'tickets':<12} |")
    print()

else:
    print("That is not a valid option, Please try again!")
