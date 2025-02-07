

n = int(input())

host_list = []
guest_list = []
for i in range(n):

    host, guest = map(int, input().split())

    host_list.append(host)
    guest_list.append(guest)


counter = 0




for i in host_list:


    if i in guest_list:

        counter += guest_list.count(i)

print(counter)
