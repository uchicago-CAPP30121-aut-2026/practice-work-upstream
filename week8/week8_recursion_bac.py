### Recursion Be-A-Computer Problems
### These are the problems that AMR posted on Ed, in a slightly different order
### and with slightly different names.

### Problem 1: What is the output from calling call_mystery()?
def mystery(num):
    if num == 0:
        return 2
    elif num == 2:
        return 1

    if num % 2 == 0:
        return 1 + mystery(num + 1)
    else:
        return 2 + mystery((num - 1) // 2)


def call_mystery1():
    print("Calling mystery1...\n")
    for num in [0, 1, 4, 10]:
        print(f"mystery({num}): {mystery(num)}")
    print()


### Problem 2: What is the output from calling call_luck()?
def luck(lst, acc):
    if lst == []:
        return []
    else:
        first, *rest = lst
        if first % 7 != 0:
            return luck(rest, [first] + acc)
        else:
            return acc


def call_luck():
    print("Calling luck...\n")
    print(luck([17, 2, 9, 14, 0, 7, 15], [7]))
    print()


### Problem 3: What is the output from calling call_mystery_function()?
def mystery_function(lst):
    if lst == []:
        return 0

    first, *rest = lst
    if len(lst) % 2 == 0:
        return first + mystery_function(rest)
    return first - mystery_function(rest)


def call_mystery_function():
    print("Calling mystery function...\n")
    print(f"mystery_function([]): {mystery_function([])}")
    print(f"mystery_function([5]): {mystery_function([5])}")
    print(f"mystery_function([1, 2, 3, 4]): {mystery_function([1, 2, 3, 4])}")
    print(f"mystery_function([10, 11, 12]): {mystery_function([10, 11, 12])}")
    print()



### Problem 4: What is the output from calling call_another_mystery()?
def another_mystery(lst):
    n = len(lst)
    if n == 0:
        return 0

    if n == 1:
        return lst[0] % 2

    if lst[0] == lst[-1]:
        v = lst[n // 2] + 1
    else:
        v = n

    rv = v + another_mystery(lst[1 : n - 1])
    return rv


def call_another_mystery():
    print("Calling another mystery...\n")
    print("another_mystery([])", another_mystery([]))
    print("another_mystery([7])", another_mystery([7]))
    print("another_mystery([6, 2, -1, 3, 2, 6])", another_mystery([6, 2, -1, 3, 2, 6]))
    print("another_mystery([1, 10, 3, 1, 1])", another_mystery([1, 10, 3, 1, 1]))
    print()


### Problem 5: What is the output from calling call_another_mystery()?
def yet_another_mystery(lst, a, b):
    if b == 0:
        return 0
    return lst[a] + yet_another_mystery(lst, lst[a], b - 1)


def call_yet_another_mystery():
    print("Calling yet another myster...\n")
    print(f"yet_another_mystery([2], 0, 1)): {yet_another_mystery([2], 0, 1)}")
    print("yet_another_mystery([1, 3], 0, 1)):", f"{yet_another_mystery([1, 3], 0, 1)}")
    print(
        "yet_another_mystery([4, 1, 0, 1, 2], 2, 3)):",
        f"{yet_another_mystery([4, 1, 0, 1, 2], 2, 3)}",
    )
    print(
        "yet_another_mystery([1, 3, 0, 2], 2, 4)):",
        f"{yet_another_mystery([1, 3, 0, 2], 2, 4)}",
    )
    print()


if __name__ == "__main__":
    call_mystery1()
    call_luck()
    call_mystery_function()
    call_another_mystery()
    call_yet_another_mystery()
