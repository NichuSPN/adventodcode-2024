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
dirNames = ['right', 'left', 'down', 'up']

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
    
def getFencesDirsForPlant(i, j):
    fencesDirs = set()
    for dir_idx, [dir_i, dir_j] in enumerate(dirs):
        neigh_i, neigh_j = i+dir_i, j+dir_j
        if (not inBound(neigh_i, neigh_j)) or input[neigh_i][neigh_j]!=input[i][j]:
            fencesDirs.add(dirNames[dir_idx])
    return fencesDirs

fencesDirs = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(getFencesDirsForPlant(i, j))
    fencesDirs.append(row)
    
def getVerticalLines(jPoints, region):
    vLines = 0
    for jPoint in jPoints:
        plants = [plant for plant in region if plant[1]==jPoint]
        plants.sort()
        prevLeft = prevRight = False
        prevI = None
        for (i, j) in plants:
            currLeft = 'left' in fencesDirs[i][j]
            currRight = 'right' in fencesDirs[i][j]
            if currLeft and (not prevLeft or i!=prevI+1):
                vLines+=1
            if currRight and (not prevRight or i!=prevI+1):
                vLines+=1
            prevLeft, prevRight = currLeft, currRight
            prevI = i
    return vLines

def getHorizontalLines(iPoints, region):
    hLines = 0
    for iPoint in iPoints:
        plants = [plant for plant in region if plant[0]==iPoint]
        plants.sort()
        prevUp = prevDown = False
        prevJ = None
        for (i, j) in plants:
            currUp = 'up' in fencesDirs[i][j]
            currDown = 'down' in fencesDirs[i][j]
            if currUp and (not prevUp or j!=prevJ+1):
                hLines+=1
            if currDown and (not prevDown or j!=prevJ+1):
                hLines+=1
            prevUp, prevDown = currUp, currDown
            prevJ = j
    return hLines

def getPerimeterForRegion(region):
    iPoints, jPoints = zip(*region)
    iPoints=set(iPoints)
    jPoints=set(jPoints)
    return getHorizontalLines(iPoints, region)+getVerticalLines(jPoints, region)

cost = 0
for region in regions:
    area = len(region)
    perimeter = getPerimeterForRegion(region)
    cost+=area*perimeter

print(f"ta-da... Total cost is {cost}")