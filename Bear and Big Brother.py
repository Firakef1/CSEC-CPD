a, b = map(int, input().split())

counter = 0
while b >= a:

    a *= 3
    b *= 2

    counter += 1

print(counter)
