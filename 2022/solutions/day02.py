# read input
with open('../inputs/day02_input.txt') as f:
    lines = f.read().splitlines()

# --- Part One ---

# outcomes
outcome_scores = {'loss': 0,
                  'draw': 3,
                  'win': 6}

# remap responses to numbers; A/B/C is opponent, X/Y/Z is myself
translate_dict = {'A': '1', 'X': '1',  # rock
                  'B': '2', 'Y': '2',  # paper
                  'C': '3', 'Z': '3'}  # scissor
lines_translate = [i.translate(str.maketrans(translate_dict)) for i in lines]

res = []
for line in lines_translate:
    score = 0

    #  split response string and compute score
    opp, me = map(int, line.split(' '))
    if opp == me:
        res_score = outcome_scores['draw']
    elif (opp == 1) & (me == 2):
        res_score = outcome_scores['win']
    elif (opp == 1) & (me == 3):
        res_score = outcome_scores['loss']
    elif (opp == 2) & (me == 1):
        res_score = outcome_scores['loss']
    elif (opp == 2) & (me == 3):
        res_score = outcome_scores['win']
    elif (opp == 3) & (me == 1):
        res_score = outcome_scores['win']
    else:
        res_score = outcome_scores['loss']

    # append round score
    res.append(res_score + me)

total_score = sum(res)
print(total_score)

# --- Part Two ---

# outcomes
outcome_scores = {1: 0,  # lose
                  2: 3,  # draw
                  3: 6}  # win

res = []
for line in lines_translate:
    me = 0

    #  split response string and compute score
    opp, end_res = map(int, line.split(' '))
    if end_res == 2:
        me = opp
    elif end_res == 1:  # lose
        if opp == 1:
            me = 3
        elif opp == 2:
            me = 1
        else:
            me = 2
    else:  # win
        if opp == 1:
            me = 2
        elif opp == 2:
            me = 3
        else:
            me = 1

    # append round score
    res.append(outcome_scores[end_res] + me)

total_score = sum(res)
print(total_score)
