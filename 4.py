with open('input/4.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

def contains(first, second):
    first = first.split('-')
    second = second.split('-')
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
        return True
    else:
        return False

def getnums(line):
    first = line.split('-')[0]
    second = line.split('-')[1]

    return range(int(first), int(second)+1)

def overlap(first, second):
    first = getnums(first)
    second = getnums(second)
    for i in first:
        if i in second:
            return True

sum = 0
for line in content:
    first = line.split(',')[0]
    second = line.split(',')[1]
    if overlap(first, second):
        sum += 1

print(sum)
        



