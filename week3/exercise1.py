"""
Code for Exercise 1 in Week 3 practice problems
"""

A = 2


def f1(d, e):
    d = A + 7
    return d + e


def f2(d):
    return f1(A, d)


def f3(list0, A):
    list0[A] = A * 2


list1 = [2, 5, 7, 10]
b = f2(list1[A])
c = f2(A)
f3(list1, A - 1)
print("A:", A)
print("b:", b)
print("c:", c)
print("list1:", list1)
