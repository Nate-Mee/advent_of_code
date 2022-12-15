#open input
input = open("1_calorie_input.txt", "r")

#set up variables
elf_list = []
count = 0

#itterate through lines
for line in input:
    if line == "\n":
        elf_list.append(count)
        count = 0
    else:
        count += int(line)

#print largest value
print(max(elf_list))

#print sum of three largest values
elf_list.sort()
print(sum(elf_list[-3:]))
