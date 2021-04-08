def dfs_heroes(game_class, state_rep):
    if game_class.goal(state_rep):
        return [state_rep]

    for succ in game_class.successor(state_rep):
        sol = dfs_heroes(game_class, succ)
        if sol:
            return [state_rep] + sol
