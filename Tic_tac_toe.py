import random

class Board:
    """Represents the Tic-tac-toe game board"""
    def __init__(self) -> None:
        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',        
                      ' ', ' ', ' ']

    def print_board(self):
        """Prints the game board"""
        print()
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('_________')
        print()
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('_________')
        print()
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def update_board(self, position, symbol):
        if self.board[position-1] == ' ':
            self.board[position-1] = symbol
            return True
        else:
            print("Position already occupied!! Choose another position ")
            return False

    def check_winner(self, symbol):
        """Returns True if a player has won the game. Returns False otherwise"""
        if (self.board[0] == symbol and self.board[1] == symbol and self.board[2] == symbol) or \
           (self.board[3] == symbol and self.board[4] == symbol and self.board[5] == symbol) or \
           (self.board[6] == symbol and self.board[7] == symbol and self.board[8] == symbol) or \
           (self.board[0] == symbol and self.board[3] == symbol and self.board[6] == symbol) or \
           (self.board[1] == symbol and self.board[4] == symbol and self.board[7] == symbol) or \
           (self.board[2] == symbol and self.board[5] == symbol and self.board[8] == symbol) or \
           (self.board[0] == symbol and self.board[4] == symbol and self.board[8] == symbol) or \
           (self.board[2] == symbol and self.board[4] == symbol and self.board[6] == symbol):
            return True
        else:
            return False

    def check_draw(self):
        """Returns True if the game has been drawn. Returns False otherwise"""
        if ' ' not in self.board:
            return True

        else:
            return False
      
class Player:
    """Represents a player, with a symbol (typically an X or an O), that will be placed on the board"""
    def __init__(self, symbol) -> None:
        self.symbol = symbol


class Game:
    """Represents a game of Tic-tac-toe"""
    def __init__(self) -> None:

        self.board = Board()
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.current_player = random.choice([self.player1, self.player2])

    def play(self):
        """Initiates a single game of Tic-tac-toe"""
        while True:
            print(f"Current player: {self.current_player.symbol} ")
            position = int(input("Enter the position: "))

            if self.board.update_board(position, self.current_player.symbol):
                self.board.print_board()

                if self.board.check_winner(self.current_player.symbol):
                    print(self.current_player.symbol + ' wins')
                    break
                
                elif self.board.check_draw():
                    print("The game is a Draw")
                    break

                else:
                    if self.current_player == self.player1:
                        self.current_player = self.player2

                    else:
                        self.current_player = self.player1

game = Game()
game.play()
