
# stack creation
stack1 = ["H", "B", "V", "W", "N", "M", "L", "P"]
stack2 = ["M", "Q", "H"]
stack3 = ["N", "D", "B", "G", "F", "Q", "M", "L"]
stack4 = ["Z", "T", "F", "Q", "M", "W", "G"]
stack5 = ["M", "T", "H", "P"]
stack6 = ["C", "B", "M", "J", "D", "H", "G", "T"]
stack7 = ["M", "N", "B", "F", "V", "R"]
stack8 = ["P", "L", "H", "M", "R", "G", "S"]
stack9 = ["P", "D", "B", "C", "N"]


def move_stacks(link):
# read input page


# itterate through input
    for line in lines:
        line = line.split()
        if line[0] == "move":
            for val in range(0,int(line[1])):
                stacka = f"stack{line[3]}"         # ref external veriables??
                stackb = f"stack{line[5]}"
                stackb = stackb.append(stacka.pop())      # still pop from external variable?
# return answer
    return stack1[-1] + stack2[-1] + stack3[-1] + stack4[-1] + stack5[-1] + stack6[-1] + stack7[-1] + stack8[-1] + stack9[-1]