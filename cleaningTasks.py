#get file contents and close file
txt_file = open('Resources/assignments.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
my_text = file_content.splitlines()

result = 0

for i in my_text:
    #split lines into pairs
    temp = i.split(',')
    first = temp[0]
    second = temp[1]
    #split each pair into individual start and end
    temp = first.split('-')
    first1 = int(temp[0])
    first2 = int(temp[1])
    temp = second.split('-')
    second1 = int(temp[0])
    second2 = int(temp[1])

    #compare start and end of each individual for overlapping cleaning areas within a pair
    if (first1 <= second1 and first2 >= second1) or (first1 <= second2 and first2 >= second2) or (first1 >= second1 and first2 <= second2):
        result += 1

print(result)