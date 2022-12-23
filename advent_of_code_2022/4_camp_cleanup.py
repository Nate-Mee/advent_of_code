#Read input into list
input = open("4_section_input.txt").read().split()

#Break down into lists to parce
elf1 = []
elf2 = []
for line in input: 
    nums = (line.split(","))
    elf1.append(nums[0].split("-"))
    elf2.append(nums[1].split("-"))

#part 1
#Count pairs when one contains the other
count = 0
elf1b = []
elf2b = []
for index, value in enumerate(elf1):
    if (int(value[0]) <= int(elf2[index][0]) and int(value[1]) >= int(elf2[index][1])) or (
        int(value[0]) >= int(elf2[index][0]) and int(value[1]) <= int(elf2[index][1])):
        count += 1
    else:
        elf1b.append(value)
        elf2b.append(elf2[index])

#Print answer
print(f"Number of sections where one range contains the other: {count}")

#part 2
#Count pairs when they overlap
for index, value in enumerate(elf1b):
    sections =  list(range(int(value[0]), int(value[1])+1))
    if int(elf2b[index][0]) in sections or int(elf2b[index][1]) in sections:
        count += 1

#Print answer
print(f"Number of sections where one range overlaps the other: {count}")