import pyfiglet

LOCATION_THREE = "THE CABIN IN THE WOODS"

ENTER_CABIN = (pyfiglet.figlet_format(F"ENTERING {LOCATION_THREE} ! ", font = 'DOOM'))
print("\033[33m" + ENTER_CABIN + "\033[0m")