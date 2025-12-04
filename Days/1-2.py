from utils import get_input

input = get_input(__file__)
movements = input.split("\n")

pointer = 50
last_pointer = 0
password = 0
for movement in movements:
    dir = movement[0] == "R" #true if right, false if left
    if dir:
        dir = 1
    else:
        dir = -1

    steps = int(movement[1:])

    for step in range(steps): #can be more efficent, but would be less readable and harder to modify later.
        pointer = (pointer + dir) % 100
        if pointer == 0:
            password += 1

print(password)

