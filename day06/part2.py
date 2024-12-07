# INPUT_FILE_NAME = 'example.txt'
INPUT_FILE_NAME = 'actual.txt'

input=[]
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    # Input is in the format of strings in multiple lines
    for line in file:
        input.append(line.strip())

m = len(input)
n = len(input[0])

# Find ^
found = False
for i in range(m):
    for j in range(n):
        if input[i][j]=="^":
            start_i, start_j = i, j
            found = True
            break
    if found:
        break

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
visited = set()

i, j = start_i, start_j
dir = 0
while 0<=i<m and 0<=j<n:
    visited.add((i, j))
    next_i, next_j = i+directions[dir][0], j+directions[dir][1]
    if not (0<=next_i<m and 0<=next_j<n):
        break
    if input[next_i][next_j]=="#":
        dir=(dir+1)%4
        continue
    i, j = next_i, next_j
    
def loopFormed(ii, jj):
    visitedWithDir = set()
    i, j = start_i, start_j
    dir = 0
    while 0<=i<m and 0<=j<n:
        if (i, j, dir) in visitedWithDir:
            return True
        visitedWithDir.add((i, j, dir))
        next_i, next_j = i+directions[dir][0], j+directions[dir][1]
        if not (0<=next_i<m and 0<=next_j<n):
            return False
        if input[next_i][next_j]=="#" or (next_i==ii and next_j==jj):
            dir=(dir+1)%4
            continue
        i, j = next_i, next_j
    return False

# To print progress
tqdm = __import__("tqdm")
totalObstructions = 0
for (i, j) in tqdm.tqdm(visited):
    if i==start_i and j==start_j:
        continue
    totalObstructions+=loopFormed(i, j)
    
print(f"ta-da... {totalObstructions} obstructions can be places to put the guy in a loop!")