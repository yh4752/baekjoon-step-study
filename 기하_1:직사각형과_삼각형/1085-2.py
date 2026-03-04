# 조건을 제대로 확인하지 못해서 삽질함. 위와 같이 풀면 됨.

x,y,w,h = map(int, input().split())

min_dst =  min(x, y, w-x, h-y)

print(min_dst)