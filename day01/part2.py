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

similarityScore = 0
# As length of both the arrays will be same...
n = len(firstHalf)
i=j=0
while i<n and j<n:
    currentEle = firstHalf[i]
    currScore = 0
    # While the current element matches with elements in secondHalf,
    # create score for current element
    while j<n and secondHalf[j]==currentEle:
        currScore+=currentEle
        j+=1
    # If the element matches,
    # Add currScore to final score till the current element is the element in firstHalf
    if currScore > 0:
        while i<n and firstHalf[i]==currentEle:
            similarityScore+=currScore
            i+=1
        continue
    # If current second half element is less than current element,
    # move the index of second half to a place where it is no more less than current element
    if secondHalf[j] < currentEle:
        while j < n and secondHalf[j] < currentEle:
            j+=1
        continue
    # If current second half element is greater than current element,
    # move the index of first half to a place where it is no more greater than second half element
    if secondHalf[j] > currentEle:
        while i < n and firstHalf[i] < secondHalf[j]:
            i+=1
        continue
    

print("ta-da... Similarity Score...", similarityScore)