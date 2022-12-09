with open('input/9.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

#create list of 10 list of coords
coords = [[(0, 0)] for i in range(10)]
print(coords)


headcoords = [(0, 0)]
tailcoords = [(0, 0)]

head = (0, 0)
tail = (0, 0)


for line in content:
    direction = line[0]
    length = int(line[1:])
    print(direction, length)

    for i in range(length):


        if direction == 'R':
            head = (head[0] + 1, head[1])
            coords[0].append(head)
        elif direction == 'L':
            head = (head[0] - 1, head[1])
            coords[0].append(head)
        elif direction == 'U':
            head = (head[0], head[1] + 1)
            coords[0].append(head)
        elif direction == 'D':
            head = (head[0], head[1] - 1)
            coords[0].append(head)

        for j in range(1,10):
            dy = coords[j-1][-1][1] - coords[j][-1][1]
            dx = coords[j-1][-1][0] - coords[j][-1][0]

            tail = coords[j][-1]

            if dy == 2:
                tail = (coords[j][-1][0], coords[j][-1][1] + 1)
                if dx != 0:
                    xc = 0
                    if dx > 0:
                        xc = 1
                    else:
                        xc = -1
                    tail = (tail[0] + xc, tail[1])
            elif dy == -2:
                tail = (coords[j][-1][0], coords[j][-1][1] - 1)
                if dx != 0:
                    xc = 0
                    if dx > 0:
                        xc = 1
                    else:
                        xc = -1
                    tail = (tail[0] + xc, tail[1])
            
            elif dx == 2:
                tail = (coords[j][-1][0] + 1, coords[j][-1][1])
                if dy != 0:
                    yc = 0
                    if dy > 0:
                        yc = 1
                    else:
                        yc = -1
                    tail = (tail[0], tail[1] + yc)
            elif dx == -2:
                tail = (coords[j][-1][0] - 1, coords[j][-1][1])
                if dy != 0:
                    yc = 0
                    if dy > 0:
                        yc = 1
                    else:
                        yc = -1
                    tail = (tail[0], tail[1] + yc)

            


            coords[j].append(tail)


            
        
        
    print(coords[9][-1])


        #find coord of tail
        # dy = head[1] - tail[1]
        # dx = head[0] - tail[0]

        # if dy == 2:
            
        #     tail = (tail[0], tail[1] + 1)
        
        #     if dx == 1 or dx == -1:
        #         tail = (tail[0] + dx, tail[1])

        #     tailcoords.append(tail)

        # elif dy == -2:
        #     tail = (tail[0], tail[1] - 1)
        #     if dx == 1 or dx == -1:
        #         tail = (tail[0] + dx, tail[1])
        #     tailcoords.append(tail)

        # elif dx == 2:
        #     tail = (tail[0] + 1, tail[1])
        #     if dy == 1 or dy == -1:
        #         tail = (tail[0], tail[1] + dy)
        #     tailcoords.append(tail)
        
        # elif dx == -2:
        #     tail = (tail[0] - 1, tail[1])
        #     if dy == 1 or dy == -1:
        #         tail = (tail[0], tail[1] + dy)
        #     tailcoords.append(tail)


finalcoords = []

for i in coords[9]:
    if i not in finalcoords:
        finalcoords.append(i)


print(len(finalcoords))

            







