# s,a,b = input().split()
s = input()
t = input()
count = 0
for i in range(len(s)):
    if t in s[i:i+len(t)]:             # s.find(t, i, i+len(t)) != -1:
        count += 1
print(count)


pass
