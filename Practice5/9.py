import re

a = input()

matches = re.findall(r"\b\w{3}\b", a)
print(len(matches))