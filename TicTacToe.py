'''
https://www.jiuzhang.com/problem/tic-tac-toe-oo-design/
'''
import sys

class TicTacToe(object):
    def __init__(self):
        board = []
        currentPlayer = None
        gameEnd = False

    def initialize(self):
        self.gameEnd = False
        self.currentPlayer = 'x'
        self.board = [['-' for i in range(3)] for i in range(3)]

    def isBoardFull(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    return False
        self.gameEnd = True
        return True

    def changePlayer(self):
        self.currentPlayer = 'x' if self.currentPlayer!='x' else 'o'

    def move(self, r, c):
        if self.gameEnd:
            raise ValueError("Game ended.")
        if self.board[r][c] != '-':
            raise ValueError("Spot taken.")
        self.board[r][c] = self.currentPlayer
        win = True
        for i in range(3): #check column
            if self.board[i][c] != self.currentPlayer:
                win = False
                break
        if win:
            self.gameEnd = True
            return win
        win = True
        for i in range(3): #check row
            if self.board[r][i] != self.currentPlayer:
                win = False
                break
        if win:
            self.gameEnd = True
            return win  
        win = True
        for i in range(3): #check diag
            if self.board[i][i] != self.currentPlayer:
                win = False
                break
        if win:
            self.gameEnd = True
            return win
        win = True
        for i in range(3): #check back diag
            if self.board[i][3-1-i] != self.currentPlayer:
                win = False
                break
        if win:
            self.gameEnd = True
            return win
        self.changePlayer()
        if self.isBoardFull():
            raise ValueError("it's a draw")
        return win



if __name__ == "__main__":
    t = TicTacToe()
    t.initialize()
    if len(sys.argv) < 2:
        print("specify case number")
        exit(1)
    case = int(sys.argv[1])
    if case == 0:
        #case 0, draw
        for i in range(3):
            for j in range(3):
                t.move(i,j)
    elif case == 1:
        #case 1
        t.initialize()
        t.move(0,0)
        t.move(0,1)
        t.move(1,1)
        t.move(1,2)
        t.move(2,2)
        t.move(2,1)
    elif case == 2:
        #case 2
        t.initialize()
        t.move(0,0)
        t.move(0,0)
