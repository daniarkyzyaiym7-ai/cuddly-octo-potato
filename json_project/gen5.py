def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = 5
for num in countdown(n):
    print(num, end=" ")