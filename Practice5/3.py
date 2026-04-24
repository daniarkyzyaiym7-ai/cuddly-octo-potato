import re

a = input()
b = input()

matches = re.findall(re.escape(b), a)
print(len(matches))