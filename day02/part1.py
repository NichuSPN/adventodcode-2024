# INPUT_FILE_NAME = 'example.txt'
INPUT_FILE_NAME = 'actual.txt'

input = []
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    # Input is in the format of 5 integers separated by a single space
    for line in file:
        input.append([int(x) for x in line.strip().split(' ')])

def isReportSafe (report):
    n = len(report)
    direction = None
    for i in range(1, n):
        [prev, curr] = report[i-1:i+1]
        # Check if direction changes or difference is greater than 3 return False
        if curr > prev:
            if direction=='down' or curr-prev > 3:
                return False
            direction='up'
        elif curr < prev:
            if direction=='up' or prev-curr > 3:
                return False
            direction='down'
        else:
            return False
    return True

safeReportsCount=0
for report in input:
    # Automatic type cast of boolean to integer happens
    safeReportsCount+=isReportSafe(report)

print(f"ta-da... {safeReportsCount} safe reports")