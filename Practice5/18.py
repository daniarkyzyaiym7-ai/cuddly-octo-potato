import re

a = input()
pattern = input()

matches = re.findall(re.escape(pattern), a)
print(len(matches))