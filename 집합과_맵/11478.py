s = input()

length = 1
count = 0
index = 0
s_set = set()
while length <= len(s):
    if index+length > len(s):
        length += 1
        index = 0
    else:
        s_set.add(s[index:index+length])
        index += 1

print(len(s_set))
