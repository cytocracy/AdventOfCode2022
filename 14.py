with open('input/14.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

rock_coords = []

highest = 0
for line in content:
    coords = line.split(' -> ')
    for coord in coords:
        point = coord.split(',')
        x = int(point[0])
        y = int(point[1])
        if y > highest:
            highest = y

print(highest)
def on_ground(x, y):
    return y == 172
        
for line in content:
    points = line.split(' -> ')
    point = points[0].split(',')
    points.pop(0)
    while points:
        point2 = points[0].split(',')
        points.pop(0)
        x1 = int(point[0])
        y1 = int(point[1])
        x2 = int(point2[0])
        y2 = int(point2[1])
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                rock_coords.append((x1, y))
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                rock_coords.append((x, y1))
        point = point2

def simulate():
    sand = (500, 0)
    if sand in rock_coords:
        return False
    while 1:
        if sand[1] == 172:
            break
        if (sand[0], sand[1] + 1) not in rock_coords:
            sand = (sand[0], sand[1] + 1)
            continue
        elif (sand[0] - 1, sand[1]+1) not in rock_coords:
            sand = (sand[0] - 1, sand[1]+1)
            continue
        elif (sand[0] + 1, sand[1]+1) not in rock_coords:
            sand = (sand[0] + 1, sand[1]+1)
            continue
        break
    rock_coords.add(sand)
    return True
    
rock_coords = set(rock_coords)
counter = 0
while simulate():
    counter+= 1

print(counter)



        

