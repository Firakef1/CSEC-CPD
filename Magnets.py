n =  int(input())
 
counter = 1
sets = ""
for i in range(n):
 
    magnet = input()
    if len(sets) == 0 or sets[-1] != magnet[0]:
 
        sets+=magnet
        continue
 
    sets+=magnet
    counter+=1
 
print(counter)
