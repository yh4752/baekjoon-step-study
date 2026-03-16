n = 123456*2

prime = [True] * (n+1)
prime[0] = prime[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = False

def check_prime(a, prime):
    return sum(prime[a+1: 2*a+1])
while True:
    q = int(input())

    if q == 0:
        break

    print(check_prime(q, prime))
