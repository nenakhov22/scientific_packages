with open("input.txt") as file:
    array = [[element for element in row.strip().split() ] for row in file]
    array.sort(key=lambda x: x[1])
    name = array[0][1]
    pol = array[0][2]
    pair = 0
    countAnimal = [0]
    nameAnimal = [name]
    for i in array:
        if name==i[1]:
            countAnimal[len(nameAnimal)-1] += 1
            if pol!=i[2] and pair == 0:
                pair = 1
                print(name)
        if name!=i[1]:
            pair = 0
            name = i[1]
            type = i[2]
            nameAnimal.append(name)
            countAnimal.append(1)
    for i in range(len(nameAnimal)):
        print(nameAnimal[i] + " -" + str(countAnimal[i]))
file.close()

# file = open('input.txt', '+r')
# animals = []
# animal_spicies = []
# n = 0
#
# for line in file:
#     print(line)
#
# print()
#
# for line in file:
#     animals.append(line.split(' '))
#     n+=1
#
# for i in range(n-1):
#     for j in range(i+1, n):
#         if (animals[i][1] == animals[j][1] and animals[i][2] != animals[j][2]):
#           animal_spicies.append(animals[i][1])
#
# animal_spicies = set(animal_spicies)
# print(animal_spicies)
#
#
# print()
# file.close()
