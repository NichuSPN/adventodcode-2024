INPUT_FILE_NAME = "actual.txt"
# INPUT_FILE_NAME = "example.txt"

with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    for line in file:
        input = line.strip().split(' ')

maxBlinks = 75 # Part 1
# maxBlinks = 75 # Part 2

memo = {}

def rule1Passed(stone):
    return stone=='0'

def rule2Passed(stone):
    return len(stone)%2==0

def splitStoneInHalf(stone):
    n = len(stone)//2
    return str(int(stone[:n])), str(int(stone[n:]))

def getNewStone(stone):
    return str(int(stone)*2024)

def getCountAfterBlinks(stone, blinksLeft):
    if blinksLeft==0:
        return 1
    
    if stone not in memo:
        memo[stone] = [-1]*maxBlinks
        
    if memo[stone][blinksLeft-1]!=-1:
        return memo[stone][blinksLeft-1]
    
    if rule1Passed(stone):
        memo[stone][blinksLeft-1] = getCountAfterBlinks('1', blinksLeft-1)
    elif rule2Passed(stone):
        stoneLeft, stoneRight = splitStoneInHalf(stone)
        
        leftCount = getCountAfterBlinks(stoneLeft, blinksLeft-1)
        rightCount = getCountAfterBlinks(stoneRight, blinksLeft-1)
        
        memo[stone][blinksLeft-1] = leftCount + rightCount
    else:
        memo[stone][blinksLeft-1] = getCountAfterBlinks(getNewStone(stone), blinksLeft-1)
    
    return memo[stone][blinksLeft-1]

totalStones = 0
for stone in input:
    totalStones += getCountAfterBlinks(stone, maxBlinks)

print(totalStones)
        
