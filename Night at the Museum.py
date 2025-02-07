word = input()
 
letters = "abcdefghijklmnopqrstuvwxyz"
 
start = "a"
counter = 0
 
for i in word:
 
    index1 = letters.index(start)
    index2 = letters.index(i)
 
    if abs(index1-index2) >= 13:
 
        counter += (26-abs(index1 - index2))
        start = i
        continue
    
    
    counter += abs(index1-index2)
    start = i
 
 
print(counter)
