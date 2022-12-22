import math

#get file contents and close file
txt_file = open('Resources/sandInput.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
wall_instructions = file_content.splitlines()

clean_instructions = []
for line in wall_instructions:
    temp = line.split('->')
    for i in range(len(temp)):
        temp[i] = temp[i].strip()

    clean_instructions.append(temp)

#find highest and lowest x and y, create a 2d array with gaps on all edges
highX = float('-inf')
lowX = float('inf')
highY = float('-inf')
lowY = 0

for i in range(len(clean_instructions)):
    for j in range(len(clean_instructions[i])):
        temp = clean_instructions[i][j].split(',')
        if highX < int(temp[0]):
            highX = int(temp[0])
        if lowX > int(temp[0]):
            lowX = int(temp[0])

        if highY < int(temp[1]):
            highY = int(temp[1])

#raw point - differential  = index
#x off set by 3 from origin to make sure it doesn't check a non-existent index, y static but left in because the code expects it now.
differential = (lowX - 200,lowY)

#height adds one at the bottom and width adds 1 to the other side
grid_width = highX - differential[0] + 200
grid_height = highY - differential[1] + 1

new_walls = []
for i in range(len(clean_instructions)):
    current_point = clean_instructions[i][0].split(',')
    current_point[0],current_point[1] = int(current_point[0]), int(current_point[1])
    for j in range(1,len(clean_instructions[i])):
        next_point = clean_instructions[i][j].split(',')
        next_point[0],next_point[1] = int(next_point[0]), int(next_point[1])
        travel_distance = 0
        travel_axis = 'x'
        if current_point[0] == next_point[0]:
            travel_distance = 1 + abs(current_point[1] - next_point[1])
            travel_axis = 'y'
        else:
            travel_distance = 1 + abs(current_point[0] - next_point[0])
        for k in range(travel_distance):
            step_value = k
            if travel_axis == 'x':
                if next_point[0] - current_point[0] < 0:
                    step_value *= -1
                new_walls.append((current_point[0] + step_value,current_point[1]))
            if travel_axis == 'y':
                if next_point[1] - current_point[1] < 0:
                    step_value *= -1
                new_walls.append((current_point[0],current_point[1] + step_value))
        current_point[0], current_point[1] = next_point[0],next_point[1]


my_map =[]
for i in range(grid_height + 1):
    my_map.append([])
    for j in range(grid_width + 1):
        my_map[i].append('.')

for wall in new_walls:
    my_map[wall[1] - differential[1]][wall[0] - differential[0]] = '#'

#for part two, add a row of walls to the bottom, and change the stop condition from a part reaching the empty line to a part stopping in the position my_map[0,500-differential[0]]
my_map.append(my_map[len(my_map)-1].copy())
for i in range(len(my_map[len(my_map)-1])):
    my_map[len(my_map)-1][i] = '#'

def dropParticle():
    moving = True
    #reverse x and y because my_map uses rows for the first value
    particle_position = (0,500 - differential[0])
    while moving:
        moving = False
        target1 = (particle_position[0] + 1, particle_position[1])
        target2 = (particle_position[0] + 1, particle_position[1] - 1)
        target3 = (particle_position[0] + 1, particle_position[1] + 1)
        if target3[1] == 500-differential[0] + 1 and my_map[1][500-differential[0]+1] == 'O':
            print('Sand stopped flowing')
            return False
        if my_map[target1[0]][target1[1]] == '.':
            my_map[target1[0]][target1[1]] = 'O'
            my_map[particle_position[0]][particle_position[1]] = '.'
            particle_position = target1
            moving = True
        elif target2[1] >= 0 and my_map[target2[0]][target2[1]] == '.':
            my_map[target2[0]][target2[1]] = 'O'
            my_map[particle_position[0]][particle_position[1]] = '.'
            particle_position = target2
            moving = True
        elif target3[1] < len(my_map[0]) and my_map[target3[0]][target3[1]] == '.':
            my_map[target3[0]][target3[1]] = 'O'
            my_map[particle_position[0]][particle_position[1]] = '.'
            particle_position = target3
            moving = True
        
    return True

#starts at negative one because the current setup stops on the particle of sand that rolls off the edge and the question asks for how many stay put
#0 for part 2 because it stops before adding the last piece
counter = 0
shifting = True
while shifting:
    shifting = dropParticle()
    counter += 1
print(counter)
for row in my_map:
    print("".join(row))
