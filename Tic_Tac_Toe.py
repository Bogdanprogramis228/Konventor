import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    # Перевірка рядків
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Перевірка колонок
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Перевірка діагоналей
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Хрестики-Нулики")

        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text=" ", font=('Arial', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            winner = check_winner(self.board)
            if winner:
                messagebox.showinfo("Кінець гри", f"Гравець {winner} переміг!")
                self.reset_game()
            elif is_board_full(self.board):
                messagebox.showinfo("Кінець гри", "Нічия!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Неправильний хід", "Це місце вже зайняте. Спробуйте ще раз.")

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
    