def move(a, b):
    print("Move from {} to {}".format(a, b))


def hanoi(n, start, end, helper):
    if n == 0:
        pass
    else:
        hanoi(n-1, start, helper, end)
        move(start, end)
        hanoi(n-1, helper, end, start)


hanoi(2, "A", "Z", "B")
