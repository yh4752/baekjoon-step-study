# 핵심은 리스트. index를 활용하게 되면 n^2의 시간 복잡도가 나올 수 있다.
import sys
input = sys.stdin.readline

# 입력
n = int(input())
num_list = list(map(int, input().split()))

# 1. 중복 제거 + 정렬 + 압축값 부여
num_dict = {num: idx for idx, num in enumerate(sorted(set(num_list)))}

# 2. 원래 순서대로 압축값 출력
print(' '.join(str(num_dict[num]) for num in num_list))