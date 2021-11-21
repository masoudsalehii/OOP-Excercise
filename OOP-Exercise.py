import random

N = ["Hossein", "Maziyar", "Akbar", "Nima", "Mahdi", "Farhad", "Mohamad", "Khashayar", "Milad", "Mostafa", "Amin", "Saeed", "Pooya", "Pooriya", "Reza", "Ali", "Behzad", "Soheyl", "Behrooz", "Shahrooz", "Saman", "Mohsen"]


class Human:
    def __init__(self, names):
        self.names = names


class foobalist(Human):
    def choose_team(self):
        self.players = []
        #members_of_A:
        self.A = random.sample(self.names, 11)
        for i in self.A:
            self.players.append((i, 'Team A'))
        #members_of_B:
        for i in self.names:
            if i not in self.A:
                self.players.append((i, 'Team B'))
        for i in self.players:
            print("%s: %s"%(i[0], i[1]))


x = foobalist(N)
x.choose_team()
