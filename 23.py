with open('input/23.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

directions = [(-1,0), (1,0), (0,-1), (0,1)]



elves = set()

for r, line in enumerate(content):
    for c, char in enumerate(line):
        if char == '#':
            elves.add((r,c))




def get_neighbors(r, c):
    neighbors = []
    for dx in range(-1,2):
        for dy in range(-1,2):
            if dx == 0 and dy == 0:
                continue
            neighbors.append((r+dx, c+dy))
    return neighbors

def get_north_neighbors(r, c):
    dy = -1
    neighbors = []
    for dx in range(-1,2):
        neighbors.append((r+dy, c+dx))

    return neighbors

def get_south_neighbors(r, c):
    dy = 1
    neighbors = []
    for dx in range(-1,2):
        neighbors.append((r+dy, c+dx))

    return neighbors

def get_east_neighbors(r, c):
    dx = 1
    neighbors = []
    for dy in range(-1,2):
        neighbors.append((r+dy, c+dx))

    return neighbors

def get_west_neighbors(r, c):
    dx = -1
    neighbors = []
    for dy in range(-1,2):
        neighbors.append((r+dy, c+dx))

    return neighbors

def get_bounds(elves):
    # print(len(elves))
    minx = min([x[0] for x in elves])
    maxx = max([x[0] for x in elves])
    miny = min([x[1] for x in elves])
    maxy = max([x[1] for x in elves])
    print(minx, maxx, miny, maxy)
    return minx, maxx, miny, maxy

def get_num_empty(elves, bounds):
    minx, maxx, miny, maxy = bounds
    empty = 0
    for r in range(minx, maxx+1):
        for c in range(miny, maxy+1):
            if (r,c) not in elves:
                empty += 1
    return empty

proposed = {}

# def print(elves):
#     minx, maxx, miny, maxy = get_bounds(elves)
#     for r in range(minx, maxx+1):
#         for c in range(miny, maxy+1):
#             if (r,c) in elves:
#                 print('#', end='')
#             else:
#                 print('.', end='')
#         print()

def print_elves(elves):
    minx, maxx, miny, maxy = get_bounds(elves)
    for r in range(minx, maxx+1):
        for c in range(miny, maxy+1):
            if (r,c) in elves:
                print('#', end='')
            else:
                print('.', end='')
        print()


def run(elves):

    for i in range(1000):
        proposed = {}
        # print(directions)
        
        newcoords = set()
        print(i+1)
        for elf in elves:
            neighbors = get_neighbors(*elf)
            if any([n in elves for n in neighbors]):
                # newcoords.add(elf)
                
                for i in range(4):
                    direction = directions[i]
                    if direction == (1,0):
                        neighbors = get_south_neighbors(*elf)
                        if not any([n in elves for n in neighbors]):
                            proposed[elf] = (elf[0]+direction[0], elf[1]+direction[1])
                            break
                    elif direction == (-1,0):
                        neighbors = get_north_neighbors(*elf)
                        if not any([n in elves for n in neighbors]):
                            proposed[elf] = (elf[0]+direction[0], elf[1]+direction[1])
                            break
                    elif direction == (0,1):
                        neighbors = get_east_neighbors(*elf)
                        if not any([n in elves for n in neighbors]):
                            # if elf == (0,1):
                                # print('east')
                            proposed[elf] = (elf[0]+direction[0], elf[1]+direction[1])
                            break
                    elif direction == (0,-1):
                        neighbors = get_west_neighbors(*elf)
                        if not any([n in elves for n in neighbors]):
                            proposed[elf] = (elf[0]+direction[0], elf[1]+direction[1])
                            break
            # if elf == (0,1):
            #     print(elf, proposed[elf])
            
        # newcoords = set()
        moved = False
        for elf in elves:
            newloc = elf
            if elf in proposed:
                # print('proposed', elf, proposed[elf])
                length = len([x for x in proposed if proposed[x] == proposed[elf]])
                # print(length)
                if length == 1:
                    # print('yay')
                    moved = True
                    newloc = proposed[elf]
                
            newcoords.add(newloc)
        if not moved:
            print(i+1)
            break
        # i += 1

        elves = newcoords
        directions.append(directions.pop(0))
        # print(len(elves))
        # print_elves(elves)

    return elves

# print(len(elves))
elves = run(elves)
# print(len(elves))
print(get_num_empty(elves, get_bounds(elves)))
        


            
