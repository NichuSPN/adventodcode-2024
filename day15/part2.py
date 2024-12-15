import tqdm
INPUT_FILE_NAME = "actual.txt"
# INPUT_FILE_NAME = "example.txt"

warehouseMap = []
directions = ""

warehouseMapDone=False
with open(f"input/{INPUT_FILE_NAME}", 'r') as file:
    for i, line in enumerate(file):
        if len(line) == 1:
            warehouseMapDone=True
            continue
        if warehouseMapDone:
            directions+=line.strip()
        else:
            row = []
            for j, position in enumerate(line.strip()):
                if position=='@':
                    start_i, start_j = i, j*2
                    row.extend(['@', '.'])
                elif position=='O':
                    row.extend(['[', ']'])
                else:
                    row.extend([position]*2)
                    
            warehouseMap.append(row)

m = len(warehouseMap)
n = len(warehouseMap[0])

def displayMap():
    for i in range(m):
        print("".join(warehouseMap[i]))

def swap(i1, j1, i2, j2):
    warehouseMap[i1][j1], warehouseMap[i2][j2] = warehouseMap[i2][j2], warehouseMap[i1][j1]
    
def getBlocksThatCanBeMoved(i, j, dir):
    [ix, jx] = dir
    temp_i, temp_j = i+ix, j+jx
    
    if warehouseMap[temp_i][temp_j]=='#':
        return False, None, None
    if warehouseMap[temp_i][temp_j]=='.':
        return True, {(i, j)}, {(i, j)}
    if warehouseMap[temp_i][temp_j]==']':
        temp_j-=1
    
    leftPartSuccess, blockEdges, visitedBlocks = getBlocksThatCanBeMoved(temp_i, temp_j, dir)
    if not leftPartSuccess:
        return False, None, None
    rightPartSuccess, rightBlockEdges, rightVisitedBlocks = getBlocksThatCanBeMoved(temp_i, temp_j+1, dir)
    if not rightPartSuccess:
        return False, None, None
    
    blockEdges.update(rightBlockEdges)
    visitedBlocks.add((i, j))
    visitedBlocks.update(rightVisitedBlocks)
    
    return True, blockEdges, visitedBlocks

def moveBlockUp(i, j):
    leftPartSuccess, edges, visited = getBlocksThatCanBeMoved(i, j, [-1, 0])
    if not leftPartSuccess:
        return False
    
    rightPartSuccess, rightEdges, rightVisited = getBlocksThatCanBeMoved(i, j+1, [-1, 0])
    if not rightPartSuccess:
        return False
    
    edges.update(rightEdges)
    visited.update(rightVisited)
    
    for (temp_i, temp_j) in edges:
        while (temp_i, temp_j) in visited:
            swap(temp_i, temp_j, temp_i-1, temp_j)
            temp_i+=1
    return True

def moveBlockDown(i, j):
    leftPartSuccess, edges, visited = getBlocksThatCanBeMoved(i, j, [1, 0])
    if not leftPartSuccess:
        return False
    
    rightPartSuccess, rightEdges, rightVisited = getBlocksThatCanBeMoved(i, j+1, [1, 0])
    if not rightPartSuccess:
        return False
    
    edges.update(rightEdges)
    visited.update(rightVisited)
    
    for (temp_i, temp_j) in edges:
        while (temp_i, temp_j) in visited:
            swap(temp_i, temp_j, temp_i+1, temp_j)
            temp_i-=1
    return True
    
def moveUp(i, j):
    if warehouseMap[i-1][j]=='#':
        return False
    if warehouseMap[i-1][j]=='.':
        swap(i, j, i-1, j)
        return True
    if warehouseMap[i-1][j]=='[':
        if moveBlockUp(i-1, j):
            swap(i, j, i-1, j)
            return True
        return False
    if warehouseMap[i-1][j]==']':
        if moveBlockUp(i-1, j-1):
            swap(i, j, i-1, j)
            return True
        return False
    
def moveDown(i, j):
    if warehouseMap[i+1][j]=='#':
        return False
    if warehouseMap[i+1][j]=='.':
        swap(i, j, i+1, j)
        return True
    if warehouseMap[i+1][j]=='[':
        if moveBlockDown(i+1, j):
            swap(i, j, i+1, j)
            return True
        return False
    if warehouseMap[i+1][j]==']':
        if moveBlockDown(i+1, j-1):
            swap(i, j, i+1, j)
            return True
        return False

def moveLeft(i, j):
    if warehouseMap[i][j-1]=='#':
        return False
    if warehouseMap[i][j-1]=='.':
        swap(i, j, i, j-1)
        return True
    if warehouseMap[i][j-1]==']':
        temp_j = j-1
        while warehouseMap[i][temp_j]!='#' and warehouseMap[i][temp_j]!='.':
            temp_j-=2
        if warehouseMap[i][temp_j]=='.':
            while temp_j <= j-1:
                swap(i, temp_j, i, temp_j+1)
                temp_j+=1
            return True
        return False
    
def moveRight(i, j):
    if warehouseMap[i][j+1]=='#':
        return False
    if warehouseMap[i][j+1]=='.':
        swap(i, j, i, j+1)
        return True
    if warehouseMap[i][j+1]=='[':
        temp_j = j+1
        while warehouseMap[i][temp_j]!='#' and warehouseMap[i][temp_j]!='.':
            temp_j+=2
        if warehouseMap[i][temp_j]=='.':
            while temp_j >= j+1:
                swap(i, temp_j, i, temp_j-1)
                temp_j-=1
            return True
        return False

i, j = start_i, start_j
ignore = None
for direction in tqdm.tqdm(directions):
    
    if direction==ignore:
        continue
    if direction=='^' and moveUp(i, j):
        i, j = i-1, j
        ignore = None
        continue
    if direction=='v' and moveDown(i, j): 
        i, j = i+1, j
        ignore=None
        continue
    if direction=='>' and moveRight(i, j):
        i, j = i, j+1
        ignore=None
        continue
    if direction=='<' and moveLeft(i, j):
        i, j = i, j-1
        ignore=None
        continue
    ignore=direction

displayMap()
sumOfCoords = 0
for i in range(m):
    for j in range(n):
        if warehouseMap[i][j]=='[':
            sumOfCoords+=100*i+j
print(f"ta-da... Coords is {sumOfCoords}")