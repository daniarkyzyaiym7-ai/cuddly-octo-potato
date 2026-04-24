import re

a = input()

matches = re.findall(r"\d{2,}", a)
print(" ".join(matches))