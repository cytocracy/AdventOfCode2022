from copy import deepcopy

with open('input/17.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

shapes = ['line', 'cross', 'l', 'i', 'square']
coords = set()

t = 0

seen = set()

def get_shape():
    shape = shapes.pop(0)
    shapes.append(shape)
    return shape

dirs = [*(content[0])]

def get_dir(dir):
    if dir == '>':
        return (1, 0)
    elif dir == '<':
        return (-1, 0)
def get_piece(t, highesty):
    A = set()
    y = highesty + 4
    if t==0:
        return set([(2,y), (3,y), (4,y), (5,y)])
    elif t == 1:
        return set([(3, y+2), (2, y+1), (3,y+1), (4,y+1), (3,y)])
    elif t == 2:
        return set([(2, y), (3,y), (4,y), (4,y+1), (4,y+2)])
    elif t==3:
        return set([(2,y),(2,y+1),(2,y+2),(2,y+3)])
    elif t==4:
        return set([(2,y+1),(2,y),(3,y+1),(3,y)])
    else:
        assert False

def can_move(new_coords):
    for coord in new_coords:
        if coord[0] < 0 or coord[0] > 6 or coord[1] == 0:
            return False
    return not (sig(new_coords) & rock)

def move_left(rock_coords):
    if any([x == 0 for (x, y) in rock_coords]):
        return rock_coords
    return set([(x - 1, y) for (x, y) in rock_coords])

def move_right(rock_coords):
    if any([x == 6 for (x, y) in rock_coords]):
        return rock_coords
    return set([(x + 1, y) for (x, y) in rock_coords])

def move_down(rock_coords):
    return set([(x, y - 1) for (x, y) in rock_coords])
def move_up(rock_coords):
    return set([(x, y + 1) for (x, y) in rock_coords])

def sig(R):
    maxy = max([y for (x, y) in R])
    return frozenset([(x, maxy - y) for (x, y) in R if maxy-y <=50])

def show(R):
    maxY = max([y for (x,y) in R])
    for y in range(maxY,0,-1):
        row = ''
        for x in range(7):
            if (x,y) in R:
                row += '#'
            else:
                row += ' '
        print(row)

L = 1000000000000
top = 0
i = 0
rock = set([(x, -1) for x in range(7)])
seen = {}
added = 0
    
while t<L:
    piece = get_piece(t%5, top)
    while True:
        if dirs[i]=='<':
            piece = move_left(piece)
            if piece & rock:
                piece = move_right(piece)
        else:
            piece = move_right(piece)
            if piece & rock:
                piece = move_left(piece)
        i = (i+1)%len(dirs)
        piece = move_down(piece)
        if piece & rock:
            piece = move_up(piece)
            rock |= piece
            top = max([y for (x,y) in rock])

            key = (i, t%5, sig(rock))
            if key in seen and t>=2022:
                (oldt, oldy) = seen[key]
                dy = top-oldy
                dt = t-oldt
                amt = (L-t)//dt
                added += amt*dy
                t += amt*dt
                assert t<=L
            seen[key] = (t,top)
            
            break
    t += 1
print(top+added)
        





