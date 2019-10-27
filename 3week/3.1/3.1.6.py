# s,a,b = input().split()
s = input()
a = input()
b = input()
count = 0
while a in s and count <= 1000:
    s = s.replace(a, b)
    count += 1    

if count > 1000:
    print('Impossible')
else:
    print(count)


pass
