with open('input/5.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

stackstring = content[:10]
moves = content[10:]

print(content[0])

stacks = []
for i in range(0, 9):
    stacks.append([])

for i in range(0, 7):
    line = content[7-i]
    
    if len(line) == 35:
        letters = line[1] + line[5] + line[9] + line[13] + line[17] + line[21] + line[25] + line[29] + line[33]
    if len(line) == 27:
        letters = "  " + line[1] + line[5] + line[9] + line[13] + line[17] + line[21] + line[25]

    for j in range(0, 9):
        stacks[j].append(letters[j])


for i in range(0, 9):
    while stacks[i][-1] == " ":
        stacks[i].pop()

#Because I SUCK and my ass had to HARD CODE IT bc the last row DIDNT READ and my fucking STACKS KEPT BEING EMPTY
stacks[3].append("L")
stacks[4].append("M")
stacks[7].append("M")

for i in range(0, 9):
    print(stacks[i])

for move in moves:
    nums = move.split()
    first = int(nums[1])
    second = int(nums[3])
    third = int(nums[5])
    # print(first, second, third)
    
    letters = []
    for i in range(0, first):
        letters.append(stacks[second-1].pop())
        
    letters = letters[::-1] 
    for letter in letters:
        stacks[third-1].append(letter)


letters = ""
for i in range(0, 9):
    letters += stacks[i][-1]

print(stacks)
print(letters)