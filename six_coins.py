start_node = ["LC", "LC", "LC", "E", "RC", "RC", "RC"]
goal_node = ["RC", "RC", "RC", "E", "LC", "LC", "LC"]


def cleanup(nodes):
    # in-place!!
    # remove dummy entries from begin and end of list
    # clean from the front
    while not nodes[0]:
        nodes.pop(0)
    while not nodes[-1]:
        nodes.pop()


node_d = [1, 2, 1, 2, 1, 2]


def goal(nodes):
    return nodes == [1, 1, 1, 2, 2, 2] or nodes == [2, 2, 2, 1, 1, 1]


def successor(node):
    for i in range(len(node) - 1):  # stop at second last
        # always move two adjacent coins to the right
        if not node[i] or not node[i + 1]:
            # if one of them empty, try other move
            continue
        # try all moves
        for target in range(i + 1, len(node) + 1):
            # print "move from", i, "to", target
            new_node = node[:]  # copy
            doublet = new_node[i:i + 2]
            new_node[i:i + 2] = [0, 0]  # empty them
            new_node.extend([0, 0])  # buffer at the end
            if new_node[target:target + 2] == [0, 0]:
                # target area empty
                new_node[target:target + 2] = doublet
                cleanup(new_node)  # in-place!!
                if new_node == node:
                    continue
                #  print "Successor:", node, new_node
                yield new_node


def breadth_first_search(paths):
    if not paths:
        return
    candidate = paths.pop(0)
    current_state = candidate[-1]

    if goal(current_state):
        return candidate

    for succ in successor(current_state):
        paths.append(candidate + [succ])

    return breadth_first_search(paths)


for sol in breadth_first_search([[node_d]]):
    print(sol)
