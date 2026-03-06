text = input()

words = text.split("_")

camel = words[0] + "".join(word.capitalize() for word in words[1:])

print(camel)