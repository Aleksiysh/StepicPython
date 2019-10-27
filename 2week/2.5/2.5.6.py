import operator as op
from functools import partial

# sort_by_last = partial(list.sort, key=op.itemgetter(-1))

# x= ['qwe','asa','fdgd']
# sort_by_last(x)
# print(x)


def mod_checker(x, mod=0):
    return lambda y: y % x == mod


mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True
