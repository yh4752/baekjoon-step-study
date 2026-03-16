t = int(input())

n = 1000000

prime = [True] * (n+1)
prime[0] = prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = False

for _ in range(t):
    num = int(input())

    count = 0

    for i in range(2, num // 2 + 1):
        if prime[i] and prime[num - i]:
            count += 1
        
    print(count)