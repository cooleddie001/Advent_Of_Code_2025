from utils import get_input

batteries = get_input(__file__).split("\n")

def get_highest_digit_recur(battery: str, start_at: int = 0, length_remaining=2) -> int:
    if length_remaining <= 0:
        return 0

    major = 0
    major_index = 0
    #print(len(battery), length_remaining)

    for i in range(start_at, len(battery) - length_remaining + 1):  # first loop to determine tens place
        volt = battery[i]

        if int(volt) > major:
            major = int(volt)
            major_index = i

    return (major * 10**(length_remaining - 1)) + get_highest_digit_recur(battery, major_index + 1, length_remaining - 1)

def get_highest_voltage(battery: str) -> int:
    return get_highest_digit_recur(battery, 0, 12)



summation = 0
for battery in batteries:
    print(get_highest_voltage(battery))
    summation += get_highest_voltage(battery)

print(summation)