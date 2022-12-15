with open('input/15.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

#create sensor class
class Sensor:
    def __init__(self, x, y, closex, closey):
        self.x = x
        self.y = y
        self.closex = closex
        self.closey = closey


#create list of sensors
#Sensor at x=1363026, y=2928920: closest beacon is at x=1571469, y=3023534
sensors = []
for line in content:
    x = int(line.split(',')[0].split('=')[1])
    y = int(line.split(':')[0].split('=')[2])
    closex = int(line.split(':')[1].split(',')[0].split('=')[1])
    closey = int(line.split(':')[1].split(',')[1].split('=')[1])
    
    sensors.append(Sensor(x, y, closex, closey))

coords = set()
beacons = set()

for sensor in sensors:
    print (sensor.x, sensor.y, sensor.closex, sensor.closey)
    coords.add((sensor.x, sensor.y))
    beacons.add((sensor.closex, sensor.closey))


notcoords = set()
# for sensor in sensors:
#     distance = abs(sensor.x - sensor.closex) + abs(sensor.y - sensor.closey)
#     for x in range(sensor.x - distance + 1, sensor.x + distance):
#         distanceleft = distance - x
#         for y in range(sensor.y - distanceleft + 1, sensor.y + distance):
#             if (x, y) not in coords:
#                 print(x, y)
#                 notcoords.add((x, y))

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def can_exist(x, y):
    # if  (x, y) in beacons:
    #     return True
    for sensor in sensors:
        distance = get_distance(sensor.x, sensor.y, x, y)
        if distance <= get_distance(sensor.x, sensor.y, sensor.closex, sensor.closey):
            return False
    return True


print("here")
#count number of notcords where y == 2000000
# y = 2000000

# lowest = 0
# highest = 0
# for sensor in sensors:
#     if sensor.closex < lowest:
#         lowest = sensor.closex
#     if sensor.closex > highest:
#         highest = sensor.closex

#create list of sets of coords that can exist for each sensor
# for sensor in sensors:
possibles = []


for sensor in sensors:
    x = sensor.x
    y = sensor.y
    closex = sensor.closex
    closey = sensor.closey

    possible = set()

    dist = get_distance(x, y, closex, closey)
    for i in range(x - dist, x + dist + 1):
        tempy = y + dist - abs(x - i)
        if (0 <= i <= 4000000) and (0 <= tempy <= 4000000):
            possible.add((i, tempy))
        tempy = y - (dist - abs(x - i))
        if (0 <= i <= 4000000) and (0 <= tempy <= 4000000):
            possible.add((i, tempy))
    print(len(possible))
    possibles.append(possible)




def get_tuning():
    #return intersection of all sets
    for poss in possibles:
        for tup in poss:
            if can_exist(tup[0], tup[1]):
                return(tup[0] * 4000000 + tup[1])
        
    print()
            
               
# count = 0
# for notcoord in notcoords:
#     if notcoord[1] == 2000000:
#         print(count)
#         count += 1

print(get_tuning())


