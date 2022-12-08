shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

LOST = "lost"
DRAW = "draw"
WON = "won"


table_part1 = {
    "A": {
        "Z": LOST,
        "X": DRAW,
        "Y": WON
    },
    "B": {
        "X": LOST,
        "Y": DRAW,
        "Z": WON
    },
    "C": {
        "Y": LOST,
        "Z": DRAW,
        "X": WON
    }
}

round_score = {
    LOST: 0,
    DRAW: 3,
    WON: 6
}

file = open("input.txt")

sum = 0

for l in file.readlines():
    their, me = l.strip().split(" ")
    sum += shape_score[me] + round_score[table_part1[their][me]]

print("part1:", sum)

table_part2 = {
    "X": LOST,
    "Y": DRAW,
    "Z": WON
}

def get_shape_part2(target, their):
    for key, value in table_part1[their].items():
        if value == target:
            return key

file = open("input.txt")

sum2 = 0

for l in file.readlines():
    their, me = l.strip().split(" ")
    sum2 += shape_score[get_shape_part2(table_part2[me], their)] + round_score[table_part2[me]]

print("part2:", sum2)