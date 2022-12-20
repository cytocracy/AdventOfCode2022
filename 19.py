from copy import deepcopy
from collections import deque

with open('input/19.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

blueprints = []

for line in content:
    nums = [int(s) for s in line.split() if s.isdigit()]
    blueprints.append(nums)

def get_max(cost_ore, cost_clay, cost_obs1, cost_obs2, cost_geo1, cost_geo2, time):

    best = 0
    
    start_state = (0,0,0,0,1,0,0,0,time)

    queue = deque([start_state])
    dp = set()
    while queue:
        state = queue.popleft()

        ore,cl,ob,g,r1,r2,r3,r4,t = state
        best = max(best, g)
        if t == 0:
            continue  
        
        max_core = max([cost_ore, cost_clay, cost_obs1, cost_geo1])

        if r1 >= max_core:
            r1 = max_core
        if r2 >= cost_obs2:
            r2 = cost_obs2
        if r3 >= cost_geo2:
            r3 = cost_geo2
        if ore >= t*max_core-r1*(t-1):
            ore = t*max_core-r1*(t-1)
        if cl >= t*cost_obs2-r2*(t-1):
            cl = t*cost_obs2-r2*(t-1)
        if ob >= t*cost_geo2-r3*(t-1):
            ob = t*cost_geo2-r3*(t-1)

        state = (ore,cl,ob,g,r1,r2,r3,r4,t)

        if state in dp:
            continue
        dp.add(state)

        queue.append((ore + r1, cl + r2, ob + r3, g + r4, r1, r2, r3, r4, t-1))

        if ore>= cost_ore:
            queue.append((ore - cost_ore+r1, cl + r2, ob + r3, g + r4, r1+1, r2, r3, r4, t-1))
        if ore>= cost_clay:
            queue.append((ore - cost_clay+r1, cl + r2, ob + r3, g + r4, r1, r2+1, r3, r4, t-1))
        if ore>= cost_obs1 and cl>= cost_obs2:
            queue.append((ore - cost_obs1+r1, cl-cost_obs2 + r2, ob + r3, g + r4, r1, r2, r3+1, r4, t-1))
        if ore>= cost_geo1 and ob>= cost_geo2:
            queue.append((ore - cost_geo1+r1, cl + r2, ob - cost_geo2 + r3, g + r4, r1, r2, r3, r4+1, t-1))    
    return best

total = 0
counter = 0
total2 = 1
for blueprint in blueprints:
    counter += 1
    if counter == 4:
        break
    num = get_max(blueprint[0], blueprint[1], blueprint[2], blueprint[3], blueprint[4], blueprint[5], 32)
    total2 *= num

print(total2)

