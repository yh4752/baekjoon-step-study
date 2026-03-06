a,b,c,d,e,f = map(int, input().split())

y = (c*d - a*f)/(b*d - a*e)
x = (c*e-f*b)/(a*e-b*d)

print(int(x), int(y))