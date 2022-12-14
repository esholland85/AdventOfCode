#get file contents and close file
txt_file = open('Resources/signalInput.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
commands = file_content.splitlines()
parsed_commands = []

for command in commands:
    parsed_commands.append(command.split(' '))

x_register = 1
current_cycle = 0
current_row = ""
collected_rows = []

for command in parsed_commands:
    if current_cycle == x_register - 1 or current_cycle == x_register or current_cycle == x_register + 1:
        current_row += '#'
    else:
        current_row += '.'

    current_cycle += 1

    if current_cycle % 40 == 0:
        collected_rows.append(current_row)
        current_row = ""
        current_cycle = 0

    if command[0] == 'addx':
        if current_cycle == x_register - 1 or current_cycle == x_register or current_cycle == x_register + 1:
            current_row += '#'
        else:
            current_row += '.'

        current_cycle += 1

        if current_cycle % 40 == 0:
            collected_rows.append(current_row)
            current_row = ""
            current_cycle = 0
        x_register += int(command[1])
        #print(f"Adding {command[1]} after cycle {current_cycle}")
        
print(current_cycle)
for row in collected_rows:
    print(row)