with open('input/11.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

class Monkey:
    def __init__(self, worries, operation, test, tr, fl):
        self.worries = worries
        self.operation = operation
        self.test = test
        self.tr = tr
        self.fl = fl
        self.inspects = 0

    def __str__(self):
        return 'Monkey: ' + str(self.worries) + ' ' + self.operation + ' ' + self.test

monkeys = []

# Monkey 0:
#   Starting items: 99, 63, 76, 93, 54, 73
#   Operation: new = old * 11
#   Test: divisible by 2
#     If true: throw to monkey 7
#     If false: throw to monkey 1

for i in range(8):
    
    info = content[i*7:i*7+7]
    worries = info[1].split(': ')[1].split(', ')
    worries = [int(x) for x in worries]
    print(worries)
    operation = info[2].split(': ')[1]
    print(operation)
    test = info[3].split(': ')[1]
    tr = info[4].split(' ')[5]
    fl = info[5].split(' ')[5]
    m = Monkey(worries, operation, test, tr, fl)
    monkeys.append(m)


for i in range(10000):
    for monkey in monkeys:
        for worry in monkey.worries:
            
            expression = monkey.operation.split("= ")[1]
            fn = lambda old : eval(expression)
            new = fn(worry)
            new = new % 9699690
            
            divide = monkey.test.split(" ")[2]
            if new % int(divide) == 0:
                monkeys[int(monkey.tr)].worries.append(new)
            else:
                monkeys[int(monkey.fl)].worries.append(new)
            monkey.inspects += 1

        monkey.worries = []

monkeys.sort(key=lambda x: x.inspects, reverse=True)
print(monkeys[0].inspects * monkeys[1].inspects)