
n = int(input())
 
lis = list(map(int, input().split()))
 
untreated_crimes = 0
 
available_police = 0
 
for i in range(n):
 
    if lis[i] > 0:
 
        available_police += lis[i]
 
    elif lis[i] < 0:
 
        if available_police != 0:
 
            available_police -= 1
        else:
 
            untreated_crimes +=1
 
print(untreated_crimes)
