start_stable = ["C", "C", "C", "C", "E", "S", "S", "S", "S"]
goal_stable = ["S", "S", "S", "S", "E", "C", "C", "C", "C"]


def successor(stable):
    # Finds empty spot
    empty = stable.index("E")

    # possible candidate positions
    candidates = [empty-2, empty-1, empty+1, empty+2]

    # update candidates position to be legal
    candidates = [c for c in candidates if 0 <= c < len(stable)]

    candidates = [c for c in candidates if stable[c:c+2] == ["C", "E"]
                  or stable[c-1:c+1] == ["E", "S"]
                  or stable[c:c+3] == ["C", "S", "E"]
                  or stable[c-2:c+1] == ["E", "C", "S"]]

    assert not [c for c in candidates if stable[c] == "E"]
    for c in candidates:
        new_stable = stable[:]
        new_stable[c], new_stable[empty] = new_stable[empty], new_stable[c]

        yield new_stable


def solution(stable):
    if stable == goal_stable:
        return [stable]

    for new_stable in successor(stable):
        sol = solution(new_stable)
        if sol:
            return [stable] + sol


for s in solution(start_stable):
    print(s)
