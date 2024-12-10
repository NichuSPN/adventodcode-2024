import tqdm

INPUT_FILE_NAME = "actual.txt"
# INPUT_FILE_NAME = "example.txt"

input = []
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    for line in file:
        input.append([int(number) for number in line.strip()])

m = len(input)
n = len(input[0])

reachableEndpoints = []
for i in range(m):
    row = []
    for j in range(n):
        if input[i][j]==9:
            tempSet = set()
            tempSet.add((i, j))
            row.append(tempSet)
        else:
            row.append(None)
    reachableEndpoints.append(row)

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def pointInBound(i, j):
    return 0<=i<m and 0<=j<n

def findReachables(i, j):
    if reachableEndpoints[i][j]!=None:
        return reachableEndpoints[i][j]
    
    currHeight = input[i][j]
    reachableEndpoints[i][j] = set()
    for [ix, jx] in dirs:
        inew, jnew = i+ix, j+jx
        if pointInBound(inew, jnew) and input[inew][jnew]==currHeight+1:
            reachableEndpoints[i][j].update(findReachables(inew, jnew))
    return reachableEndpoints[i][j]

trialheads = 0
for i in tqdm.tqdm(range(m)):
    for j in range(n):
        if input[i][j]==0:
            trialheads+=len(findReachables(i, j))
        
print(f"ta-da... Total trialheads is {trialheads}")