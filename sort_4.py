def sort4(w, x, y, z):
    new_list = [w, x, y, z]
    min1 = new_list.pop(new_list.index(min(new_list)))
    min2 = new_list.pop(new_list.index(min(new_list)))
    min3 = new_list.pop(new_list.index(min(new_list)))
    min4 = new_list.pop(new_list.index(min(new_list)))

    return min1, min2, min3, min4


if __name__ == "__main__":
    a = sort4(25, 8, 99, 33)
    print(type(a))
    print(a)
