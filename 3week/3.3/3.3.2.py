import re

# print(re.match)
# print(re.search)
# print(re.findall)
# print(re.sub)

pattern = r'a[a-c]c'
string = 'acc'
math_object = re.match(pattern,string)
print(math_object)

string = 'abc,acc,aac,asd'
all_ilusions = re.findall(pattern,string)
print(all_ilusions)

fixed_typeos = re.sub(pattern,'abc',string)
print (fixed_typeos)
