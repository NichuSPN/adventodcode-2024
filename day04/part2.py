# INPUT_FILE_NAME = 'example.txt'
INPUT_FILE_NAME = 'actual.txt'

input=[]
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    # Input is in the format of strings in multiple lines
    for line in file:
        input.append(line.strip())
        
m = len(input)
n = len(input[0])
        
def diag1match(i, j):
    print([input[i-1][j-1], input[i-1][j-1]])
    return [input[i-1][j-1], input[i+1][j+1]] in [["M", "S"], ["S", "M"]]

def diag2match(i, j):
    return [input[i-1][j+1], input[i+1][j-1]] in [["M", "S"], ["S", "M"]]

def XMasMatched (i, j):
    return diag1match(i, j) and diag2match(i, j)
    
XMasMatches = 0
for i in range(1, m-1):
    for j in range(1, n-1):
        if input[i][j]=='A':
            XMasMatches+=XMasMatched(i, j)
            
print(f"ta-da... {XMasMatches} number X MAS matched!")

'''
Diag 1 \
Diag 2 /
'''