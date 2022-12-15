#open input
input = open("2_rps_input.txt", "r")

#part 1
# #create count and lookup dict
# total_score = 0
# lookup = {"A":1, "B":2,"C":3, "X":1, "Y":2, "Z":3}

# #itterate through games
# for line in input:
#     line.split()
#     elf = lookup[line[0]]
#     me = lookup[line[2]]

# #win lose or draw
#     if (elf == 3 or me == 3) and (elf == 1 or me == 1):
#         if line[0] + line[2] == "AZ":
#             total_score += me
#         else:
#             total_score += me + 6
#     elif elf < me:
#         total_score += me + 6
#     elif elf == me:
#         total_score += me + 3
#     else:
#         total_score += me

# #print total score
# print(total_score)

#part 2
#create count and lookup dicts
total_score = 0
lookup = {"A":1, "B":2,"C":3}
win_lookup = {"A":"B", "B":"C", "C":"A"}
lose_lookup = {"A":"C", "B":"A", "C":"B"}

#itterate through games
for line in input:
    line.split()
    elf = line[0]
    wld = line[2]

    #win
    if wld == "Z":
        me = win_lookup[elf]
        total_score += lookup[me] + 6
    #draw
    elif wld == "Y":
        total_score += lookup[elf] + 3
    #lose
    else:
        me = lose_lookup[elf]
        total_score += lookup[me]

#print total score
print(total_score)