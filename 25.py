with open('input/25.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

nummap = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2, 2: '2', 1: '1', 0: '0', -1: '-', -2: '='}

def to_base10(num): 
    total = 0
    for i in range(len(num)):
        total += nummap[num[i]] * 5 ** (len(num) - i - 1)
    return total

def dist(a,b):
    return abs(a-b)

def to_snafu(num):
    #get closest max to num
    length= get_length(num)
    
    snafu = ''
    s = 0
    for i in range(length, 0, -1):
        #range -2 to 2 that gets s cloest to num
        
        # print(s)
        best = 0
        for j in range(-2, 3):
            place = j* (5 ** (i-1))
            # print('str', j, place, s+ place)
            num1 = s + place
            num2 = s + (best * (5 ** (i-1)))
            if dist(num1, num) < dist(num2, num):
                best = j

        # print("best", best)
        s += best * (5 ** (i-1))
        
        snafu += nummap[best]
        
    return snafu



    

def get_max(length):
    pows = []
    for i in range(length):
        pows.append(5 ** i)
    
    return 2 * sum(pows)

def get_length(maxnum):
    length = 0
    m = 0
    while m < maxnum:
        m += (5 ** length) * 2
        length += 1
    return length




def sum_to_base10(list):
    total = 0
    for num in list:
        total += to_base10(num)
    return total

print(sum_to_base10(content))
# print(get_max(3))

# print(get_length(4890))

print(to_snafu(sum_to_base10(content)))

# print(get_max(6))
