import re

a = input()

digits = re.findall(r"\d", a)
print(" ".join(digits))