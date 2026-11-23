f = open("stock.txt", "w")
f.write("fern,12\ncactus,5\nivy,0\n")
f.close()
 
f = open("stock.txt", "r")
lines = f.readlines()
f.close()
print(len(lines))
print(lines[0])
for line in lines:
    parts = line.strip().split(",")
    if int(parts[1]) == 0:
        print(parts[0], "has sold out")
print(lines[2] == "ivy,0")
