def even(x):
    return x % 2 == 0


lst = list(map(int, input().split()))
print(list(filter(even,lst)))
