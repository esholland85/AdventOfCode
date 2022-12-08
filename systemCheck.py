folder_holder = []

class folder:
    def __init__(self, name, parent, file_size):
        self.name = name
        self.parent = parent
        self.children = []
        self.content_size = file_size
        self.ls = False

    def add_child(self, child_object):
        self.children.append(child_object)

    def get_size(self):
        result = self.content_size
        for c in self.children:
            result += c.get_size()

        folder_holder.append(result)
        return result

#get file contents and close file
txt_file = open('Resources/directoryCommands.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
commands = file_content.splitlines()

startingDirectory = folder("/", None,0)

currentDirectory = startingDirectory

#create folder structure. Each folder's contents are listed before changing directory, so at change directory, add all collected sizes to that directory. After final command, if those sizes weren't added, add them in.
size_since_cd = 0
for c in commands:
    command_array = c.split(' ')
    if command_array[0] == '$' and command_array[1] == 'cd':
        if command_array[2] == '..':
            if not currentDirectory.name == '/':
                currentDirectory.content_size += size_since_cd
                size_since_cd = 0
                currentDirectory = currentDirectory.parent
        else:
            currentDirectory.content_size += size_since_cd
            size_since_cd = 0
            for c in currentDirectory.children:
                if c.name == command_array[2]:
                    currentDirectory = c
                    break
            if not currentDirectory.name == command_array[2]:
                new_directory = folder(command_array[2],currentDirectory,0)
                currentDirectory.add_child(new_directory)
                currentDirectory = new_directory
    if command_array[0].isnumeric():
        size_since_cd += int(command_array[0])

currentDirectory.content_size += size_since_cd

disk_size = 70_000_000
required_space = 30_000_000
startingDirectory.get_size()

curent_empty = disk_size - folder_holder[len(folder_holder)-1]
print(curent_empty)

min_delete = required_space - curent_empty
print(min_delete)

temp = float('inf')
for d in folder_holder:
    if d >= min_delete and d < temp:
        temp = d

print(temp)