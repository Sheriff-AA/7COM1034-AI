class Game:
    def start(self):
        pass

    def goal(self, state):
        pass

    def succ(self, state):
        pass


list1 = [[(1, 2, 3)]]
x = list1.pop(0)
print(x)

list1.append(x + [(2, 8, 3)])
print(list1)
