import re

# print(re.match)
# print(re.search)
# print(re.findall)
# print(re.sub)


# . ^ $ * + ? { } [ ] \ | ( ) метасимволы

# [a-zA-Z] диапазоны
# [^a-d] исключение
# \d ~ [0-9]
# \D ~ [^0-9]
# \s ~[\n\t\r\v\f\v] пробельные символы
# \S ~[^\n\t\r\v\f\v] не пробельные символы
# \w ~ [a-zA-Z0-9_] буквы+цифры+_
# \W ~ [^a-zA-Z0-9_] не буквы+цифры+_
# . ~ любой один символ кроме \n
# * любое кол-во символов перед *
# + любое кол-во символов перед + >=1
# ? 0 or 1  кол-во символов перед ?
# {2} 2  кол-во символов перед {2}
# {2,4} от 2 до 4 вхождений символа


pattern = r' english\?'
string = 'Do you speack english?'
math = re.search(pattern,string)
print(math)

pattern = r'ab+a'
string = 'aa,aba,abba'
all_inclusions = re.findall(pattern,string)
print(all_inclusions)
print()
# жадный 
pattern = r'a[ab]+a'
string = 'abaaba'
print(pattern)
print(re.match(pattern,string))
print(re.findall(pattern,string))

print()
pattern = r'a[ab]+?a'
print(pattern)
print(re.match(pattern,string))
print(re.findall(pattern,string))
