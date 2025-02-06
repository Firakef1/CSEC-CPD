
calories =  list(map(int, input().split()))
 
game = list(map(int, input()))
 
total_calories = 0
for i in game:
 
    total_calories += calories[i-1]
 
print(total_calories)
