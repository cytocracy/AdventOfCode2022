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
    #     return False
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
possible = set()

def get_tuning():
    counter = 0
    possible = set()

    for sensor in sensors:
        counter += 1
        print("new sensor: " + str(counter))    
        x = sensor.x
        y = sensor.y
        closex = sensor.closex
        closey = sensor.closey

        
        distance = get_distance(x, y, closex, closey)
        neededdistance = distance + 1
        for nx in range(x - neededdistance, x + neededdistance+1):
            if(0 <= nx <= 4000000):
                distanceleft = neededdistance - get_distance(x, y, nx, y)
                y1 = y - distanceleft
                y2 = y + distanceleft
                if 0 <= y1 <= 4000000:
                    possible.add((nx,y1))
                if 0 <= y2 <= 4000000:
                    possible.add((nx,y2))
                    
    print("len: " + str(len(possible)))
    for coord in possible:
        if can_exist(coord[0], coord[1]):
            print(coord)
            return(coord[0] * 4000000 + coord[1])

                
               

# count = 0
# for notcoord in notcoords:
#     if notcoord[1] == 2000000:
#         print(count)
#         count += 1

print(get_tuning())


