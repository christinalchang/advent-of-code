
# read input
with open('../inputs/day01_input.txt') as f:
    lines = f.read().splitlines()

calories = []
calories_sum = 0

# calorie sums
for i in lines:
    if i == '':
        calories.append(calories_sum)
        calories_sum = 0
    else:
        calories_sum = calories_sum + int(i)

# max calories carried by elf
print(max(calories))

# sum of calories carried by top 3 elfs
print(sum(sorted(calories)[-3:]))
