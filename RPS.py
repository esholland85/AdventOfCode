#get file contents and close file
txt_file = open('Resources/strategy.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
cheat_guide = file_content.splitlines()
#in both scenarios ABC is rock, paper, scissors respectively
#Rock = 1 point, Paper = 2 points, scissors = 3 points
#losing = 0 points, drawing = 3 points, winning = 6 points
#input is your opponent's throw (A, B, or C) a space and one of two things depending on the scenario.
#Per scenario, your return is the points you scored that round, with the final output being total points

#x means rock, y means paper, z means scissors
results1 = {'A': {
   'X': 4,
   'Y': 8,
   'Z': 3 
},
'B': {
    'X': 1,
    'Y': 5,
    'Z': 9
},
'C': {
    'X': 7,
    'Y': 2,
    'Z': 6
}}

#x means lose, y means draw, z means win
results2 = {'A': {
   'X': 3,
   'Y': 4,
   'Z': 8 
},
'B': {
    'X': 1,
    'Y': 5,
    'Z': 9
},
'C': {
    'X': 2,
    'Y': 6,
    'Z': 7
}}

total = 0

for e in cheat_guide:
    total += results2[e[0]][e[2]]

print(total)