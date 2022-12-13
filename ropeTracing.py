#get file contents and close file
txt_file = open('Resources/ropeInstructions.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
rope_moves = file_content.splitlines()
parsed_moves = []

for line in rope_moves:
    parsed_moves.append(line.split(' '))

class point:
    def __init__(self,x,y,name = 'point'):
        self.x = x
        self.y = y
        self.name = name
        self.history = {}

    def follow(self, target_point):
        dif_x = target_point.x - self.x
        dif_y = target_point.y - self.y
        if abs(dif_x) > 1:
            if dif_x > 0:
                self.x += 1
            else:
                self.x -= 1
            if dif_y > 0:
                self.y += 1
            elif dif_y < 0:
                self.y -= 1
        elif abs(dif_y) > 1:
            if dif_y > 0:
                self.y += 1
            else:
                self.y -= 1
            if dif_x > 0:
                self.x += 1
            elif dif_x < 0:
                self.x -= 1
        
        if self.name != 'point':
            print(f"Target is at: ({target_point.x},{target_point.y})")
            print(f"Tail is at: ({self.x},{self.y})")
        if self.x in self.history:
            self.history[self.x].add(self.y)
        else:
            self.history[self.x] = set([self.y])
            

def move(direction, times, moving_point, tail):
    if times > 1:
        move (direction, times-1, moving_point, tail)

    if direction == 'L':
        moving_point.x -= 1
    elif direction == 'U':
        moving_point.y += 1
    elif direction == 'R':
        moving_point.x += 1
    elif direction == 'D':
        moving_point.y -= 1

    #this should be refactored; a tail could be a characteristic of a point, and follow would recursively call follow all the way down the line. But since this solves the challenge, I'm stopping here.
    tail.follow(moving_point)
    r2.follow(r1)
    r3.follow(r2)
    r4.follow(r3)
    r5.follow(r4)
    r6.follow(r5)
    r7.follow(r6)
    r8.follow(r7)
    r9.follow(r8)

#if this were longer, the rope pieces could be created in a list and follow called on each one using a loop
r0 = point(0,0)
r1= point(0,0)
r2= point(0,0)
r3= point(0,0)
r4= point(0,0)
r5= point(0,0)
r6= point(0,0)
r7= point(0,0)
r8= point(0,0)
r9= point(0,0)

for line in parsed_moves:
    move(line[0],int(line[1]),r0,r1)

total_spots = 0

for column in r9.history:
    total_spots += len(r9.history[column])

print(total_spots)