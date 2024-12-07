# INPUT_FILE_NAME = 'example.txt'
INPUT_FILE_NAME = 'actual.txt'

input = []
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    # Input is in the format of 5 integers separated by a single space
    for line in file:
        input.append([int(x) for x in line.strip().split(' ')])

def isReportSafe (report, tolerance=1):
    n = len(report)
    direction = None
    failed = False
    for i in range(1, n):
        [prev, curr] = report[i-1:i+1]
        # Check if direction changes or difference is greater than 3 return False
        if curr > prev:
            if direction=='down' or curr-prev > 3:
                failed=True
            direction='up'
        elif curr < prev:
            if direction=='up' or prev-curr > 3:
                failed=True
            direction='down'
        else:
            failed=True
        # Same logic as part one but when failed, 
        # remove the 2 elements in action and check if it is fixed    
        if failed:
            if tolerance > 0:
                return isReportSafe(report[:i]+report[i+1:], 0) or isReportSafe(report[:i+1]+report[i+2:], 0)
            return False
    return True

safeReportsCount=0
for report in input:
    # Automatic type cast of boolean to integer happens
    # Check reverse as well for cases like direction up down down down
    safeReportsCount+=(isReportSafe(report) or isReportSafe(report[::-1]))

print(f"ta-da... {safeReportsCount} safe reports")