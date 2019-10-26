lst = [1, 2, 3, 4, 5, 6, 7]
book = {
    'title':'one title',
    'author':'one author',
    'year_publisher':1990
}
string = 'Hello, world'

for i in book:
    print(i)

print()
it = iter(book)
while True:
    try:
        print(next(it))
    except StopIteration:
        break


pass