class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def is_winner(self):
        # Zeilen, Spalten und Diagonalen auf einen Gewinner überprüfen
        return any(all(cell == self.current_player for cell in row) for row in self.board) or \
               any(all(self.board[i][j] == self.current_player for i in range(3)) for j in range(3)) or \
               all(self.board[i][i] == self.current_player for i in range(3)) or \
               all(self.board[i][2 - i] == self.current_player for i in range(3))

    def is_board_full(self):
        # Prüfung ob alle Felder belegt sind
        return all(cell != ' ' for row in self.board for cell in row)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        else:
            print("Ungültiger Zug. Das Feld ist bereits belegt. Bitte wähle erneut.")
            return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while True:
            self.print_board()
            row = int(input(f"Spieler {self.current_player}, wähle eine Zeile (0-2): "))
            col = int(input(f"Spieler {self.current_player}, wähle eine Spalte (0-2): "))

            if self.make_move(row, col):
                if self.is_winner():
                    self.print_board()
                    print(f"Herzlichen Glückwunsch, Spieler {self.current_player}! Du hast gewonnen!")
                    break
                elif self.is_board_full():
                    self.print_board()
                    print("Unentschieden! Das Spielfeld ist voll.")
                    break
                else:
                    self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()