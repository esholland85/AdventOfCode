from collections import defaultdict, deque
import sys
import math

#get file contents and close file
txt_file = open('Resources/maze.txt','r')
file_content = txt_file.read()
txt_file.close()

#turn contents into a list
lines = file_content.splitlines()

rows = len(lines)
columns = len(lines[0])

possible_moves = []
for r in range(rows):
    for c in range(columns):
        if lines[r][c] == 'S':
            possible_moves.append((r,c,0))

elevations = [[0 for _ in range(columns)] for _ in range(rows)]
for r in range(rows):
    for c in range(columns):
        if lines[r][c] == 'S':
            elevations[r][c] = 1
        elif lines[r][c] == 'E':
            elevations[r][c] = 26
        else:
            elevations[r][c] = ord(lines[r][c]) - ord('a') + 1

def breadthSearch(node):
    possible_moves = deque()
    for r in range(rows):
        for c in range(columns):
            if (node == 1 and lines[r][c]) == 'S' or (node == 2 and elevations[r][c] == 1):
                possible_moves.append((r,c,0))

    used_moves = set()
    while possible_moves:
        r, c, d = possible_moves.popleft()
        if (r,c) in used_moves:
            continue
        used_moves.add((r,c))
        if lines[r][c] == 'E':
            print(f'exit at step {d}')
            return d
        for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r + dr
            cc = c + dc
            if 0<=rr<rows and 0<=cc<columns and elevations[rr][cc]<= 1 + elevations[r][c]:
                possible_moves.append((rr,cc,d+1))

    
print(breadthSearch(1))
print(breadthSearch(2))
