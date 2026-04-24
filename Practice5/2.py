import re

a = input()
b = input()

if re.search(re.escape(b), a):
    print("Yes")
else:
    print("No")