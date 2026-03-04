x_list = []
y_list = []
xy_case = []
xy_all_case = []

for _ in range(3):
    x, y = map(int, input().split())
    xy_case.append((x,y))
    if x not in x_list:
        x_list.append(x)
    if y not in y_list:
        y_list.append(y)

for x in x_list:
    for y in y_list:
        xy_all_case.append((x,y))

result = set(xy_all_case) - set(xy_case)
rx,ry = result.pop()
print(rx, ry)

