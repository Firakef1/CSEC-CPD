
matrix = []

for i in range(5):

    column = list(input().split())

    matrix.append(column)

for i in range(5):

    if "1" in matrix[i]:

        c = matrix[i].index("1")

        print(abs(3-1-c) + abs(3-1-i))

