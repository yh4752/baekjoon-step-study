"""
	•	check 제거
	•	5000 같은 임시 큰 수 제거
	•	구조 더 명확
    •	5kg를 최대한 많이 쓰는 경우부터 확인
	•	처음 가능한 조합이 최소 봉지 수
"""

n = int(input())

for five in range(n // 5, -1, -1):
    remain = n - 5 * five
    if remain % 3 == 0:
        print(five + remain // 3)
        break
else:
    print(-1)