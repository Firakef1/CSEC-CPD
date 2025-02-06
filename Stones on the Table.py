n = int(input())
colors = input()
 
 
counter = 0
 
for i in range(n):
    try:
        if colors[i] == colors[i+1]:
 
            counter += 1
    
    except IndexError:
 
        pass
 
print(counter)
