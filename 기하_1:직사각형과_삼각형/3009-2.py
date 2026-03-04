# xor 연산으로 풀기
# xor : 두 값이 다르면 1, 같으면 0

x = 0
y = 0

for _ in range(3):
    ix, iy = map(int, input().split())
    x ^= ix
    y ^= iy

print(x,y)