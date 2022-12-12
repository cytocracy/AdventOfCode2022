with open('input/12.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == 'S':
            start = (i,j)
        if content[i][j] == 'E':
            end = (i,j)

for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == 'S':
            content[i] = content[i][:j] + 'a' + content[i][j+1:]
            
        if content[i][j] == 'E':
            content[i] = content[i][:j] + 'z' + content[i][j+1:]
            
eleva = []
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == 'a':
            eleva.append((i,j))

order = 'abcdefghijklmnopqrstuvwxyz'

def get_neighbors(i, j): 
    neighbors = []
    letter = content[i][j]

    letter_index = order.index(letter)

    if i >= 0:
        neighbors.append((i-1,j))
    if i < len(content)-1:
        neighbors.append((i+1,j))
    if j >= 0:
        neighbors.append((i,j-1))
    if j < len(content[i])-1:
        neighbors.append((i,j+1))

    new = []
    for k in range(len(neighbors)):
        letter = content[neighbors[k][0]][neighbors[k][1]]
        index = order.index(letter)
        if index <= letter_index +1:
            new.append(neighbors[k])
    return new

def bfs(starts, end):
    queue = [x for x in starts]
    visited = [x for x in starts]
    parent = {} 
    for start in starts:
        parent[start] = None

    while queue:
        current = queue.pop(0)
        if current == end:
            path = []
            while current != None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        neighbors = get_neighbors(current[0], current[1])
        for neighbor in neighbors:
            if neighbor not in visited:
                parent[neighbor] = current
                queue.append(neighbor)
                visited.append(neighbor)
    return False

path = bfs(eleva, end)
print(path)
print(get_neighbors(2,3))
print(len(path)-1)
