n, m = map(int,input().split())

cards = list(map(int,input().split()))
cards_a = []
cards.sort()
for c in cards:
    if c <= m:
        cards_a.append(c)

max_value = 0
for i in range(0, len(cards_a)):
    for j in range(1, len(cards_a)):
        for k in range(2, len(cards_a)):
            if i < j < k:
                value = cards_a[i]+cards_a[j]+cards_a[k]
                if max_value < value and value <= m:
                    max_value = value

print(max_value)