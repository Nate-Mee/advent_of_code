#open input
input = open("3_rucksack_input.txt") 

#create letter value lookup
letters = []
let_val = {}
count = 1
for num in range(65, 123):
    letters.append(chr(num))
del letters[26:32]
for num in range(26, len(letters)):
    let_val[letters[num]] = count
    count += 1
for num in range(0, 26):
    let_val[letters[num]] = count
    count += 1

#split out two parts of rucksack
ruck1 = []
ruck2 = []
for line in input:
    line = line.strip()
    ruck1.append(line[:len(line) // 2])
    ruck2.append(line[len(line) // 2:])

#find duplicate value for each rucksack
duplicates = [] 
count2 = 0
for string in ruck1:
    for let in string:
        if let in ruck2[count2]:
            duplicates.append(let)
            break
    count2 += 1

#check correct number of duplicates - instructions say 1 per rucksack
print("Correct number of duplicates." if len(duplicates) == len(ruck1) else "Incorrect number of duplicates.")

#sum duplicates
total = 0
for dup in duplicates: total += let_val[dup]

#print answer
print(total)