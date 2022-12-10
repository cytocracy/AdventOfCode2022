with open('input/10.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

strength = []
cycle = 0
x = 1
nums = []
board = []

for i in range(6):
    board.append([])
    for j in range(40):
        board[i].append(".")

for line in content:
    strength.append(x)
    if line != "noop":
        strength.append(x)
        num = int(line.split()[1])
        x += num
            
for i in range(6):
    for j in range(40):
        index = i*40 + j
        if strength[index] == j or (strength[index]+1 == j) or strength[index]-1 == j:
            board[i][j] = "#"

for i in range(6):
    for j in range(40):
        print(board[i][j], end="")
    print()
            
print(len(strength))
print(strength[19]*20 + strength[59]*60 + strength[99]*100 + strength[139]*140 + strength[179]*180 + strength[219]*220)