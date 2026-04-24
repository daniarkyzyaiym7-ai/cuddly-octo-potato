def s(n):
    for i in range(1, n + 1):
        yield i * i

n = int(input())
for square in s(n):
    print(square)