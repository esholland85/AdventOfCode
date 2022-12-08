#get file contents and close file
txt_file = open('Resources/encoded.txt','r')
file_content = txt_file.read()
txt_file.close()

trackedPs = []

knownDup = -1


#make list of current range of chars
for i in range (0,14):
    trackedPs.append(file_content[i])

for i in range(12,-1,-1):
    for j in  range(i+1,14):
        if trackedPs[i] == trackedPs[j]:
            knownDup = i
            break
    if knownDup >= 0:
        break

#check if new inclusion moves the bar for exiting
result = 0
for i in range(14,len(file_content)):
    if knownDup == -1:
        result = i
        break
    for j in range(13,0,-1):
        if file_content[i] == trackedPs[j]:
            knownDup = j
            break
        if knownDup == j-1:
            break
    for k in range(0,13):
        trackedPs[k] = trackedPs[k+1]
    trackedPs[13] = file_content[i]
    knownDup -= 1
    print(knownDup)

print(result)

