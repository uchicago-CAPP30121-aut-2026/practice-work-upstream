def f(n, k):
    print(f"start f({n}, {k}")
    lst = [False] * n
    i = -1
    for r in range(n):
        c=0
        while c < k:
            i = (i + 1) % n
            if not lst[i]:
                c += 1
        print("i:", i)
        lst[i] = True
    print(f"end f({n}, {k})")
    return i

x = f(3, 1)
print("x:", x)
print()

y = f(5, 3)
print("y:", y)
