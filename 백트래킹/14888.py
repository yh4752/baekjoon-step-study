n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_value = -10**9
min_value = 10**9
def backtrack(idx, current, plus, minus, mul, div):
    global max_value, min_value

    if idx == n:
        max_value = max(max_value, current)
        min_value = min(min_value, current)
        return
    
    if plus > 0:
        backtrack(idx + 1, current + a[idx], plus - 1, minus, mul, div)
    if minus > 0:
        backtrack(idx + 1, current - a[idx], plus, minus - 1, mul, div)
    if mul > 0:
        backtrack(idx + 1, current * a[idx], plus, minus, mul - 1, div)
    if div > 0:
            if current > 0:
                backtrack(idx + 1, current // a[idx], plus, minus, mul, div - 1)
            else:
                backtrack(idx + 1, -(-current // a[idx]), plus, minus, mul, div - 1)

idx = 1
current = a[0]
backtrack(idx, current, b[0], b[1], b[2], b[3])

print(max_value)
print(min_value)