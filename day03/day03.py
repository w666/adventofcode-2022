import re

file = open("input.txt")

lower_case_shift = 96
upper_case_shift = 38

sum = 0

file = open("input.txt")


def get_prio(item):
    if re.match("[A-Z]", item) != None:
        return ord(item)-upper_case_shift
    else:
        return ord(item)-lower_case_shift


for l in file.readlines():
    line = l.strip()
    mid = int(len(line)/2)
    r1 = line[:mid]
    r2 = line[mid:]

    shared_items = set(r1).intersection(set(r2))

    if (len(shared_items) > 0):
        for item in shared_items:
            sum += get_prio(item)

print("part1:", sum)


sum = 0

file = open("input.txt")
lines = file.readlines()
groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

for arr in groups:
    shared_items = set(arr[0].strip()).intersection(
        set(arr[1].strip())).intersection(set(arr[2].strip()))
    for item in shared_items:
        sum += get_prio(item)

print("part2:", sum)