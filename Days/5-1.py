from utils import get_input

input = get_input(__file__).split("\n\n")
ranges = input[0].split("\n")
available = input[1].split("\n") #seems to always be sorted

def validate_to_range(minimum: int, maximum: int) -> int:
    valid = 0
    for a in available.copy(): #prevent skipping
        a = int(a)
        if a >= minimum and a <= maximum:
            valid += 1
            available.remove(str(a)) #no duplicates counted

    return valid

valid = 0
for r in ranges:
    parts = r.split("-")
    valid += validate_to_range(int(parts[0]), int(parts[1]))

print(valid)
print(available)