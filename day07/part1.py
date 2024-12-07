import itertools
import tqdm

# INPUT_FILE_NAME = 'example.txt'
INPUT_FILE_NAME = 'actual.txt'

input = []
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    # Read each line in the file
    for line in file:
        # Print each line
        [k, v] = line.strip().split(': ')
        tempInput = [k]
        tempInput.append([int(x) for x in v.split(' ')])
        input.append(tempInput)
        
def add(x, y): 
    return x+y

def mul(x, y):
    return x*y

combMap = {}

def getCombinations(repeat):
    if str(repeat) in combMap:
        return combMap[str(repeat)]
    combs = list(itertools.product([add, mul], repeat=repeat))
    combMap[str(repeat)] = combs
    return combs

def anyEquationPresent(testValue, numbers):
    n = len(numbers)
    combinations = getCombinations(n-1)
    for comb in combinations:
        evaluated = numbers[0]
        for i in range(n-1):
            evaluated = comb[i](evaluated, numbers[i+1])
        if evaluated==int(testValue):
            return evaluated 
    return 0

totalOfValidValues = 0
for [testValue, numbers] in tqdm.tqdm(input):
    totalOfValidValues+=anyEquationPresent(testValue, numbers)
    
print(f"ta-da... Here is the sum of valid test values: {totalOfValidValues}")