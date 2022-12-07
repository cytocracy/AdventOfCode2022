with open('input/7.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

def get_size(index):
    sum = 0
    index = index + 1
    sign = content[index].split()[0]
    counter = 0
    while True:
        if sign == "$":
            if content[index].split()[1] == "cd":
                if content[index].split()[2] == "..":
                    counter -= 1 
                else:
                    counter += 1
            if counter < 0:
                break
        elif content[index].split()[0] != "dir":
            sum += int(content[index].split()[0])
        index = index + 1
        if index >= len(content):
            break
        sign = content[index].split()[0]
    
    return sum

maxsize = 70000000
totsize = get_size(1)
unused = maxsize-totsize
champ = None

total = 0
for i in range(len(content)):
    if content[i].split()[0] == "$":
        if content[i].split()[1] == "ls":
            print("getting size of " + str(i))
            size = get_size(i)
            print(size)
            if unused + size >= 30000000:
                if champ is None or size <= champ:
                    champ = size

print(champ)
