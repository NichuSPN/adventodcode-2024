# INPUT_FILE_NAME = 'example.txt'
INPUT_FILE_NAME = 'actual.txt'

input=[]
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    # Input is in the format of strings in multiple lines
    for line in file:
        input.append(line.strip())
        
stringToBeMatched = "XMAS"        
        
m = len(input)
n = len(input[0])

def upPossible(i):
    return i-3>=0

def downPossible(i):
    return i+3<m

def leftPossible(j):
    return j-3>=0

def rightPossible(j):
    return j+3<n

def upMatch(i, j):
    if not upPossible(i):
        return False
    
    for idx in range(4):
        if input[i-idx][j]!=stringToBeMatched[idx]:
            return False
    return True

def downMatch(i, j):
    if not downPossible(i):
        return False
    
    for idx in range(4):
        if input[i+idx][j]!=stringToBeMatched[idx]:
            return False
    return True

def leftMatch(i, j):
    if not leftPossible(j):
        return False
    
    for idx in range(4):
        if input[i][j-idx]!=stringToBeMatched[idx]:
            return False
    return True

def rightMatch(i, j):
    if not rightPossible(j):
        return False
    
    for idx in range(4):
        if input[i][j+idx]!=stringToBeMatched[idx]:
            return False
    return True

def q1Match(i, j):
    if not upPossible(i) or not rightPossible(j):
        return False
    
    for idx in range(4):
        if input[i-idx][j+idx]!=stringToBeMatched[idx]:
            return False
    return True

def q2Match(i, j):
    if not downPossible(i) or not rightPossible(j):
        return False
    
    for idx in range(4):
        if input[i+idx][j+idx]!=stringToBeMatched[idx]:
            return False
    return True

def q3Match(i, j):
    if not downPossible(i) or not leftPossible(j):
        return False
    
    for idx in range(4):
        if input[i+idx][j-idx]!=stringToBeMatched[idx]:
            return False
    return True

def q4Match(i, j):
    if not upPossible(i) or not leftPossible(j):
        return False
    
    for idx in range(4):
        if input[i-idx][j-idx]!=stringToBeMatched[idx]:
            return False
    return True

def numberOfDirectionsMatched(i, j):
    functions = [upMatch, downMatch, rightMatch, leftMatch,
                 q1Match, q2Match, q3Match, q4Match]
    return sum([f(i, j) for f in functions])

matches=0
for i in range(m):
    for j in range(n):
        if input[i][j]==stringToBeMatched[0]:
            matches+=numberOfDirectionsMatched(i, j)
            
print(f"ta-da... {matches} number of XMAS found")

'''
Checking if first letter matches to reduce number of iteraction checks
Directions:
right, left, up and down are self explanatory
Quadrants:
4|1
---
3|2 
'''