with open('input/15.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

class Sensor:
    def __init__(self, x, y, closex, closey):
        self.x = x
        self.y = y
        self.closex = closex
        self.closey = closey

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

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def can_exist(x, y):

    for sensor in sensors:
        distance = get_distance(sensor.x, sensor.y, x, y)
        if distance <= get_distance(sensor.x, sensor.y, sensor.closex, sensor.closey):
            return False
    return True
    
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

print(get_tuning())