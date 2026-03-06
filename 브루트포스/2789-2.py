n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_value = 0

# 반복문 조건에서 i < j < k가 되도록
# if 문 대신 max 함수로 max_value 결정
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            value = cards[i] + cards[j] + cards[k]
            if value <= m:
                max_value = max(max_value, value)

print(max_value)