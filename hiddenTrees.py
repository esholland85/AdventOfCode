#get file contents and close file
txt_file = open('Resources/surveyedTrees.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
treeRows = file_content.splitlines()

visibleMap = []

#create an array to represent how far each tree can see in each direction
for row in range(0,len(treeRows)):
    visibleMap.append([])
    for tree in range(0,len(treeRows[row])):
        visibleMap[row].append([])

#Track how far away each height can see by column. Height 1 should always be lowest or tied for lowest.
top_mask = []
for t in treeRows[0]:
    top_mask.append({
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0
    })
bot_mask = []
for t in treeRows[len(treeRows)-1]:
    bot_mask.append({
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0
    })

#apply top height mask, create and apply left height mask for each row
for row in range(0,len(treeRows)):
    left_mask = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0
    }
    for tree in range(0,len(treeRows[row])):
        current_tree = int(treeRows[row][tree])
        visibleMap[row][tree].append(left_mask[current_tree])
        visibleMap[row][tree].append(top_mask[tree][current_tree])

        for i in range(1,10):
            if current_tree >= i:
                top_mask[tree][i] = 1
                left_mask[i] = 1
            else:
                top_mask[tree][i] += 1
                left_mask[i] += 1

#same as above, but for the right side and bottom, so the loops need to start on the right and the bottom
for row in range(len(treeRows)-1,-1,-1):
    right_mask = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0
    }
    for tree in range(len(treeRows[row])-1,-1,-1):
        current_tree = int(treeRows[row][tree])
        visibleMap[row][tree].append(right_mask[current_tree])
        visibleMap[row][tree].append(bot_mask[tree][current_tree])

        for i in range(1,10):
            if current_tree >= i:
                bot_mask[tree][i] = 1
                right_mask[i] = 1
            else:
                bot_mask[tree][i] += 1
                right_mask[i] += 1


#evaluate each tree's overall scenic value
printable_map = []
max_so_far = float('-inf')
for row in visibleMap:
    printable_map.append([])
    for tree in row:
        scenic_value = tree[0]*tree[1]*tree[2]*tree[3]
        printable_map[len(printable_map)-1].append(scenic_value)
        if(scenic_value) > max_so_far:
            max_so_far = scenic_value

print(max_so_far)

    
