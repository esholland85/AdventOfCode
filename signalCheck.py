#get file contents and close file
txt_file = open('Resources/mixedSignal.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
my_text = file_content.splitlines()

myInputs = []
for line in my_text:
    temp = None
    #for i in range(len(temp)):
    #    if len(temp[i]) > 0:
    #        temp[i] = int(temp[i])
    #    else:
    #        temp.pop()
    if len(line) > 0:
        temp = eval(line)
    myInputs.append(temp)

#following a solution
def compare(left,right):
    #print(f"comparing {left} to {right}")
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left == right:
            return 'continue'
        else:
            return False
    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left) and i < len(right):
            c = compare(left[i],right[i])
            if c != 'continue':
                return c
            i += 1
        if i == len(left) and i < len(right):
            return True
        elif i < len(left) and i == len(right):
            return False
        else:
            return 'continue'
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left],right)
    else:
        return compare(left,[right])

#initial attempt
def compareLists(left,right):
    lengthL = len(left)
    lengthR = len(right)
    max_iterations = 0

    if lengthL <= lengthR:
        max_iterations = lengthL
    else:
        max_iterations = lengthR
    
    #mine does not work for the attached scenario; it seems to be a miss-order in a list contiaining a list vs a list shorter than the outer list
    #[[[[4],2]]]
    #[[4,0],[1,[[1]],[]],[[10,[1]]],[0,0,[0,[6,5,7,8],[1,10]],7,[9,[3,9],[9,6]]]]
    #which breaks down to comparing [[4], 2] to [4]
    #The fours should compare, and then the left list should see that it's too long and return false, but mine is returning continue instead

    for i in range(max_iterations):
        if not isinstance(left[i],int) or not isinstance(right[i], int):
            #need to include returns of true, false, and keep going from sub-lists
            this_list = compareUnmatched(left[i],right[i])
            if this_list != 'continue' or i == max_iterations - 1:
                return this_list
            else:
                continue
        if left[i] > right[i]:
            return False
        elif left[i] < right[i]:
            return True
        
    if lengthL < lengthR:
        return True
    elif lengthL > lengthR:
        return False
    return 'continue'

def compareUnmatched(left,right):
    if isinstance(left,int):
        left = [left]
    elif not isinstance(left, list):
        print('Alert!')
    if isinstance(right,int):
        right = [right]
    elif not isinstance(right, list):
        print('Alert!')
    return compareLists(left,right)

#answer for part 1
output = 0
exposed_index = 0
for i in range(0,len(myInputs),3):
    exposed_index += 1

    if compare(myInputs[i],myInputs[i+1]):
        output += exposed_index
        #print(f"Line {i} is in the right order")

print(output)

new_inputs = []
for line in my_text:
    if line == '':
        continue
    else:
        new_inputs.append(eval(line))

new_inputs.append([[2]])
new_inputs.append([[6]])

#answer for part 2
current_index = -1
important_indices = [0,0]
while current_index < len(new_inputs)-2:
    current_index +=1
    if not compare(new_inputs[current_index], new_inputs[current_index + 1]):
        new_inputs[current_index], new_inputs[current_index + 1] = new_inputs[current_index + 1], new_inputs[current_index]
        current_index -= 1
        if current_index > -1:
            current_index -= 1
    if new_inputs[current_index] == [[2]]:
        important_indices[0] = current_index
    if new_inputs[current_index] == [[6]]:
        important_indices[1] = current_index
print((important_indices[0]+1)*(important_indices[1]+1))