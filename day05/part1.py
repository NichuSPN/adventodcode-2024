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
      
def rulesPassed(update):
    for rule in rules:
        i1, i2 = getIndex(update, rule[0]), getIndex(update, rule[1])
        # If indexes not found skip
        if i1==-1 or i2==-1:
            continue
        # If page not in order return False
        if i1 >= i2:
            return False
    return True

sumOfMiddlePages = 0
for update in updates:
    if rulesPassed(update):
        # if rule passed get middle page number
        sumOfMiddlePages+=update[len(update)//2]
    
print(f"ta-da... {sumOfMiddlePages} is the sum of middle page numbers of valid updates!")