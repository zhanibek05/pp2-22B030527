import re

txt = input()

pattern0 = r'^a(b)*'
print(re.search(pattern0, txt))

txt = input()

pattern1 = r'^a(b){2-3}'
print(re.search(pattern1, txt))

txt = input()

pattern2 = r'[a-z]+_[a-z]+'
print(re.findall(pattern2, txt))

txt = input()

pattern3 = r'^[A-Z]{1}[a-z]+$'
print(re.search(pattern3, txt))

txt = input()

pattern4 = r'a.(b{1})'
print(re.search(pattern4, txt))

txt = input()

pattern5 = re.sub('[ ,.]', ":",txt)
print(pattern5)

txt = input()

l = []
camel = re.split('_', txt)
for i in camel:
    l.append(i.capitalize())
camel_case = "".join(l)
print(camel_case)

txt = input()

pattern7 = re.split('[A-Z]', txt)
print(pattern7)

txt = input()

pattern8 = re.findall('[A-Z][a-z]*', txt)
for i in pattern8:
    print(i, end=" ")
    
txt = input()

pattern9 = re.findall('[A-Z][a-z]*', txt)
for i in pattern9:
    x = i.lower()
    print(x, end = "_")
    