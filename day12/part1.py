INPUT_FILE_NAME = "actual.txt"
# INPUT_FILE_NAME = "example.txt"

input = []
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    for line in file:
        input.append([plantLabel for plantLabel in line.strip()])

m = len(input)
n = len(input[0])

notVisited = set()
for i in range(m):
    for j in range(n):
        notVisited.add((i, j))

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def inBound(i, j):
    return 0<=i<m and 0<=j<n
  
def getAllPlantsForRegion(i, j):
    plant = input[i][j]
    plantsInRegion = {(i, j)}
    notVisited.remove((i, j))
    for [dir_i, dir_j] in dirs:
        neigh_i, neigh_j = i+dir_i, j+dir_j
        if (neigh_i, neigh_j) in notVisited and input[neigh_i][neigh_j]==plant:
            plantsInRegion.add((neigh_i, neigh_j))
            plantsInRegion.update(getAllPlantsForRegion(neigh_i, neigh_j))
    return plantsInRegion
  
regions = []        
while len(notVisited) > 0:
    (i, j) = list(notVisited)[0]
    regions.append(getAllPlantsForRegion(i, j))

def getFencesForPlant(i, j):
    fences = 0
    for [dir_i, dir_j] in dirs:
        neigh_i, neigh_j = i+dir_i, j+dir_j
        if (not inBound(neigh_i, neigh_j)) or input[neigh_i][neigh_j]!=input[i][j]:
            fences+=1
    return fences

cost = 0
for region in regions:
    area = len(region)
    perimeter = 0
    for (i, j) in region:
        perimeter+=getFencesForPlant(i, j)
    cost+=area*perimeter

print(f"ta-da... Total cost is {cost}")