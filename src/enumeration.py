animals = ["Dog", "Zebra", "Lion", "Cat", "Hyena"]

for index, animal in enumerate(animals):
    if index % 2 ==0:
        continue
    else:
        print(index+1, animal)