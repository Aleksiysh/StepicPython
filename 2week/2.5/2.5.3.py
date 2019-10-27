# def even(x):
#     return x % 2 == 0

# even = lambda x: x % 2 ==0


lst = list(map(int, input().split()))
print(list(filter(lambda x: x % 2 ==0, lst)))
