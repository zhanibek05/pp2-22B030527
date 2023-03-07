import re

text = input()

x = re.findall(r'[a-z]*[A-Z][a-z]*', text)

res = " ".join(x)

print(res)
