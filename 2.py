with open('input/rpc.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

sum = 0

for line in content:
    first = line.split(' ')[0]
    second = line.split(' ')[1]
    if second == "X":
        if first == "A":
            sum +=3
        if first == "B":
            sum +=1
        if first == "C":
            sum += 2
        
    elif second == "Y":
        sum += 3  
        if first == "A":
            sum += 1
        elif first == "B":
            sum += 2
        elif first == "C":
            sum += 3
    elif second == "Z":
        sum += 6
        if first == "A":
            sum += 2
        elif first == "B":
            sum += 3
        elif first == "C":
            sum += 1
print (sum)

