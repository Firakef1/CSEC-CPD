
n, h = map(int, input().split(" "))

lis = list(map(int, input().split(" ")))

width = 0
for i in lis:
    
    if i <= h:
        
        width += 1
        continue
    
    width += 2
    
print(width)
