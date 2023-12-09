class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.players = {'X': '', 'O': ''}
        self.rounds = 1
        self.max_rounds = 3
        self.player_stats = {'X': {'wins': 0, 'losses': 0}, 'O': {'wins': 0, 'losses': 0}}
        self.moves_history = []

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def is_winner(self):
        return any(all(cell == self.current_player for cell in row) for row in self.board) or \
               any(all(self.board[i][j] == self.current_player for i in range(3)) for j in range(3)) or \
               all(self.board[i][i] == self.current_player for i in range(3)) or \
               all(self.board[i][2 - i] == self.current_player for i in range(3))

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.moves_history.append((row, col, self.current_player))
            return True
        else:
            print("Ungültiger Zug. Das Feld ist bereits belegt. Bitte wähle erneut.")
            return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def undo_move(self):
        if self.moves_history:
            row, col, player = self.moves_history.pop()
            self.board[row][col] = ' '
            self.switch_player()
            print(f"Zug von {player} auf Position ({row}, {col}) wurde rückgängig gemacht.")
        else:
            print("Es gibt keine Züge zum Rückgängig machen.")

    def get_player_names(self):
        self.players['X'] = input("Name des Spielers X: ")
        self.players['O'] = input("Name des Spielers O: ")

    def play_round(self):
        while True:
            self.print_board()
            print(f"{self.players[self.current_player]}, du bist am Zug.")
            print("Optionen:")
            print("1. Mach einen Zug")
            print("2. Mache den letzten Zug rückgängig")
            choice = input("Wähle eine Option (1-2): ")

            if choice == '1':
                row = int(input("Wähle eine Zeile (0-2): "))
                col = int(input("Wähle eine Spalte (0-2): "))
                if self.make_move(row, col):
                    if self.is_winner():
                        self.print_board()
                        print(f"Herzlichen Glückwunsch, {self.players[self.current_player]}! Du hast diese Runde gewonnen!")
                        self.player_stats[self.current_player]['wins'] += 1
                        break
                    elif self.is_board_full():
                        self.print_board()
                        print("Unentschieden! Das Spielfeld ist voll.")
                        break
                    else:
                        self.switch_player()
            elif choice == '2':
                self.undo_move()
            else:
                print("Ungültige Option. Bitte wähle erneut.")

    def play_game(self):
        self.get_player_names()

        while self.rounds <= self.max_rounds:
            print(f"\nRunde {self.rounds}")
            self.play_round()
            self.rounds += 1

        print("\nSpiel beendet.")
        self.print_final_stats()

    def print_final_stats(self):
        print("\nSpielstatistiken:")
        for player, stats in self.player_stats.items():
            print(f"{self.players[player]} - Gewonnen: {stats['wins']}, Verloren: {stats['losses']}")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()