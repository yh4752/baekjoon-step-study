n,m = map(int, input().split())

never_seen = set()
never_heard = set()

for _ in range(n):
    never_heard.add(input())

for _ in range(m):
    never_seen.add(input())

never_seen_heard = never_heard.intersection(never_seen)

never_seen_heard_inorder = sorted(never_seen_heard)
print(len(never_seen_heard_inorder))
print("\n".join(never_seen_heard_inorder))