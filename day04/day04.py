import numpy as np

def get_arrays():
    file = open("input.txt")
    arrays = []
    for l in file.readlines():
        line = l.strip()
        one, two = line.split(",")
        range_one = one.split("-")
        range_two = two.split("-")
        elf_1 = np.arange(int(range_one[0]), int(range_one[1]) + 1, 1)
        elf_2 = np.arange(int(range_two[0]), int(range_two[1]) + 1, 1)
        arrays.append([elf_1, elf_2])
    return arrays

arrays = get_arrays()
sum = 0
for elfs in arrays:
    if(set(elfs[0]).issubset(set(elfs[1])) or set(elfs[1]).issubset(set(elfs[0]))):
        sum += 1

print("part1:", sum)

sum = 0
for elfs in arrays:
    if(len(set(elfs[0]).intersection(set(elfs[1]))) > 0):
        sum += 1

print("part2:", sum)