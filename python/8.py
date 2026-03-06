import re

text = input()

result = re.findall(r"[A-Z][^A-Z]*", text)

print(result)