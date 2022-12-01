data = []

max = [0,0,0]
curr = 0

inp = input()

while inp != "end":
    
    if inp == '':
        data.append(0)
    else:
        data.append(int(inp))
    inp = input()

def updateMax(curr, max):
    i = 2
    if curr > max[1]:
        i-=1
    if curr > max[0]:
        i-=1
    max.insert(i, curr)
    max.pop()


for i in range(len(data)):
    if data[i] == 0 or data[i] == None:
        if curr > max[2]:
            updateMax(curr, max)
        curr = 0
    else:
        curr += data[i]
        



    




print(max[0] + max[1] + max[2])
    