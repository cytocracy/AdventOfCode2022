with open('input/21.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

namedict = {}
for line in content:
    name, val = line.split(': ')
    namedict[name] = val

def find_n(str, expected):
    val = namedict[str]
    if str == 'humn':
        return expected
    

    name1 = val.split(' ')[0]
    name2 = val.split(' ')[2]
    operator = val.split(' ')[1]
    if contains_humn(name1):
        if operator == '+':
            newexpect = expected - get_val(name2)
            return find_n(name1, newexpect)
        elif operator == '*':
            newexpect = expected / get_val(name2)
            return find_n(name1, newexpect)
        elif operator == '-':
            newexpect = expected + get_val(name2)
            return find_n(name1, newexpect)
        elif operator == '/':
            newexpect = expected * get_val(name2)
            return find_n(name1, newexpect)
    else:
        if operator == '+':
            newexpect = expected - get_val(name1)
            return find_n(name2, newexpect)
        elif operator == '*':
            newexpect = expected / get_val(name1)
            return find_n(name2, newexpect)
        elif operator == '-':
            newexpect = get_val(name1) - expected
            return find_n(name2, newexpect)
        elif operator == '/':
            newexpect = get_val(name1) / expected
            return find_n(name2, newexpect)



def get_val(str):
    val = namedict[str]
    if val.isdigit():
        return int(val)
    else:
        name1 = val.split(' ')[0]
        name2 = val.split(' ')[2]
        operator = val.split(' ')[1]
        if operator == '+':
            return get_val(name1) + get_val(name2)
        elif operator == '*':
            return get_val(name1) * get_val(name2)
        elif operator == '-':
            return get_val(name1) - get_val(name2)
        elif operator == '/':
            return get_val(name1) / get_val(name2)

print(namedict['root'])



def contains_humn(str):
    val = namedict[str]
    
    
    if str == 'humn':
        return True
    else:
        if val.isdigit():
            return False
        name1 = val.split(' ')[0]
        name2 = val.split(' ')[2]
        return contains_humn(name1) or contains_humn(name2)



#rjmz should be 51928434600306

# print(contains_humn('pppw'))
print(get_val('nfct'))

print(find_n('rjmz', 51928434600306))



# print(get_val('root'))