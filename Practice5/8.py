import re

a = input()  
pattern = input()  

parts = re.split(pattern, a)
print(",".join(parts))