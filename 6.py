with open('input/6.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

string = ""
for line in content:
    string += line

sum = 0
for line in content:

    for i in range(len(string)):
        print(string[i:i+14])
        if len(set(string[i:i+14])) == 14:
            print(string[i:i+14])
            print(i)
            break
        else :
            sum += 1

print(sum + 14) 