import re

a = input()
match = re.search(r"\S+@\S+\.\S+", a)

if match:
    print(match.group())
else:
    print("No email")