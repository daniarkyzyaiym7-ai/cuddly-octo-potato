import re

a = input()

match = re.match(r"Name:\s*(.+),\s*Age:\s*(.+)", a)

if match:
    name, age = match.groups()
    print(name, age)