with open('input/8.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

def is_visible(i, j):
    num = int(content[i][j])
    if i == 0 or i == len(content) - 1 or j == 0 or j == len(content[i]) - 1:
        return True
    top = True
    for k in range(0, i):
        if int(content[k][j]) >= num:
            top = False
    bottom = True
    for k in range(i + 1, len(content)):
        if int(content[k][j]) >= num:
            bottom = False
    left = True
    for k in range(0, j):
        if int(content[i][k]) >= num:
            left = False
    right = True
    for k in range(j + 1, len(content[i])):
        if int(content[i][k]) >= num:
            right = False

    if top or bottom or left or right:
        return True
    else:
        return False

def find_viewing_score(i, j):
    num = int(content[i][j])
    if i == 0 or i == len(content) - 1 or j == 0 or j == len(content[i]) - 1:
        return 0
    sum1 = 0
    for k in range(0, i):
        sum1 += 1
        if int(content[i-k-1][j]) >= num:
            break
        
    sum2 = 0
    for k in range(i + 1, len(content)):
        sum2 += 1
        if int(content[k][j]) >= num:
            break
    sum3 = 0
    for k in range(0, j):
        sum3 += 1
        if int(content[i][j-k-1]) >= num:
            break
        
    sum4 = 0
    for k in range(j + 1, len(content[i])):
        sum4 += 1
        if int(content[i][k]) >= num:
            break
        
    return sum1 * sum2 * sum3 * sum4

maxnum = None
total = 0
for i in range(0, len(content)):
    for j in range(0, len(content[i])):
        if is_visible(i, j):
            total += 1
        num = find_viewing_score(i, j)
        if maxnum == None or num > maxnum:
            maxnum = num

print(total)
print(maxnum)