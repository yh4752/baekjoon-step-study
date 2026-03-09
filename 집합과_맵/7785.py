n = int(input())

here_set = set()
for _ in range(n):
    name, enter = input().split()

    if enter == "enter":
        here_set.add(name)
    elif enter == "leave":
        here_set.remove(name)

here_list = sorted(list(here_set), reverse=True)

for name in here_list:
    print(name)