import tqdm

INPUT_FILE_NAME = 'example.txt'
# INPUT_FILE_NAME = 'actual.txt'

input = {}
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    m = 0
    for i, line in enumerate(file):
        m+=1
        n = 0
        for j, letter in enumerate(line.strip()):
            n+=1
            if letter!='.':
                if letter in input:
                    input[letter].append([i, j])
                else:
                    input[letter] = [[i, j]]

antinodes = {}
for antenna in tqdm.tqdm(input):
    antennaCoords = input[antenna]
    antinodes[antenna] = set()
    numberOfAntennas = len(antennaCoords)
    for i in range(numberOfAntennas):
        for j in range(i+1, numberOfAntennas):
            [prev_i, prev_j] = antennaCoords[i]
            [next_i, next_j] = antennaCoords[j]
            
            prevSide_i, prevSide_j = 2*prev_i-next_i, 2*prev_j-next_j
            nextSide_i, nextSide_j = 2*next_i-prev_i, 2*next_j-prev_j
            
            if 0<=prevSide_i<m and 0<=prevSide_j<n:
                if [prevSide_i, prevSide_j] not in antennaCoords:
                    antinodes[antenna].add((prevSide_i, prevSide_j)) 
            
            if 0<=nextSide_i<m and 0<=nextSide_j<n:
                if [nextSide_i, nextSide_j] not in antennaCoords:
                    antinodes[antenna].add((nextSide_i, nextSide_j))

allAntinodes = set()

for antinodesCoords in antinodes.values():
    allAntinodes.update(antinodesCoords)
    
print("ta-da... Found all coords - A total of ", len(allAntinodes))