INPUT_FILE_NAME="actual.txt"

with open(f'input/{INPUT_FILE_NAME}', 'r') as file:
    for line in file:
        input = line.strip()
        
mem_blocks = []
for i, mem_block_count in enumerate(input):
    mem_block_count = int(mem_block_count)
    if i%2==0:
        mem_blocks+=[i//2]*mem_block_count
    else:
        mem_blocks+=[None]*mem_block_count

first_free_idx=0
while mem_blocks[first_free_idx]!=None:
    first_free_idx+=1

last_filled_mem_idx = len(mem_blocks) - 1
while mem_blocks[last_filled_mem_idx]==None:
    last_filled_mem_idx-=1

while first_free_idx < last_filled_mem_idx:
    mem_blocks[first_free_idx] = mem_blocks[last_filled_mem_idx]
    mem_blocks[last_filled_mem_idx] = None
    
    while mem_blocks[first_free_idx]!=None:
        first_free_idx+=1
        
    while mem_blocks[last_filled_mem_idx]==None:
        last_filled_mem_idx-=1

checksum = 0
for idx, mem_block in enumerate(mem_blocks):
    if mem_block==None:
        break
    checksum+=idx*mem_block

print(f"ta-da... the checksum is {checksum}")