#get file contents and close file
txt_file = open('Resources/monkeyMath.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
#commands = file_content.splitlines()
monkey_text = file_content.split('Monkey ')

class Monkey:
    def __init__(self, number, items, operation, test, target1, target2):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = int(test)
        self.target1 = int(target1)
        self.target2 = int(target2)
        self.throw_count = 0

    def throw(self):
        current_object = self.items.pop(0)
        pre_test_divisors = current_object.divisors
        current_object.operation_mask(self.operation)

        thrown_to = -1
        if current_object.divisors[self.test] == 0:
            monkey_objects[self.target1].items.append(current_object)
            thrown_to = self.target1
        else:
            monkey_objects[self.target2].items.append(current_object)
            thrown_to = self.target2
        self.throw_count += 1


def round(iteration):
    print(f"Round {iteration}:")
    for monkey in monkey_objects:
        item_count = len(monkey.items)
        for i in range(0,item_count):
            monkey.throw()
    

class item:
    def __init__(self, value, divisors, monk_num):
        self.starting_value = value
        self.starting_monkey = monk_num
        self.value = int(value)
        self.divisors = divisors
        for d in self.divisors:
            self.divisors[d] = self.value % d

    def operation_mask(self, operation):
        for d in self.divisors:
            old = self.divisors[d]
            self.divisors[d] = eval(operation)
            self.divisors[d] = self.divisors[d] % d

#skip zeroeth "monkey"; it's a result of using headers to split
#turn monkeys from a list of text into objcts with properties
monkey_objects = []
my_divisors = {}
for i in range(1,len(monkey_text)):
    pull_apart = monkey_text[i].split(':')
    temp_number = pull_apart[0]
    temp_items = pull_apart[2][1:-12].split(', ')
    temp_operation = pull_apart[3][7:-7]
    #assumes all tests are division based
    temp_test = pull_apart[4][14:-12]
    my_divisors[int(temp_test)] = 0
    #assumes true is always target1 and false target2
    temp_target1 = pull_apart[5].split('monkey ')[1].splitlines()[0]
    temp_target2 = pull_apart[6].split('monkey ')[1].splitlines()[0]
    
    monkey_objects.append(Monkey(temp_number,temp_items,temp_operation,temp_test,temp_target1,temp_target2))

for monkey in monkey_objects:
    item_count = len(monkey.items)
    item_objects = []
    for i in range(0, item_count):
        current_item = monkey.items.pop(0)
        objectified = item(current_item, my_divisors.copy(), monkey.number)
        item_objects.append(objectified)
    monkey.items = item_objects

for i in range(0,10000):
    round(i)

for monkey in monkey_objects:
    print(f"Monkey {monkey.number} inspected objects {monkey.throw_count} times.")