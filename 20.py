with open('input/20.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

nums = []

for i, line in enumerate(content):
    nums.append((i, int(line) * 811589153))


og = [x[1] for x in nums]


def move(nums, og):
    
    for i, line in enumerate(og):
        num = int(line)
        search = (i, num)

        idx = nums.index(search)

        temp = nums[:idx] + nums[idx+1:]
        newidx = (idx+num) % len(temp)
        if newidx == 0:
            temp.append(search)
        else:
            temp.insert(newidx, search)

        nums = temp

    return nums
        
for i in range(10):
    nums = move(nums, og)

for addidx, x in enumerate(nums):
    if x[1] == 0:
        break

print(addidx)

total = 0
total += nums[(addidx+1000) % len(nums)][1]
total += nums[(addidx+2000) % len(nums)][1]
total += nums[(addidx+3000) % len(nums)][1]

print(total)
