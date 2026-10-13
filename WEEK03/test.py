def simple_multiplication():
    number_one = int(input("Please enter a number: "))
    if  number_one % 2 == 0:
        output = number_one * 8
    else:
        output = number_one * 9

    print(output)

simple_multiplication()