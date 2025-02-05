

user_name = input()


charcters = ""

for i in user_name:

    if i not in charcters:

        charcters += i

if len(charcters)%2 == 1:

    print("IGNORE HIM!")
else:

    print("CHAT WITH HER!")



