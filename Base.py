import random


class Cards:
    def __init__(self,suite,value):
        self.suite = suite
        self.value = value

    def re_val(self):
        return self.value

    def re_sui(self):
        return self.suite

    def show(self):
        print("{} of {}".format(self.value, self.suite))



class Deck:

    def __init__(self):
        self.card = []

    def create(self):
            for s in {'Hearts', "Diamonds", "Spades", "Clubs"}:
                for i in range(1, 14):
                    self.card.append(Cards(s, i))

    def show(self):
        for x in self.card:
            x.show()

    def shuffle(self):
        random.shuffle(self.card)

    def draw(self):
        return self.card.pop()


class Player:
    def __init__(self):
        self.hand=[]

    def draw(self,d1):
        self.hand.append(d1.draw())

    def show(self):
        for i in self.hand:
            Cards.show(i)

    def discard(self,n):
        Cards.show(self.hand.pop(n))
