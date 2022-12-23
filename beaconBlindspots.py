import math

#get file contents and close file
txt_file = open('Resources/beaconFeedback.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
signal_sources = file_content.splitlines()

#create a sensor:beacon dictionary
located_beacons = {}
for line in signal_sources:
    temp = line.split(' ')
    sensor = (int(temp[2].strip('x=,')),int(temp[3].strip('y=:')))
    beacon = (int(temp[8].strip('x=,')),int(temp[9].strip('y=')))
    located_beacons[sensor] = beacon
    if located_beacons[sensor] == sensor:
        print('Alert! Shared space')

def getDistance(sensor):
    x_distance = abs(located_beacons[sensor][0] - sensor[0])
    y_distance = abs(located_beacons[sensor][1] - sensor[1])
    return x_distance + y_distance

#since the solution is looking for row data, I want a y:x dictionary where the x is a set containing all coordinates filled in that row
not_beacons = {}
lowestX = float('inf')
highestX = float('-inf')
lowestY = float('inf')
highestY = float('-inf')
for sensor in located_beacons:
    sensor_x = sensor[0]
    sensor_y = sensor[1]
    beacon_x = located_beacons[sensor][0]
    beacon_y = located_beacons [sensor][1]
    if sensor_x < lowestX:
        lowestX = sensor_x
    if sensor_y < lowestY:
        lowestY = sensor_y
    if beacon_x < lowestX:
        lowestX = beacon_x
    if beacon_y < lowestY:
        lowestY = beacon_y
    if sensor_x > highestX:
        highestX = sensor_x
    if sensor_y > highestY:
        highestY = sensor_y
    if beacon_x > highestX:
        highestX = beacon_x
    if beacon_y > highestY:
        highestY = beacon_y

def designateEmpty(row, new_range):
    #if not point in located_beacons.values():
    if not row in not_beacons:
        not_beacons[row] = []
        not_beacons[row].append(new_range)
    #print(f"placing {new_range} in row {row}")
    for i in range(len(not_beacons[row])):
        #print(f"segment {i}")
        target_range_low = not_beacons[row][i][0]
        target_range_high = not_beacons[row][i][1]
        #if entirely subsumed in existing data, stop looking
        if new_range[0] >= target_range_low and new_range[1] <= target_range_high:
            break
        #if new range entirely subsumes existing data, delete the existing data, call placement again to avoid dealing with changed indices, then break the cycle
        if new_range[0] <= target_range_low and new_range[1] >= target_range_high:
            not_beacons[row].pop(i)
            if len(not_beacons[row]) == 0:
                not_beacons[row].append(new_range)
            else:
                designateEmpty(row,new_range)
            break
        #if entirely less than the current entry, insert data here
        if new_range[1] < target_range_low:
            not_beacons[row].insert(i,new_range)
        #if entirely greater than the current entry and more entries exist, next entry
        elif new_range[0] > target_range_high and i < len(not_beacons[row]) - 1:
            continue
        #if new range overlaps the low end, merge together
        elif new_range[0] <= target_range_low and new_range[1] >= target_range_low:
            not_beacons[row].pop(i)
            if len(not_beacons[row]) == 0:
                not_beacons[row].append((new_range[0],target_range_high))
            else:
                designateEmpty(row,(new_range[0],target_range_high))
            break
        #if new range overlaps the high end, merge together the other way
        elif new_range[0] <= target_range_high and new_range[1] >= target_range_high:
            not_beacons[row].pop(i)
            if len(not_beacons[row]) == 0:
                not_beacons[row].append((target_range_low,new_range[1]))
            else:
                designateEmpty(row,(target_range_low,new_range[1]))
            break
        #if it gets to the last entry
        elif i == len(not_beacons[row]) - 1:
            not_beacons[row].append(new_range)

for sensor in located_beacons:
    beacon = located_beacons[sensor]
    occlusion_height = getDistance(sensor)
    occlusion_width = 0
    min_occlusion = occlusion_height * -1
    increasing = True
    working = True
    while working:
        #lowest point = same x value as beacon, y + distance (since zero is top left)
        working_point = (sensor[0],sensor[1] + occlusion_height)
        working_range = (working_point[0] - occlusion_width, working_point[0] + occlusion_width)
        designateEmpty(working_point[1],working_range)
        occlusion_height -= 1
        if occlusion_height < min_occlusion:
            working = False
        if increasing:
            occlusion_width += 1
            if occlusion_width == abs(min_occlusion):
                increasing = False
        else:
            occlusion_width -= 1

#remove points that already are beacons from the list of things that can't be beacons
for sensor in located_beacons:
    beacon = located_beacons[sensor]
    row = not_beacons[beacon[1]]
    for j in range(len(row)):
        entry_low = row[j][0]
        entry_high = row[j][1]
        #if the beacon is less than the low of the current entry, its location is already considered possible
        if beacon[0] < entry_low:
            break
        #if the beacon is greater than the high of the current entry, move to next
        if beacon[0] > entry_high:
            continue
        #if the beacon falls in the middle of an entry, insert a new entry before, and chop the current entry to be after
        if entry_low < beacon[0] and entry_high > beacon[0]:
            not_beacons[beacon[1]][j] = (beacon[0]+1,entry_high)
            not_beacons[beacon[1]].insert(j,(entry_low,beacon[0]-1))
            break
        #if the beacon replaces a one-number-range:
        if beacon[0] == entry_low and beacon[0] == entry_high:
            not_beacons[beacon[1]].pop(j)
            break
        #if the beacon is the lowest number in an entry:
        if beacon[0] == entry_low:
            not_beacons[beacon[1]][j] = (beacon[0]+1,entry_high)
        #if the beacon is the highest number in an entry:
        if beacon[0] == entry_high:
            not_beacons[beacon[1]][j] = (entry_low,beacon[0]-1)
            break

#for row in not_beacons:
    #print(F"row {row} contains {not_beacons[row]}")

count = 0
for entry in not_beacons[2000000]:
    count += entry[1]-entry[0] + 1

#answer to part 1
print(count)

#answer to part 2
#to avoid potential out of bounds errors looking ahead, I'm simply printing the relevant values and doing the math manually
max_value = 4000000
for row_num in not_beacons:
    if row_num < 0 or row_num > max_value:
        continue
    row = not_beacons[row_num]
    if len(row) == 1:
        if row[0][0] > 0 or row[0][1] < max_value:
            print(f"row {row_num} contains range {row[0]}")
            break
        continue
    previous_entry = ('a','b')
    for entry in row:
        if entry[0] > 0 and entry[0] <= max_value + 1:
            if (entry[0] - 1,row_num) in located_beacons.values():
                print('Known beacon present')
                continue
            print(f"row {row_num} contains range {entry}, with previous entry {previous_entry}")
        if entry[1] > 0 and entry[1] < max_value:
            if (entry[1] + 1,row_num) in located_beacons.values():
                print('Known beacon present')
                continue
            print(f"row {row_num} contains range {entry}, with previous entry {previous_entry}")
        previous_entry = entry