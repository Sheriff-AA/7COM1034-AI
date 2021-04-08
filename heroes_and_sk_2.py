class HeroSidekicks:
    def start(self):
        return {(x, y): "Left" for x in ["Hero", "Sidekick"] for y in [1, 2]}, "Left"

    def goal(self, state):
        new_state = {(x, y): "Right" for x in ["Hero", "Sidekick"] for y in [1, 2]}, "Right"
        if state == new_state:
            return True
        else:
            return False
        # person_side, boat = state
        # return set(person_side[person] for person in person_side) == {"Right"}

    def successor(self, state):
        characters_pos, boat = state
        # Characters who can be with the boat
        chars_with_boat = [chars[0] for chars in characters_pos.items() if chars[1] == boat]

        for travel_group in select_travellers(chars_with_boat):
            new_positions = characters_pos.copy()
            for traveller in travel_group:
                new_positions[traveller] = switch_sides(characters_pos[traveller])

            new_state = new_positions, switch_sides(boat)

            if safe_state(new_state):
                yield new_state


def select_travellers(characters):
    for a in range(len(characters)):
        yield [characters[a]]

    for i in range(len(characters)):
        for j in range(i+1, len(characters)):
            yield [characters[i], characters[j]]


def switch_sides(side):
    if side == "Right":
        return "Left"
    else:
        return "Right"


def safe_state(state):
    character_pos, _ = state
    for side in ["Left", "Right"]:
        lone_kick = [char for char in character_pos if char[0] == "Sidekick"
                     if character_pos[char] == side if character_pos[("Hero", char[1])] != side]
        hero = [char for char in character_pos if char[0] == "Hero" if character_pos[char] == side]

        if lone_kick and hero:
            return False
    return True


def sort_char(state):
    new_list = sorted(state[0].items())
    return tuple(new_list), state[1]


if __name__ == "__main__":
    def depth_first_search(class_name, state, visited_states):
        vs_node = sort_char(state)
        # b = set([vs_node])
        if vs_node in visited_states:
            # print(set([vs_node]))
            return
        visited_states = visited_states.union(set([vs_node]))

        if class_name.goal(state):
            return [state]
        for successor_state in class_name.successor(state):
            solved = depth_first_search(class_name, successor_state, visited_states)
            if solved:
                return [state] + solved

    def breadth_first_search(instance, paths):
        if not paths:
            return
        candidate = paths.pop(0)
        current_state = candidate[-1]

        if instance.goal(current_state):
            return candidate

        for successor in instance.successor(current_state):
            paths.append(candidate + [successor])

        return breadth_first_search(instance, paths)


    hero_class = HeroSidekicks()
    game = hero_class.start()
    visited = set()
    for path in depth_first_search(hero_class, game, visited):
        print(path)
    print("*" * 100)
    for sol in breadth_first_search(hero_class, [[game]]):
        print(sol)
