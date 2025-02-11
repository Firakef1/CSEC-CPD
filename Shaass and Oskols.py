wires = int(input())
birds = list(map(int, input().split()))
killed_birds = int(input())
 
 
for i in range(killed_birds):
 
    x, y = map(int, input().split())
 
    if x == wires:
        birds[x-2] += y-1
        birds[x-1] = 0
      
    elif x == 1:
        birds[x] += birds[x-1] - y
        birds[x-1] = 0
      
    else:
        birds[x-2] += y-1
        birds[x] += birds[x-1] - y
        birds[x-1] = 0
 
 
for i in birds:
 
    print(i)
