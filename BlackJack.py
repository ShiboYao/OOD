'''
https://www.jiuzhang.com/problem/black-jack-oo-design/
'''

class Card(object):
    def __init__(self, value):
        self.value = value
    
    def getValue(self):
        return self.value


class Hand(object):
    def __init__(self):
        self.cards = []

    def getPossibleValues(self):
        result = []
        num_ace = 0
        result_without_ace = 0
        for card in self.cards:
            if card.getValue() == 1:
                num_ace += 1
            else:
                result_without_ace += min(card.getValue(), 10)
        for i in range(num_ace + 1):
            result.append(result_without_ace + i + 11*(num_ace-i))
        return result

    def getBestValue(self):
        result = self.getPossibleValues()
        max_under = -1
        for r in result:
            max_under = max(max_under, r if r <= 21 else -1)
        return max_under

    def insertCard(self, card):
        self.cards.append(card)

    def printHand(self):
        cards = [str(c.getValue()) for c in self.cards]
        res = ' , '.join(cards)
        res += ';'
        return res + " Current best value is: " + str(self.getBestValue())

    
class Dealer(object):
    def __init__(self, game):
        self.hand = Hand()
        self.bet = 10000
        self.game = game

    def insertCard(self, card):
        self.hand.insertCard(card)

    def largerThan(self, player):
        return self.hand.getBestValue() >= player.getBestValue()

    def updateBet(self, amount):
        self.bet += amount

    def setGame(self, game):
        self.game = game

    def dealNextCard(self):
        self.insertCard(game.dealNextCard)

    def printDealer(self):
        return "Dealer " + self.hand.printHand() + ", total bet: " + str(self.bet)


class Player(object):
    def __init__(self):
        self.id = None
        self.hand = None
        self.total_bet = None
        self.bet = None
        self.stop_dealing = None
        self.game = None

    def initialize(self, id, bet):
        self.id = id
        self.hand = Hand()
        self.total_bet = 1000
        try:
            self.placeBet(bet)
        except:
            pass
        self.stop_dealing = False

    def getId(self):
        return self.id

    def insertCard(self, card):
        self.hand.insertCard(card)

    def getBestValue(self):
        return self.hand.getBestValue()

    def stopDealing(self):
        self.stop_dealing = True

    def joinGame(self, game):
        game.addPlayer(self)
        self.game = game
        
    def dealNextCard(self):
        self.insertCard(self.game.dealNextCard())

    def placeBet(self, amount):
        if self.total_bet < amount:
            print("No enough money.")
        else:
            self.bet = amount
            self.total_bet -= amount

    def getCurrentBet(self):
        return self.bet

    def printPlayer(self):
        return self.hand.printHand() + ", current bet: " + str(self.bet) + ", total bet: " + str(self.total_bet)

    def win(self):
        self.total_bet += self.bet*2
        self.bet = 0

    def lose(self):
        self.bet = 0


class BlackJack(object):
    def __init__(self):
        self.players = None
        self.dealer = None
        self.cards = None

    def initialize(self, players):
        self.players = players
        self.dealer = Dealer(self)
        self.cards = []

    def initCards(self, cards):
        self.cards = cards

    def addPlayer(self, p):
        self.players.append(p)

    def dealInitialCards(self):
        for p in self.players:
            p.insertCard(self.dealNextCard())
        self.dealer.insertCard(self.dealNextCard())
        for p in self.players:
            p.insertCard(self.dealNextCard())
        self.dealer.insertCard(self.dealNextCard())

    def dealNextCard(self):
        card = self.cards.pop(0) #note this is O(n) in python
        return card

    def getDealer(self):
        return self.dealer

    def compareResult(self):
        for p in self.players:
            if self.dealer.largerThan(p):
                self.dealer.updateBet(p.getCurrentBet())
                p.lose()
            else:
                self.dealer.updateBet(-p.getCurrentBet())
                p.win()

    def printGame(self):
        players = ["playerid: "+str(p.getId())+' ;'+p.printPlayer() for p in self.players]
        return "".join(players)



if __name__ == "__main__":
    p0 = Player()
    p1 = Player()
    p2 = Player()
    p0.initialize(1,10)
    p1.initialize(2,100)
    p2.initialize(3,500)
    cards = [1,4,2,3,1,4,2,3,9,10]
    cards = [Card(c) for c in cards]
    game = BlackJack()
    game.initialize([p0,p1,p2])
    game.initCards(cards)
    
    game.dealInitialCards()
    print(game.printGame())
    print(game.dealer.printDealer())
    game.compareResult()
    print(game.printGame())
    print(game.dealer.printDealer())
