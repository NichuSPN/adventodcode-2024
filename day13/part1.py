import numpy as np
INPUT_FILE_NAME = "actual.txt"
# INPUT_FILE_NAME = "example.txt"

input = []
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    temp = {}
    for i, line in enumerate(file):
        if i%4==0:
            temp['A'] = [int(p[2:]) for p in line.strip()[10:].split(', ')]
        elif i%4==1:
            temp['B'] = [int(p[2:]) for p in line.strip()[10:].split(', ')]
        elif i%4==2:
            temp['C'] = [int(p[2:]) for p in line.strip()[7:].split(', ')]
        else:
            input.append(temp)
            temp = {}

if temp!={}:
    input.append(temp)
    
def valid_count(count):
    return count.is_integer() and 0 <= count <= 100

tokens = 0
for eq in input:
    combinations = np.array(list(zip(eq['A'], eq['B'])))
    result = np.array(eq['C'])
    
    [a, b] = np.linalg.solve(combinations, result)
    a = float('{0:.3f}'.format(a))
    b = float('{0:.3f}'.format(b))
    
    if valid_count(a) and valid_count(b):
        tokens+=(a*3+b)
    
print(f"ta-da... Number of required tokens is {int(tokens)}")