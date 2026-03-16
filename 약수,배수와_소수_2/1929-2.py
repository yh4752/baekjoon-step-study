# 에라토스테네스의 체로 풀기

'''
자기 자신을 제외한 특정 배수를 지움.
이미 지워진건 건너뛰기.
-> 남은 것들은 모두 소수
'''

a, b = map(int, input().split())
n = 1000000

prime = [True] * (n + 1)
prime[0] = prime[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, n + 1, i):
            prime[j] = False

for i in range(a, b+1):
    if prime[i]:
        print(i)          
