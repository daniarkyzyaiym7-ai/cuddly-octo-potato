import re

a = input()
if re.match(r"^[A-Za-z].*[0-9]$", a):
    print("Yes")
else:
    print("No")