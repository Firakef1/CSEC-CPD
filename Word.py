

word =  input()

counter = 0

for i in word:

    if i == i.lower():

        counter += 1


if counter/len(word) < 0.5:

    print(word.upper())

elif counter/len(word) >= 0.5:

    print(word.lower())
