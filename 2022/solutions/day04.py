
# read input
with open('../inputs/day04_input.txt') as f:
    lines = f.read().splitlines()

# --- Part One ---
overlap_count = 0
for i in lines:
    i_split = i.replace(',', '-').split('-')
    i_split = [int(i) for i in i_split]

    # make section ranges
    rng1 = set(range(i_split[0], i_split[1]+1))
    rng2 = set(range(i_split[2], i_split[3]+1))

    # check if one is completely contained in the other
    if (len(rng1 - rng2) == 0) | (len(rng2 - rng1) == 0):
        overlap_count += 1

print(overlap_count)

# --- Part Two ---
overlap_count = 0
for i in lines:
    i_split = i.replace(',', '-').split('-')
    i_split = [int(i) for i in i_split]

    # make section ranges
    rng1 = set(range(i_split[0], i_split[1]+1))
    rng2 = set(range(i_split[2], i_split[3]+1))

    # check if length of individual ranges equal length of union
    if len(rng1) + len(rng2) != len(rng1.union(rng2)):
        overlap_count += 1

print(overlap_count)
