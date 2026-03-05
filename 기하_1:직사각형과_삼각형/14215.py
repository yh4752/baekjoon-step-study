a,b,c = map(int, input().split())

longest = max(a,b,c)

remain = a+b+c-longest
if remain <= longest:
    r = remain-1
    print(remain+r)
else:
    print(a+b+c)