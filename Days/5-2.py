from utils import get_input
#i did a similar problem on a coding test, they denied me :(

input = get_input(__file__).split("\n\n")
ranges = input[0].split("\n")

graph_fun = {}

for r in ranges:
    parts = r.split("-")
    minimum = int(parts[0])
    maximum = int(parts[1]) + 1

    graph_fun[minimum] = graph_fun.get(minimum, 0) + 1
    graph_fun[maximum] = graph_fun.get(maximum, 0) -1

graph_fun = dict(sorted(graph_fun.items()))
print(graph_fun)

start = None
active = 0
total_valid_ids = 0
for num, is_start in graph_fun.items():
    if active == 0 and active + is_start > 0:
        start = num
    elif active > 0 and active + is_start <= 0:
        print(start, num)
        total_valid_ids += num - start
        start = None
    active += is_start
print(total_valid_ids)
