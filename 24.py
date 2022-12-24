with open('input/23.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

walls = set()
blizzards = set()

