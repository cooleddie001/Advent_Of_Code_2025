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

    pointer += (steps * dir)
    pointer %= 100

    if pointer == 0:
        password += 1

print(password)

