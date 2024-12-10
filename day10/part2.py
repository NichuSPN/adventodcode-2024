import tqdm

# INPUT_FILE_NAME = "actual.txt"
INPUT_FILE_NAME = "example.txt"

input = []
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    for line in file:
        input.append([int(number) for number in line.strip()])

m = len(input)
n = len(input[0])

trialheadRatings = []
for i in range(m):
    row = [1 if input[i][j]==9 else -1 for j in range(n)]
    trialheadRatings.append(row)

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def pointInBound(i, j):
    return 0<=i<m and 0<=j<n

def findRatings(i, j):
    if trialheadRatings[i][j]!=-1:
        return trialheadRatings[i][j]
    currHeight = input[i][j]
    rating = 0
    for [ix, jx] in dirs:
        inew, jnew = i+ix, j+jx
        if pointInBound(inew, jnew) and input[inew][jnew]==currHeight+1:
            rating+=findRatings(inew, jnew)
    
    trialheadRatings[i][j] = rating
    return rating

totalRatings = 0
for i in tqdm.tqdm(range(m)):
    for j in range(n):
        if input[i][j]==0:
            totalRatings += findRatings(i, j)
            
print(f"ta-da... Total trialhead ratings is {totalRatings}")