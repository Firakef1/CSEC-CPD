
n = int(input())

counter = 0
for i in range(n):

    lis = list(input().split())

    if lis.count("1") >= 2:

        counter += 1

print(counter)


