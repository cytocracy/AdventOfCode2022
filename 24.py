with open('input/24.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

STAY = (0,0)

start = (0,1)

walls = set()
blizzards = set()
right_c = len(content[0])-1
bottom_r = len(content)-1

for r, line in enumerate(content):
    for c, char in enumerate(line):
        if char == '^':
            blizzards.add(((r,c), UP))
        elif char == 'v':
            blizzards.add(((r,c), DOWN))
        elif char == '<':
            blizzards.add(((r,c), LEFT))
        elif char == '>':
            blizzards.add(((r,c), RIGHT))

        elif char == '#':
            walls.add((r,c))


def neighbors(node):
    time = node[1] + 1

    
    if time in blizzards_cache:
        blizzards = blizzards_cache[time]
    else:
        blizzards = update_blizzards(time)
        blizzards_cache[time] = blizzards


    r,c = node[0]
    for dr,dc in [UP, DOWN, LEFT, RIGHT, STAY]:
        new = (r+dr, c+dc)
        if new == (0,1) or new == (bottom_r, right_c-1):
            yield (new, time)
        elif new[0] <= 0 or new[1] <= 0 or new[0] >= bottom_r or new[1] >= right_c:
            
            continue
        
        elif new not in [x[0] for x in blizzards]:
            assert new not in walls
            # print('yield', new)
            yield (new, time)


blizzards_cache = {}
blizzards_cache[0] = blizzards

def wrap(pos):
    r,c = pos
    if r == 0:
        return (bottom_r-1, c)
    elif r == bottom_r:
        return (1, c)
    elif c == 0:
        return (r, right_c-1)
    elif c == right_c:
        return (r, 1)
    assert False


def update_blizzards(time):
    new_blizzards = set()
    for pos, direction in blizzards:
        r,c = pos
        dr,dc = direction
        if direction == UP or direction == DOWN:
            newr = ((r-1) + (time * dr)) % (bottom_r-1) + 1
            new = (newr, c)
        elif direction == LEFT or direction == RIGHT:
            newc = ((c-1) + (time * dc)) % (right_c-1) + 1
            new = (r, newc)

        # new = (r+dr, c+dc)
        assert new not in walls
        # if new not in walls:
        #     new_blizzards.add((new, direction))
        # else:
        new_blizzards.add((new, direction))
    # print("returning new blizzards")

    return frozenset(new_blizzards)

def print_blizzards(time):
    if time >= len(blizzards_cache):
        blizzards_cache[time] = update_blizzards(time)
        # print(len(blizzards_cache[time]))

    for r in range(bottom_r+1):
        for c in range(right_c+1):
            if (r,c) in walls:
                print('#', end='')
            elif (r,c) in [x[0] for x in blizzards_cache[time]]:
                print('X', end='')
            else:
                print('.', end='')
        print()

def manhattan(pos1, pos2):
    r1,c1 = pos1
    r2,c2 = pos2
    return abs(r1-r2) + abs(c1-c2)

def bfs(start=(0,1), end=(bottom_r, right_c-1), time=0):
    SEEN = set()
    print("end", end)
    queue = [(start,time)]
    parent = {(start, time): None}
    visited = set((start,time))
    while queue:
        node = queue.pop(0)
        # if node[1] > 100:
        #     break
        # print(node)
        # print("pop")
        if node[0] == end:

            curr = node
            path = []
            while curr != None:
                path.append(curr)
                curr = parent[curr]
            return path[::-1]
    

        for neighbor in neighbors(node):
            if neighbor not in visited:
                # if manhattan(neighbor[0], end) > 75 and neighbor[1] - time > 100:
                #     continue
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

        # queue = sorted(queue, key=lambda x: x[1])
        # queue = sorted(queue, key=lambda x: manhattan(x[0], end))


# print(len(walls))
# path = bfs()
# print(path)
firststep = 249
print(firststep)
path2 = bfs((bottom_r, right_c-1), (0,1), firststep)
# print(path2)
secondstep = len(path2)-1
print(secondstep)
path3 = bfs(time=firststep+secondstep)
thirdstep = len(path3)-1
print(thirdstep)

print(firststep+secondstep+thirdstep)