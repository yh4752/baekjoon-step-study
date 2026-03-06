n = int(input())
movies = []

count = 0
num = 666
while True:
    if count == n:
        break
    str_num = str(num)
    
    if '666' in str_num:
        movies.append(num)
        count += 1
    num += 1

print(movies[n-1])

# 굳이 리스트로 할 필요 없음. 메모리 낭비