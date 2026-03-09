# dict 2개 만들기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_to_name = {}
name_to_num = {}

for i in range(1, n + 1):
    pokemon = input().strip()
    num_to_name[i] = pokemon
    name_to_num[pokemon] = i

for _ in range(m):
    cmd = input().strip()
    if cmd.isdigit():
        print(num_to_name[int(cmd)])
    else:
        print(name_to_num[cmd])
