stone_color = input()
instruction = input()
 
 
start = 0
 
for i in instruction:
 
    if stone_color[start] == i:
 
        start += 1
 
print(start+1)
