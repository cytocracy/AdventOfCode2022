with open('input/18.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

coords = set()
for line in content:
    nums = line.split(',')
    x = int(nums[0])
    y = int(nums[1])
    z = int(nums[2])
    coords.add((x, y, z))

surface = 0
surfacecoords = set()

maxx = max([x[0] for x in coords])
maxy = max([x[1] for x in coords])
maxz = max([x[2] for x in coords])

minx = min([x[0] for x in coords])
miny = min([x[1] for x in coords])
minz = min([x[2] for x in coords])

def get_neighbors(air):
    neighbors = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if abs(dx) + abs(dy) + abs(dz) > 1:
                    continue
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                if (air[0] + dx, air[1] + dy, air[2] + dz) in coords:
                    continue
                neighbors.append((air[0] + dx, air[1] + dy, air[2] + dz))
    return neighbors

def is_pocket(coord):
    if bfs(coord, (maxx+1, maxy+1, maxz+1)) == None:
        return True
    return False

dp = {}
def bfs(startair, endair):
    queue = [startair]
    visited = [startair]
    parent = {startair: None}

    while queue:
        current = queue.pop(0)
        if current == endair:
            path = []
            while current != None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                parent[neighbor] = current

        queue.sort(key=lambda x: get_distance(x, endair))
    return None

def get_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]) + abs(coord1[2] - coord2[2])

def get_coords(surface=0):

    counter = 0
    for coord in coords:
        counter += 1
        print(counter)
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    # print("new coord")
                    if abs(dx) + abs(dy) + abs(dz) > 1:
                        continue
                    if dx == 0 and dy == 0 and dz == 0:
                        continue
                    if (coord[0] + dx, coord[1] + dy, coord[2] + dz) in coords:
                        continue
                    if is_pocket((coord[0] + dx, coord[1] + dy, coord[2] + dz)):
                        continue
                    surface += 1

                    surfacecoords.add((coord[0] + dx, coord[1] + dy, coord[2] + dz))

    return surface

surface = get_coords()
print(surface)