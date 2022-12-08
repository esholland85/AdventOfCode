#get file contents and close file
txt_file = open('Resources/elves.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
contents_as_list = file_content.splitlines()

#turn strings into ints and new lines into 0/demarcation point
for i in range(0,len(contents_as_list)):
    if contents_as_list[i] == "":
        pass
    else:
        contents_as_list[i] = int(contents_as_list[i])

#use demarcation point to calculate which elf is holding the most calories
def count_totals (list):
    #sorting a totals list was an alternate way to accomplish the test, arguably cleaner, but it wasn't the first way I came up with.
    #I used it to re-affirm that the answer I was getting was right when testing said it wasn't.
    #turned out the issue wasn't my logic, it was the formatting I was doing as I manually entered the answer on the website.
    #commented out for my own reference in future tasks
    #totals = []
    elf = 0
    max_so_far = 0
    second = 0
    third = 0
    for i in list:
        if i == "":
            #totals.append(elf)
            if elf > max_so_far:
                third = second
                second = max_so_far
                max_so_far = elf
            elif elf > second:
                third = second
                second = elf
            elif elf > third:
                third = elf
            elf = 0

        else:
            elf += i
        
    result = max_so_far + second + third
    #totals.sort()

    return result
    #first challenge
    #return max_so_far


#print the answer
print(count_totals(contents_as_list))