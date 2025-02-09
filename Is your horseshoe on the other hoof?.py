
color_lis = list(map(int, input().split()))
 
 
temp = []
 
for i in range(4):
 
    if color_lis[i] not in temp:
 
        temp.append(color_lis[i])
        color_lis[i] = None
 
 
print(4-color_lis.count(None))
