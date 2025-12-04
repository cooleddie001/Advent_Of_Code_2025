from utils import get_input

def get_repeating_ids(n1: int, n2: int, minimum: int, maximum: int):
    repeating_ids = []
    for i in range(n1, n2 + 1):
        x = str(i)
        repeating = x

        while len(repeating) <= len(str(maximum)):
            repeating_num = int(repeating)

            if repeating_num > maximum:
                break
            elif repeating_num >= max(minimum, 10):
                repeating_ids.append(repeating_num)

            repeating += x

    return repeating_ids

def get_all_repeating_combos(minimum: int, maximum: int):
    n1 = str(minimum)
    n2 = str(maximum)

    half_length_remove = len(n2) // 2
    n1 = n1[:-half_length_remove] or "1"
    n2 = n2[:-half_length_remove] or "1"

    all_repeating_ids = []
    while len(n2) > 0:
        print(n1, n2, minimum, maximum)

        all_repeating_ids.extend(get_repeating_ids(int(n1 or "1"), int(n2), minimum, maximum))

        n1 = n1[:-1]
        n2 = n2[:-1]
    return all_repeating_ids

def get_sum_of_repeating_combos(range: str):
    parts = range.split("-")
    all_repeating_ids = get_all_repeating_combos(int(parts[0]), int(parts[1]))
    return all_repeating_ids

input = get_input(__file__)
ranges = input.split(",")

all_r = []
summation = 0
for r in ranges:
    all_r.extend(get_sum_of_repeating_combos(r))

print(sum(set(all_r)))