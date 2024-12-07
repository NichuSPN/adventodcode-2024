# INPUT_FILE_NAME = 'example.txt'
INPUT_FILE_NAME = 'actual.txt'

input = []
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    # Input is in the format of 2 integers separated by 3 spaces
    for line in file:
        input.append([int(x) for x in line.strip().split('   ')])

# zip(*input) will pass every single element in input as individual arguments to zip 
[firstHalf_, secondHalf_] = list(zip(*input))

# Sort both the lists so that while traversing, 
# in each index we get pairs of smallest elements
firstHalf = sorted(firstHalf_)
secondHalf = sorted(secondHalf_)

absSum = 0
# As length of both the arrays will be same...
n = len(firstHalf)
for i in range(n):
    absSum+=abs(firstHalf[i]-secondHalf[i])

print("ta-da... Total Distance...", absSum)