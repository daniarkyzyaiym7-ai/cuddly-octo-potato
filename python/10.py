import re

text = input()

snake = re.sub(r"([A-Z])", r"_\1", text).lower()

print(snake)