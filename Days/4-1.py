from utils import get_input
rows = get_input(__file__).split("\n")
new_rows = rows.copy()
new_rows = [list(row) for row in rows]

eligible_rolls = 0
for y, row in enumerate(rows):
    for x, element in enumerate(row):
        if element == ".":
            continue

        borders = 0
        for x1 in range(x-1, x+2):
            for y1 in range(y-1, y+2):
                if x1 == x and y1 == y:
                    continue

                if x1 < 0 or y1 < 0 or y1 >= len(row) or x1 >= len(row):
                    continue

                elif rows[y1][x1] == "@":
                    borders += 1

        if borders < 4:
            eligible_rolls += 1
            new_rows[y][x] = "x"


print("\n".join("".join(row) for row in new_rows))
print(eligible_rolls)