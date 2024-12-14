INPUT_FILE_NAME = "actual.txt"
m, n = 103, 101
# INPUT_FILE_NAME = "example.txt"
# m, n = 7, 11

input = []
with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    for line in file:
        [start, vel] = line.strip().split(' ')
        input.append({"start": [int(x) for x in start[2:].split(',')],
                      "velocity": [int(x) for x in vel[2:].split(',')]}) 

positions = []
for i in range(m):
    t = []
    for j in range(n):
        t.append(0)
    positions.append(t)
    
seconds = 100
for robot in input:
    [start_x, start_y] = robot["start"]
    [vel_x, vel_y] = robot["velocity"]
    
    x_after_10s = (start_x + 100*vel_x)%n
    y_after_10s = (start_y + 100*vel_y)%m
    positions[y_after_10s][x_after_10s]+=1
    
q1 = 0
q2 = 0
for i in range(m//2):
    q1+=sum(positions[i][:n//2])
    q2+=sum(positions[i][n//2+1:])

q3 = q4 = 0
for i in range(m//2+1, m):
    q3+=sum(positions[i][:n//2])
    q4+=sum(positions[i][n//2+1:])
    
safetyFactor = q1*q2*q3*q4
print(f"ta-da... The safety Factor is {safetyFactor}")