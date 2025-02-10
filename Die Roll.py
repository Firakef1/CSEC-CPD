y, w = map(int, input().split())
 
max_roll = max(y, w)
 
factors_of_six = [1,2,3,6]
 
gcf = 1
 
for i in factors_of_six:
    
    if (7-max_roll)%i == 0:
 
        gcf = i
 
print(f"{int((7-max_roll)/gcf)}/{int(6/gcf)}")
