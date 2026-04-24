def square_gen(N):
    for i in range(N + 1):
        yield i ** 2
N = 5
for square in square_gen(N):
    print(square, end=" ")