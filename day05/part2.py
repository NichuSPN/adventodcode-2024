RULES_INPUT_FILE_NAME = "actual-rules.txt"
UPDATES_INPUT_FILE_NAME = "actual-updates.txt"
# RULES_INPUT_FILE_NAME = "example-rules.txt"
# UPDATES_INPUT_FILE_NAME = "example-updates.txt"

rules = []
with open(f'input/{RULES_INPUT_FILE_NAME}', 'r') as file:
    # Input is in the format of 2 numbers split by |
    for line in file:
        rules.append([int(x) for x in line.strip().split('|')])

updates = []
with open(f'input/{UPDATES_INPUT_FILE_NAME}', 'r') as file:
    # Input is in the format of numbers split by ,
    for line in file:
        updates.append([int(x) for x in line.strip().split(',')])

def getIndex(update, page):
    try:
        return update.index(page)
    except ValueError:
        return -1  
      
def getWrongPageNumbers(update):
    for rule in rules:
        i1, i2 = getIndex(update, rule[0]), getIndex(update, rule[1])
        # If indexes not found skip
        if i1==-1 or i2==-1:
            continue
        # If page not in order return False
        if i1 >= i2:
            return False, [i1, i2]
    return True, None

def swapPages(update, indexes):
    update[indexes[0]], update[indexes[1]] = update[indexes[1]], update[indexes[0]]
    return update

def fixPageNumbers(update, retries=0):
    if retries>(len(updates)+1)/2:
        print(f"Retries crossed {(len(updates)+1)/2} for update {update}!")
        return False, None
    success, indexes = getWrongPageNumbers(update)
    if success:
        return True, update[len(update)//2]
    return fixPageNumbers(swapPages(update, indexes), retries+1)

sumOfMiddlePages = 0
for update in updates:
    success, indexes = getWrongPageNumbers(update)
    if not success:
        # if rule passed get middle page number
        fixed, middlePage = fixPageNumbers(swapPages(update, indexes))
        if fixed:
            sumOfMiddlePages+=middlePage
    
print(f"ta-da... {sumOfMiddlePages} is the sum of middle page numbers of valid updates!")