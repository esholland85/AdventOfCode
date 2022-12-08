def find_error(backpack):
    #split backpack into two equal pockets and reduce items to one copy of each/pocket
    pocket1 = set(backpack[0:int(len(backpack)/2)])
    pocket2 = set(backpack[int(len(backpack)/2):])
    result = 0
    
    #lowercase ord('a') - 96 = intended a value
    #uppercase ord('A') - 38 = intended A value
    alpha_bucket = []
    for i in range(0,53):
        alpha_bucket.append(0)
    for item in pocket1:
        aligner = 96*(not item.isupper()) + 38*(item.isupper())
        alpha_bucket[ord(item) - aligner] += 1
    for item in pocket2:
        aligner = 96*(not item.isupper()) + 38*(item.isupper())
        alpha_bucket[ord(item) - aligner] += 1
    
    #the item that exists in both sets now is the only index with a value of 2
    for i in range(len(alpha_bucket)):
        if alpha_bucket[i] == 2:
            result = i
    
    return result

def find_badge(backpack1,backpack2,backpack3):
    #reduce backpacks to a single copy of each item
    b1 = set(backpack1)
    b2 = set(backpack2)
    b3 = set(backpack3)
    result = 0

    #create the same bucket system
    alpha_bucket = []
    for i in range(0,53):
        alpha_bucket.append(0)
    for item in b1:
        aligner = 96*(not item.isupper()) + 38*(item.isupper())
        alpha_bucket[ord(item) - aligner] += 1
    for item in b2:
        aligner = 96*(not item.isupper()) + 38*(item.isupper())
        alpha_bucket[ord(item) - aligner] += 1
    for item in b3:
        aligner = 96*(not item.isupper()) + 38*(item.isupper())
        alpha_bucket[ord(item) - aligner] += 1

    #the item that exists in all sets now is the only index with a value of 3
    for i in range(len(alpha_bucket)):
        if alpha_bucket[i] == 3:
            result = i

    return result

#get file contents and close file
txt_file = open('Resources/backpacks.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
backpacks = file_content.splitlines()

totalResult = 0
badgeResult = 0
for b in range(len(backpacks)):
    totalResult += find_error(backpacks[b])
    #every third backpack, check the three most recent for badges
    if((b+1)%3 == 0):
        badgeResult += find_badge(backpacks[b],backpacks[b-1],backpacks[b-2])

print(totalResult)
print(badgeResult)