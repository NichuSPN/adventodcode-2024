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
            while 0<=prevSide_i<m and 0<=prevSide_j<n:
                antinodes[antenna].add((prevSide_i, prevSide_j))
                next_i, next_j = prev_i, prev_j
                prev_i, prev_j = prevSide_i, prevSide_j
                
                prevSide_i, prevSide_j = 2*prev_i-next_i, 2*prev_j-next_j
            
            [prev_i, prev_j] = antennaCoords[i]
            [next_i, next_j] = antennaCoords[j]
            
            nextSide_i, nextSide_j = 2*next_i-prev_i, 2*next_j-prev_j
            while 0<=nextSide_i<m and 0<=nextSide_j<n:
                antinodes[antenna].add((nextSide_i, nextSide_j))
                prev_i, prev_j = next_i, next_j
                next_i, next_j = nextSide_i, nextSide_j
                
                nextSide_i, nextSide_j = 2*next_i-prev_i, 2*next_j-prev_j

allAntinodes = set()

for antennaCoords in input.values():
    for antennaCoord in antennaCoords:
        allAntinodes.add(tuple(antennaCoord))

for antinodesCoords in antinodes.values():
    allAntinodes.update(antinodesCoords)

print("ta-da... Found all coords - A total of ", len(allAntinodes))