#Read input into list
input = open("4_section_input.txt").read().split()

#Break down into lists to parce
elf1 = []
elf2 = []
for line in input: 
    nums = (line.split(","))
    elf1.append(nums[0].split("-"))
    elf2.append(nums[1].split("-"))

#Count pairs when one contains the other
count = 0
for index in range(0, len(elf1)):
    if int(elf1[index][0]) <= int(elf2[index][0]) and int(elf1[index][1]) >= int(elf2[index][1]):
        count+= 1
    elif int(elf1[index][0]) >= int(elf2[index][0]) and int(elf1[index][1]) <= int(elf2[index][1]):
        count+= 1

#Print answer
print(count)