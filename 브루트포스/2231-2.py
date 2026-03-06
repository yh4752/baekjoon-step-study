# 탐색범위 줄이기
"""
핵심: num이 생성자라면, num + digit_sum(num) = n
digit_sum의 최댓값: 9 * 자리수 (cuz, 각 자리 최대가 9이기 때문)
n = 1,000,000 이므로 digit_sum의 최대값은 9 * 7(자릿수) = 63

num + digit_sum(num) = n
==> num = n - digit_sum(num)
==> num >= n - 63 : 즉 생성자는 n-63보다 작을 수 없다

그래서 검사 범위는 n - 9*len(str(n)) 부터면 충분
"""

n = int(input())

start = max(1, n-9*len(str(n)))

for num in range(start, n):
    if num + sum(map(int, str(num))) == n:
        print(num)
        break
else:
    print(0)