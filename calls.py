with open("the_calls.txt") as file:
    array = [[element for element in row.strip().split() ] for row in file]
    array.sort(key=lambda x: (x[2], -int(x[1])))
    for i in array:
        print(i)
file.close()
