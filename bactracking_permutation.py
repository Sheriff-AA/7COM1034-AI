import sort_4


def permutate(array: list):
    result = []

    if len(array) == 1:
        return [array[:]]

    for i in range(len(array)):
        val = array.pop(0)
        perms = permutate(array)

        for j in perms:
            j.append(val)
        result.extend(perms)
        array.append(val)

    return result


def insertion(e, s):
    for i in range(len(s)+1):
        yield s[:i] + [e] + s[i:]


def perm(s):
    if not s:
        yield []
    else:
        e, s1 = s[0], s[1:]
        for s1p in perm(s1):
            for p in insertion(e, s1p):
                yield p


for pa in perm([1, 2, 3, 4]):
    print(pa)

print("*" * 50)
list1 = [3, 2, 1, 4]
p_list = permutate(list1)

for p in p_list:
    print(p)
# list1.extend([[2, 3]])
# list1.extend([[3, 2]])
# print(list1)
