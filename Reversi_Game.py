# Wong Kai Lin
# created on 11 April 2019

class ReversiGame:
    def __init__(self):
        self.board_size = 8
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.board[self.board_size // 2 - 1][self.board_size // 2 - 1] = 'X'
        self.board[self.board_size // 2][self.board_size // 2] = 'X'
        self.board[self.board_size // 2 - 1][self.board_size // 2] = 'O'
        self.board[self.board_size // 2][self.board_size // 2 - 1] = 'O'
        self.current_player = 'X'  # 'X' starts first

    def print_board(self):
        print('  1 2 3 4 5 6 7 8')
        print(' +-----------------+')
        for i in range(self.board_size):
            print(f'{i+1}|', end=' ')
            for j in range(self.board_size):
                print(self.board[i][j], end=' ')
            print('|')
        print(' +-----------------+')

    def is_valid_move(self, row, col):
        if not (1 <= row <= self.board_size and 1 <= col <= self.board_size):
            return False
        if self.board[row - 1][col - 1] != ' ':
            return False
        return self.check_flips(row - 1, col - 1)

    def check_flips(self, row, col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        opponent = 'O' if self.current_player == 'X' else 'X'
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == opponent:
                r += dr
                c += dc
                if 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == self.current_player:
                    return True
        return False

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row - 1][col - 1] = self.current_player
            self.flip_pieces(row - 1, col - 1)
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

    def flip_pieces(self, row, col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        opponent = 'O' if self.current_player == 'X' else 'X'
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == opponent:
                r += dr
                c += dc
                if 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == self.current_player:
                    r, c = row + dr, col + dc
                    while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == opponent:
                        self.board[r][c] = self.current_player
                        r += dr
                        c += dc
                    break

    def game_over(self):
        return not any(' ' in row for row in self.board)

    def count_pieces(self):
        count_X = sum(row.count('X') for row in self.board)
        count_O = sum(row.count('O') for row in self.board)
        return count_X, count_O

    def print_winner(self):
        count_X, count_O = self.count_pieces()
        if count_X > count_O:
            print("Player X wins!")
        elif count_O > count_X:
            print("Player O wins!")
        else:
            print("It's a tie!")

    def play_game(self):
        while not self.game_over():
            self.print_board()
            print(f"Current player: {self.current_player}")
            row, col = map(int, input("Enter your move (row col): ").split())
            self.make_move(row, col)
        
        self.print_board()
        self.print_winner()

if __name__ == "__main__":
    game = ReversiGame()
    game.play_game()
