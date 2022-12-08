#get file contents and close file
txt_file = open('Resources/stackGuide.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
stacking_guide = file_content.splitlines()

num_stacks = 9
highest_stack = 8
stack_map = []

for i in range(0,highest_stack):
    next_line = stacking_guide[i]
    for j in range(0,num_stacks):
        if i == 0:
            stack_map.append([])
        current_crate = next_line[j*4:(j+1)*4]
        if current_crate == '    ':
            continue
        else:
            stack_map[j].append(current_crate[1:2])

#commented out moving 1 at at ime to replace with moving entire instruction at once
for i in range(highest_stack+2,len(stacking_guide)):
    instruction = stacking_guide[i].split(' ')
    for j in range(0,int(instruction[1])):
        current_crate = stack_map[int(instruction[3])-1].pop(0)
        #stack_map[int(instruction[5])-1].insert(0,current_crate)
        stack_map[int(instruction[5])-1].insert(j,current_crate)

for column in stack_map:
    if(len(column) > 0):
        print(column[0])
    else:
        print('[ ]')