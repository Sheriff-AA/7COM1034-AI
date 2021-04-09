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
    def depth_first_search(class_name, state, visited_states, counter):
        vs_node = sort_char(state)
        # b = set([vs_node])
        if vs_node in visited_states:
            # print(set([vs_node]))
            return
        visited_states = visited_states.union(set([vs_node]))

        if class_name.goal(state):
            # print(len(visited_states))
            print(counter)
            return [state]
        for successor_state in class_name.successor(state):
            counter += 1
            solved = depth_first_search(class_name, successor_state, visited_states, counter)
            if solved:
                return [state] + solved

    def breadth_first_search(instance, paths, counter):
        counter += 1
        if not paths:
            return
        candidate = paths.pop(0)
        current_state = candidate[-1]

        if instance.goal(current_state):
            print(counter)
            return candidate

        for successor in instance.successor(current_state):
            paths.append(candidate + [successor])

        return breadth_first_search(instance, paths, counter)

    def hero_heuristics(state):
        character_pos, _ = state
        x = [char for char in character_pos if character_pos[char] == "Right"]
        return len(x)

    def sorter(elem):
        a = hero_heuristics(elem[-1])
        b = len(elem) - 1
        return a + b


    def queueing_fn(array):
        x = sorted(array, key=sorter, reverse=True)
        return x

    def best_first_search(instance, paths, visited_states, counter):
        counter += 1
        if not paths:
            return

        path = paths.pop(0)
        curr_state = path[-1]
        toll = sort_char(curr_state)

        if toll in visited_states:
            return best_first_search(instance, paths, visited_states, counter)
        visited_states = visited_states.union(set([toll]))

        if instance.goal(curr_state):
            # print(len(visited_states))
            print(counter)
            return path

        for next_state in instance.successor(curr_state):
            paths.append(path + [next_state])

        paths = queueing_fn(paths)
        return best_first_search(instance, paths, visited_states, counter)


    hero_class = HeroSidekicks()
    game = hero_class.start()
    visited = set()
    count = 0
    empty_list = list()
    for sol in depth_first_search(hero_class, game, visited, count):
        print(sol)

    print("*" * 100)

    for sol in breadth_first_search(hero_class, [[game]], count):
        print(sol)

    print("*" * 100)

    for sol in best_first_search(hero_class, [[game]], visited, count):
        print(sol)
