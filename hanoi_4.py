def move(a, b):
    print("Move form {} to {}".format(a, b))


def hanoi(n, start, target, helper1, helper2):
    if n == 1:
        move(start, target)
        return
    if n == 0:
        pass
    else:
        hanoi(n-2, start, helper2, helper1, target)
        move(start, helper1)
        move(start, target)
        move(helper1, target)
        hanoi(n-2, helper2, target, helper1, start)


hanoi(3, "A", "D", "B", "C")
