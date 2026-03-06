import re

a = input()

matches = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", a)
print(len(matches))