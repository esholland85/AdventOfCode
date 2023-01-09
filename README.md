# AdventOfCode
A collection of 2022 Advent Of Code challenges
These challenges range from simple to complex, straightforward to thinking creatively. Because of the "reach a specific answer" nature of the challenges,
the time constraints involved, and the fact I was doing them for fun, the code is messy. If an idea I had didn't work, I might comment out the code for later reference,
then when another idea does work, I left old comments and code that didn't interfere alone and moved on. This is not emblematic of my general work, but does 
give unique insight to my thought process.
*Not every file contains code to solve both parts. In several of the challenges, solution 2 used the same information in a different way,
so I changed existing code rather than adding onto it.*
For full instructions, see AdventOfCode.com/2022

Every day required some form of parsing plain text inputs. The degree of parsing varied significantly. Other than that, here are the targets of each:
countingCals, Part 1: Find the object with the highest value collection.
countingCals, Part 2: Find the 3 objects containing the 3 highest value collections.
RPS, Part 1: Using both players choice for rock paper scissors, calculate total value of several matches
RPS, Part 2: Using opponent's choice and whether the match is a win, loss, or draw, calculate total value of several matches
findError, Part 1: Find a letter repeated between two sets. Repeat for multiple sets.
findError, Part 2: Find a letter used exactly once in every instance of a set. Repeat for multiple sets.
cleaningTasks, Part 1: Compare pairs of ranges to find when one range fully contains the other.
cleaningTasks, Part 2: Compare pairs of ranges to find when they overlap
crateStack, Part 1: Follow movement instructions, moving only the last item in a list at a time (invert order of moved objects)
crateStack, Part 2: Follow movement instructions, moving multiple items at once (maintain order of moved objects)
radioSignals, Part 1: Find the first instance of 4 unique characters in a string
radioSignals, Part 2: Find the first instance of 14 unique characters in a string
systemCheck, Part 1: Re-create folder structure based on command line navigation instructions, total all file sizes below 100,000
systemCheck, Part 2: In the above folder structure, find the smallest directory you can delete to have 30,000,000 space free
hiddenTrees, Part 1: In a grid, determine whether each number is larger than all numbers in any of left, right, above, or below its position
hiddenTrees, Part 2: In a grid, determine how many spaces exist between each number and a number that is greater than or equal to it in each direction
ropeTracing, Part 1: Given instructions for the head, and rules for the tail, determine the total number of positions the tail visits.
ropeTracing, Part 2: For a longer rope, each segment of the rope follows the tail's rules from above. Determine the number of positions the final tail visits.
crtRepair, Part 1: Perform math operations designated by input
crtRepair, Part 2: Use current value being operated on to create an ASCII image and read the resulting "word"
predictingMonkeys, Part 1: Perform math operations on several separate numbers designated by rules
predictingMonkeys, Part 2: Change one operation so numbers far exceed the bounds of reasonable RAM usage if raw data is used
*Challenges 12, 13 and 16 were beyond my current understanding, so I went looking for solutions.*
*12: I learned that Breadth First Searching works for shortest path determination IF each step is counted the same.*
mazeSolver, Part 1: Figure out the shortest route through the maze.
mazeSolver, Part 2: Use the end as the start, find the shortest route to any space valued at 1
*13 I attempted, but when all my logic was in place, it returned the wrong value. Following a solution, I learned about comparing ints and lists of ints*
signalCheck, Part 1: Compare two lists. Each entry may be an int or another list. Follow complex rules for what to do in various comparison outcomes
signalCheck, Part 2: Use a sorting method to sort based on the outcomes of the rules in part 1
sandFall, Part 1: Using a 2d slice of a room, determine how many pieces of sand can rest in that slice before all future pieces will fall off the lowest shelf.
sandFall, Part 2: Add a floor 2 grains below the lowest shelf, determine how many pieces of sand will rest in the slice before the most recent piece of sand rests
  at the entrance point
beaconBlindspots, Part 1: Using a group of known shortest routes, find how many spaces exist between shortest routes that might also contain a beacon.
beaconBlindspots, Part 2: Use rules to eliminate impossible blindspots, get the value of the only possible blindspot to contain the beacon.
*16 I did some setup on this, realized my approach would take too much processing time, and learned about the existence of Dynamic Programming.
  I think I could apply precepts of Dynamic Programming and solve this puzzle, but at this point, the time committment began to outweigh the value
  I was getting out of these challenges.*
travellingRepairman, Part 1(incomplete): Given a time limit and a map, determine the max value you can get by either repairing or moving at each location
