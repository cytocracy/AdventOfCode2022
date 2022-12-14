import ast
from copy import deepcopy
import json
import functools

with open('input/13.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

nums = []


sortednums = []




for line in content:
    if len(line) == 0:
        continue
    x = json.loads(line)
    nums.append(x)
    
newnums = deepcopy(nums)
    


def compare(a, b):
    if len(a) == 0 and len(b) != 0:
        return True
    if len(b) == 0 and len(a) != 0:
        return False

    if len(a) == 0 and len(b) == 0:
        return -1

    first = a[0]
    second = b[0]

    if type(first) == int and type(second) != int:
        first = [first]
        return compare(first, second)
    if type(first) != int and type(second) == int:
        second = [second]
        return compare(first, second)

    if type(first) == int and type(second) == int:
        # print("here")
        if first > second:
            return False
        if first < second:
            return True
        # return compare(a[1:], b[1:])

         
    if type(first) == list and type(second) == list:
        val = compare(first, second)
        if val == -1:
            return compare(a[1:], b[1:])
        return val
        # return compare(a[1:], b[1:])


    return compare(a[1:], b[1:])
    
    

total = 0
for i in range(0, len(nums), 2):
    left = nums[i]
    right = nums[i+1]
    # print(left)
    # print(right)
    # print(compare(left, right))
    if compare(left, right):
        total += (i/2+1)


def comparehelper(a,b):
    if compare(a,b):
        return -1
    return 1


nums.append([[2]])
nums.append([[6]])
nums.sort(key=functools.cmp_to_key(comparehelper))
for num in nums:
    print(num)
print((nums.index([[2]])+1) * (nums.index([[6]])+1))

print(total)