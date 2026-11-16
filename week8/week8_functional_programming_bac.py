### Functional Programming Practice -- be a computer problems
### What is the result of calling each function?  Some of these
### functions do the same task using different constructs.


def mystery1():
    lst = [x * 2 for x in [10, 25, -10, 18, -9]]
    return [x for x in lst if x % 10 == 0]


def mystery2():
    lst = [x for x in [10, 25, -10, 100, -9] if x % 5 == 0]
    return [x * 2 for x in lst]


def mystery3():
    lst = [(1, 2), (2, 3), (4, 9), (2, 1), (3, 1)]
    return [snd - fst for fst, snd in lst]


def mystery4():
    lst = [(1, 2), (2, 3), (4, 9), (2, 1), (3, 1)]
    return list(map(lambda t: t[1] - t[0], lst))


def q(x):
    return x > 3


def mystery5():
    new_lst = [1, 4, -3, 2, -1]
    return [x for x in new_lst if q(x)]


def mystery6():
    new_lst = [1, 4, -3, 2, -1]
    return list(filter(q, new_lst))


def r(fn1, fn2):
    return lambda x: fn1(x) or fn2(x)


def mystery7():
    new_lst = [1, 4, -3, 2, -1]
    return [x for x in new_lst if (x > 3) or (x < 0)]


def mystery8():
    new_lst = [1, 4, -3, 2, -1]
    fn = r(lambda x: x > 3, lambda x: x < 0)
    return [x for x in new_lst if fn(x)]


def mystery9():
    new_lst = [1, 4, -3, 2, -1]
    fn = r(q, lambda x: x < 0)
    return list(filter(fn, new_lst))




def gen_fn(c):
    def fn(x):
        return x % c == 0

    return fn


def mystery10():
    return list(filter(gen_fn(10), map(lambda x: x * 2, [10, 25, -10, 18, -9])))


def mystery11():
    return list(map(lambda x: x * 2, filter(gen_fn(5), [10, 25, -10, 100, -9])))


if __name__ == "__main__":
    for i in range(1, 12):
        fn_call = f"mystery{i}()"
        print(f"{fn_call}: {eval(fn_call)}")
        print()
