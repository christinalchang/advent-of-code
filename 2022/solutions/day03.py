import string

# read input
with open('../inputs/day03_input.txt') as f:
    lines = f.read().splitlines()

# --- Part One ---

# create priority dict
lower = dict(zip(string.ascii_lowercase, range(1, 27)))
upper = dict(zip(string.ascii_uppercase, range(27, 53)))
priorities = {**lower, **upper}

# split and find shared item
res = []
for i in lines:
    a, b = i[:len(i)//2], i[len(i)//2:]
    share = list(set(a) & set(b))[0]
    res.append(priorities[share])

print(sum(res))

# --- Part Two ---

res = []
group = []
for i in range(len(lines)):
    # start a list for each group
    group.append(lines[i])

    # if divisible by 3 find common item and start a new list
    if ((i+1) % 3) == 0:
        # common item
        share = list(set.intersection(*map(set, group)))[0]
        res.append(priorities[share])

        # reset the group
        group = []

print(sum(res))
