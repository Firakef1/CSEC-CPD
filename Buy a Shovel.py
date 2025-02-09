
k, n = map(int, input().split())
 
 
i = 1
 
while (k*i)%10 != 0 and  (k*i - n)%10 != 0:
 
    i+=1
 
print(i)
