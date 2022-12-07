def sum_calories(arr: list):
    sum = 0
    for item in arr:
        sum += item
    return sum

file = open("input.txt")

all_calories = []
calories = []

for l in file.readlines():
    line = l.strip()
    if line != "":
        calories.append(int(line))
    else:
        all_calories.append(sum_calories(calories))
        calories = []

# sort in descending order
all_calories.sort(reverse=True)

print("part 1:",all_calories[0])

# get sum of first three items
print("part 2", sum(all_calories[:3]))