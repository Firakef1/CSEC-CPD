n = int(input())
 
cards = list(map(int, input().split()))
 
# i made ture stand for sereja playing and false for dima
player = True
 
sereja = 0
dima = 0
 
start, end = 0, n-1
 
while start <= end:
 
    if player:
        player = False
        sereja += max(cards[start], cards[end])
 
    else:
        player = True
        dima += max(cards[start], cards[end])
 
    
    if cards[start] > cards[end]:
        start += 1
    else:
        end -=1
 
print(sereja, dima)
