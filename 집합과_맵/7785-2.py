n = int(input())

here_set = set()
for _ in range(n):
    name, enter = input().split()

    if enter == "enter":
        here_set.add(name)
    else:
        here_set.remove(name)

here_list = sorted(here_set, reverse=True)

print("\n".join(here_list))