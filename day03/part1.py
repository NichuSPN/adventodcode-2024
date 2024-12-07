# INPUT_FILE_NAME = 'example.txt'
INPUT_FILE_NAME = 'actual.txt'

inputString = ""
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    # Input is in the format of strings in multiple lines
    for line in file:
        inputString+=line.strip()
        
def evalMul(mulStr):
    # Remove string "mul(" and ")" and split by ','. Return product of 2 integers returned
    [ele1, ele2]=mulStr[4:-1].split(',')
    return int(ele1)*int(ele2)

# Dynamic Import
re = __import__("re")

# Fetch anything that had string "mul(", 2 numbers separated by ',' and ")"
pattern="mul\(\d+,\d+\)"
muls = re.findall(pattern, inputString)

mulSum=0
for mul in muls:
    mulSum+=evalMul(mul)
    
print("ta-da... Summation of multiplication :", mulSum)