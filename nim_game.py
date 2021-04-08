import random
import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid entry, try again")
        except EOFError:
            sys.exit(1)
        # finally:
        #     print("The finally clause always executes")


def nim_basic(n: int):
    x = 1
    return x


def nim_random(n: int):
    return random.randint(1, min(3, n))


def nim_best(n: int):
    x = n % 4
    if x == 0:      # loosing position, take 1 stick
        return 1
    else:
        return x


def nim_2(n: int):
    x = n % 3
    if x == 0:
        return 1
    else:
        return x


def nim_human(n: int):
    x = getint("Enter a legal number:")
    while x > min(3, n) or x < 1:
        x = getint("Wrong Input! Try again: ")

    return x


def select_two_players():
    players_r = []
    available_players = [nim_basic, nim_random, nim_best, nim_human]
    while len(players_r) != 2:
        for index, values in enumerate(available_players):
            print("{}. {}".format(index + 1, values.__name__))
        input_player = getint("Select a player: ")

        if 0 < input_player <= len(available_players) and available_players[input_player - 1] in available_players:
            players_r.append(available_players[input_player - 1])
            print("{} selected".format(available_players[input_player - 1].__name__))

    return players_r


def game():
    heap_size = getint("Enter a heap size: ")
    print("Select two players")
    players = select_two_players()

    print("Players Selected are: ")
    for i in players:
        print("     {}".format(i.__name__))

    while heap_size > 0:
        for index, y in enumerate(players):
            value = y(heap_size)
            heap_size -= value
            print("Player{} - {} played, {} heap(s) removed. Heap Size is now {}"
                  .format(index + 1, y.__name__, value, heap_size))
            if heap_size == 0:
                print("End of game, Player{} - {} WINS!".format(index + 1, y.__name__))
                break


if __name__ == "__main__":
    game()
