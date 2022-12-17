from copy import deepcopy

with open('input/16.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

class Node:
    def __init__(self, name, value, children):
        self.name = name
        self.value = value
        self.children = children
    
nodes = []
namedict = {}
DP = {}

for line in content:
    name = line.split()[1]
    value = line.split('=')[1].split(';')[0]
    children = []
    if 'valves' in line:
        children = line.split('valves ')[1].split(', ')
    else:
        children = [line.split('tunnel leads to valve ')[1]]
    namedict[name] = Node(name, value, children)

def getNonZeroNodes():
    nonZeroNodes = []
    for node in namedict:
        if namedict[node].value != '0':
            nonZeroNodes.append(node)
            
    return nonZeroNodes

def get_neighbors(name):
    return namedict[name].children

def findPath(n1, n2):
    queue = [n1]
    visited = [n1]
    parent = {n1: None}

    while queue:
        current = queue.pop(0)
        if current == n2:
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
    
paths = []
allpaths = []

for node in nodes:
    for node2 in nodes:
        if node != node2:
            allpaths.append(findPath(node, node2))
a_paths = []
is_open = {}
simvalues = {}

for node in getNonZeroNodes():
    is_open[node] = False

for node in getNonZeroNodes():
    a_paths.append(findPath('AA', node))
    for node2 in getNonZeroNodes():
        if node != node2:
            paths.append(findPath(node, node2))


def simulate(curr, timeLeft, is_open):
        
    if curr == 'AA':
        vals = []
        for path in a_paths:
            if not is_open[path[-1]]:
                newtime = timeLeft - (len(path)-1) -1
                if newtime < 1:
                    continue
                temp_is_open = deepcopy(is_open)
                temp_is_open[path[-1]] = True
                simval = simulate(path[-1], timeLeft - (len(path)-1)-1, temp_is_open)
                simnum = int(simval[0]) + int(namedict[path[-1]].value) * newtime
                vals.append((simnum, simval[1] + [path[-1]]))
                print([path[-1]] + simval[1])

        if len(vals) == 0:
            return (0, [])
        return max(vals, key=lambda x: x[0])

    possible = []
    for path in paths:
        if path[0] == curr:
            nextvalve = path[-1]
            if not is_open[nextvalve]:
                value = namedict[nextvalve].value
                newtime = timeLeft - (len(path)-1) - 1
                if newtime < 1:
                    continue
                addedval = int(newtime) * int(value)
                temp_is_open = deepcopy(is_open)
                temp_is_open[nextvalve] = True
                simval = simulate(nextvalve, newtime, temp_is_open)
                possibleval = simval[0] + addedval
                possiblepath = [nextvalve] + simval[1]
                possible.append((possibleval, possiblepath))

    
    if len(possible) == 0:
        return (0, [])
    return max(possible, key=lambda x: x[0])

def make_tuple(curr, timeLeft, is_open):
    return (curr, timeLeft, is_open)
    
def sim_all(curr, timeLeft, is_open):

    if timeLeft < 2:
        return [(0, [])]
    usize = ""
    for node in is_open:
        if is_open[node]:
            usize += "1"
        else:
            usize += "0"
    
    key = hash(curr) * hash(timeLeft) * hash(usize)
    # print(key)
    # 
    # key = hash(curr + str(timeLeft) + str(usize))
    if key in DP:
        return DP[key]
        # pass
    possible = []
    
    for neighbor in get_neighbors(curr):
        nextvalve = neighbor
        
        value = namedict[nextvalve].value
        if value != '0' and not is_open[nextvalve]:
            newtime = timeLeft - 2
            if newtime < 1:
                continue
            addedval = int(newtime) * int(value)
        
            temp_is_open = deepcopy(is_open)
            temp_is_open[nextvalve] = True
        else:
            newtime = timeLeft - 1
            if newtime < 1:
                continue
            addedval = 0
            temp_is_open = deepcopy(is_open)
        
        simval = sim_all(nextvalve, newtime, temp_is_open)
        for sim in simval:
            possibleval = sim[0] + addedval
            possiblepath = [nextvalve] + sim[1]
            
            possible.append((possibleval, possiblepath))
            # print("newposs")

    DP[key] = possible
    print(len(possible))
    return possible

def sim_both(curr, timeLeft, is_open):
    vals = []
    firstsims = sim_all(curr, timeLeft, is_open)
    print(len(firstsims))
    for sim in firstsims:
        print("newsim")
        second_is_open = deepcopy(is_open)
        for node in sim[1]:
            second_is_open[node] = True
        secondsims = sim_all(curr, timeLeft, second_is_open)
        vals.append(sim[0] + max(secondsims, key=lambda x: x[0])[0])
    return max(vals)



print(simulate('AA', 30, is_open))