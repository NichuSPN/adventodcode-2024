INPUT_FILE_NAME="actual.txt"

with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    for line in file:
        input = line.strip()

free_spaces = []
mem_blocks = []

all_mem_blocks = []
for i, mem_block_count in enumerate(input):
    mem_block_count = int(mem_block_count)
    if i%2==0:
        all_mem_blocks+=[i//2]*mem_block_count
    else:
        all_mem_blocks+=[None]*mem_block_count

start_position=0
for idx, mem_block_count in enumerate(input):
    mem_block_count=int(mem_block_count)
    if idx%2==0:
        mem_blocks.append({"space": mem_block_count, "start": start_position})
    else:
        free_spaces.append({"space": mem_block_count, "start": start_position})
    start_position+=mem_block_count

def find_free_space(mem_block):
    for idx, block in enumerate(free_spaces):
        if mem_block["start"] < block["start"]:
            break
        if mem_block["space"] <= block["space"]:
            return idx, block
    return -1, None

last_mem_space = len(mem_blocks) - 1
while last_mem_space > 0:
    mem_block = mem_blocks[last_mem_space]
    idx, free_block = find_free_space(mem_block)
    
    if idx==-1:
        last_mem_space-=1
        continue
    
    mem_block_start, mem_block_space = mem_block["start"], mem_block["space"]
    free_block_start, free_block_space = free_block["start"], free_block["space"]
    
    all_mem_blocks[free_block_start:free_block_start+mem_block_space] = [last_mem_space]*mem_block_space
    all_mem_blocks[mem_block_start:mem_block_start+mem_block_space] = [None]*mem_block_space
    
    free_spaces[idx] = {"start": free_block_start+mem_block_space, "space": free_block_space-mem_block_space}    
    last_mem_space-=1

checksum = 0
for idx, mem_block in enumerate(all_mem_blocks):
    if mem_block==None:
        continue
    checksum+=idx*mem_block

print(f"ta-da... the checksum is {checksum}")