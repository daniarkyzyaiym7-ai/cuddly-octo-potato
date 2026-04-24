import re

a = input()  
b = input()  
c = input()  
result = re.sub(re.escape(b), c, a)
print(result)