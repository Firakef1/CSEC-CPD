
game_played = int(input())

names = input()

winner = 0
for i in range(game_played):

    if names[i].upper() == "A":

        winner += 1
        continue

    winner -= 1


if winner > 0:

    print("Anton")
elif winner < 0:

    print("Danik")

else:

    print("Friendship")

