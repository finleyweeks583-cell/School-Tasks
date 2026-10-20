import time 

valid_input = False
valid_input_2 = False
GAME_RESET = False  

MONEY = 10
HEALTH = 100

LOCATION_ONE = "Dark Forest"
LOCATION_TWO = "PLACEHOLDER2"
LOCATION_THREE = "PLACEHOLDER3"
LOCATION_FOUR = "PLACEHOLDER4"

while (not GAME_RESET):
    print()
    PLAYER_NAME = input("Please enter your characters name: ")
    print()

    time.sleep(1)
    print(f"Welcome to the game {PLAYER_NAME}")
    print()

    time.sleep(1.25)
    print("You wake up in what seems to be a dark cell of somekind, the door is lightly ajar what will you do?")

    time.sleep(2)
    print()
    CELL_OPTION_ONE = print("Option A - Walk over to the door and leave")
    print()
    CELL_OPTION_TWO = print("Option B - Search around the small cell")

    while (not valid_input):
        print()
        user_input_cell = input("Chose your option: ").strip().upper()
        print()

        if user_input_cell == "A":
            valid_input = True
            GAME_RESET = True
            print("You exit the cell and infrot of you lays a dark dirt path surrounded by tall trees with only the faint shine of moonlight throught the thick leaves")
            print()
            print(f"Entering the {LOCATION_ONE}")
            time.sleep(3)

       

        elif user_input_cell == "B":
            valid_input = True 
            print("After looking around the cell you notice a cabnet, After opening the cabnet you are presented with 2 bottles")
            print()
            time.sleep(1.5)
        
            while (not valid_input_2):
                potion_input = input("What bottle will you pick, 1 or 2: ").strip().upper()
                print()
            
                if potion_input == "1":
                    valid_input_2 = True 
                    print("That was poision.......")
                    print()
                    time.sleep(2)
                    print("You Died")
                    time.sleep(0.5)
                    print("Try again")
                    time.sleep(0.5)
                    GAME_RESET = False
                
            
                elif potion_input == "2":
                    GAME_RESET = True
                    valid_input_2 = True
                    print("That was water, nothing happens")
                    print()
                    time.sleep(0.5)
                    print("After drinking the water you exit the cell and infrot of you lays a dark dirt path surrounded by tall trees with only the faint shine of moonlight throught the thick leaves")
                    print()
                    print(f"Entering the {LOCATION_ONE}")
                    time.sleep(3)
                    

                else:
                    GAME_RESET = True
                    print("That is not a valid option, please try again")
                    print()
                    valid_input_2 = False
                
        else:
            GAME_REST = True
            print("That is not a valid option, Please try again")
            valid_input = False