import random

class TicTacToeGame:

    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def select_first_player(self):
        return 'X' if random.choice([True, False]) else 'O'

    def place_marker(self, row, col, player):
        self.board[row][col] = player

    def check_winner(self, player):
        for i in range(3):
            if all([self.board[i][j] == player for j in range(3)]) or \
               all([self.board[j][i] == player for j in range(3)]):
                return True
        if all([self.board[i][i] == player for i in range(3)]) or \
           all([self.board[i][2-i] == player for i in range(3)]):
            return True
        return False

    def check_draw(self):
        return all([self.board[i][j] != '-' for i in range(3) for j in range(3)])

    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def change_turn(self, player):
        return 'O' if player == 'X' else 'X'

    def play(self):
        current_player = self.select_first_player()
        print(f"Player {current_player} goes first!")

        while True:
            self.display_board()
            print(f"Player {current_player}'s turn")

            try:
                row, col = map(int, input("Enter row and column (1-3) to place marker: ").split())
                if self.board[row-1][col-1] != '-':
                    print("Spot already taken, try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input, please enter row and column as two numbers between 1 and 3.")
                continue

            self.place_marker(row-1, col-1, current_player)

            if self.check_winner(current_player):
                self.display_board()
                print(f"Player {current_player} wins!")
                break

            if self.check_draw():
                self.display_board()
                print("It's a draw!")
                break

            current_player = self.change_turn(current_player)

if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()
