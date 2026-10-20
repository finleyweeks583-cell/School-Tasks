def abbrev_name(name):

    split_names = name.split()

    first_name = split_names[0]
    last_name = split_names[1]

    first_initial = first_name[0]
    last_initial = last_name[0]

    return(f"{first_initial}.{last_initial}").upper()