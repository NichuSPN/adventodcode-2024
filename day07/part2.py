import itertools
import tqdm

# INPUT_FILE_NAME = 'example.txt'
INPUT_FILE_NAME = 'raminput.txt'

input = []
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    # Read each line in the file
    for line in file:
        # Print each line
        [k, v] = line.strip().split(': ')
        tempInput = [k]
        tempInput.append(v.split(' '))
        input.append(tempInput)
        
combMap = {}
        
def getCombinations(ops, repeat, concatReq=False):
    searchStr = str(repeat)
    if concatReq:
        searchStr+='|'
    if searchStr in combMap:
        return combMap[searchStr]
    combs = list(itertools.product(ops, repeat=repeat))
    if concatReq:
        combs = [comb for comb in combs if '|' in comb]
    combMap[searchStr] = combs
    return combs
        
def evalOp (x, op, y):
    if op=='+':
        return str(int(x)+int(y)) 
    if op=='*':
        return str(int(x)*int(y)) 
    if op=='|':
        return x+y
    
def combineNumbersWithOps(numbers, opsComb):
    n = len(numbers)
    eq = numbers[:1]
    for i in range(n-1):
        eq.append(opsComb[i])
        eq.append(numbers[i+1])
    return eq

evalMemo = {}

def evaluateEquation(eq):
    searchStr = ''.join(eq)
    if searchStr in evalMemo:
        return evalMemo[searchStr]
    if len(eq)==3:
        result = evalOp(*eq)
        evalMemo[searchStr] = result
        return result
    result = evalOp(evaluateEquation(eq[:-2]), eq[-2], eq[-1])
    evalMemo[searchStr] = result
    return result

def anyEquationPassed(testValue, numbers, combinations):
    for comb in combinations:
        eq = combineNumbersWithOps(numbers, comb)
        if evaluateEquation(eq)==testValue:
            return int(testValue)
    return 0

validInIteration1 = []
for [testValue, numbers] in tqdm.tqdm(input):
    combinations = getCombinations(['+', '*'], len(numbers)-1)
    if anyEquationPassed(testValue, numbers, combinations) > 0:
        validInIteration1.append(testValue)

evalMemo = {}
totalOfOtherValidValues = 0
for [testValue, numbers] in tqdm.tqdm(input):
    if testValue in validInIteration1:
        continue
    combinations = getCombinations(['+', '*', '|'], len(numbers)-1, True)
    totalOfOtherValidValues+=anyEquationPassed(testValue, numbers, combinations)

finalResult = sum([int(x) for x in validInIteration1])+totalOfOtherValidValues
print(f"ta-da... Here is the sum of valid test values: {finalResult}")