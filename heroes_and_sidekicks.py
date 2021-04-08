class Hero:
    def start(self):
        return {(person, index): "Left" for person in ["Hero", "Kick"]
                for index in [1, 2, 3]}, "Left"

    def goal(self, state):
        person_side, boat = state
        return set(person_side[person] for person in person_side) == {"Right"}
        # return person_side.values == {"Right"}

    def successor(self, state):
        positions_dict, boat = state
        person_with_boat = [person for person in positions_dict if positions_dict[person] == boat]

        for traveller_group in select_travellers(person_with_boat):
            new_side = positions_dict.copy()
            for traveller in traveller_group:
                new_side[traveller] = other_side(positions_dict[traveller])

            new_state = new_side, other_side(boat)

            if safe(new_state):
                yield new_state


def select_travellers(candidates):
    for x in range(len(candidates)):
        yield [candidates[x]]

    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            yield [candidates[i], candidates[j]]


def safe(state):
    positions_dict, _ = state
    for side in ["Left", "Right"]:
        lone_kick = [number for (character, number) in positions_dict if character == "Kick"
                     if positions_dict[(character, number)] == side
                     if positions_dict[("Hero", number)] != side]
        present_hero = [number for (character, number) in positions_dict if character == "Hero"
                        if positions_dict[(character, number)] == side]

        if lone_kick and present_hero:
            return False
    return True


def other_side(word: str):
    if word == "Left":
        return "Right"
    return "Left"


if __name__ == "__main__":
    state_representation = (
        {("kick", 1): "left",
         ("kick", 3): "left",
         ("kick", 2): "left",
         ("hero", 3): "left",
         ("hero", 2): "left",
         ("hero", 1): "left",
         }, "left"
    )

    persons, _ = state_representation
    print(persons.items())
