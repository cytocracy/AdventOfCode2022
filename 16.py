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

for line in content:
    name = line.split()[1]
    value = line.split('=')[1].split(';')[0]
    children = []
    #Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
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
            newtime = timeLeft - (len(path)-1) -1
            if newtime < 1:
                continue
            temp_is_open = deepcopy(is_open)
            temp_is_open[path[-1]] = True
            simval = simulate(path[-1], timeLeft - (len(path)-1)-1, temp_is_open)
            simnum = int(simval[0]) + int(namedict[path[-1]].value) * newtime
            vals.append((simnum, simval[1] + [path[-1]]))
            print([path[-1]] + simval[1])

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

print (simulate('AA', 30, is_open))