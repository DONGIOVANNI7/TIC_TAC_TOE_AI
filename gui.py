import tkinter as tk
from tkinter import messagebox
from game import TicTacToeAI

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe - AI")
        self.game_ai = TicTacToeAI()
        self.current_player = "O"  # Human starts first
        self.buttons = []
        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        
        # Create 3x3 grid of buttons
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.frame, text="", font=('Arial', 20), width=5, height=2,
                                 command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)
        
        # Reset button
        self.reset_btn = tk.Button(self.master, text="New Game", command=self.reset_game)
        self.reset_btn.pack(pady=10)

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "O"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state=tk.NORMAL)

    def on_click(self, row, col):
        if self.board[row][col] == "" and self.current_player == "O":
            self.make_move(row, col, "O")
            
            if not self.check_game_over():
                self.ai_move()

    def ai_move(self):
        row, col = self.game_ai.best_move(self.board)
        self.make_move(row, col, "X")
        self.check_game_over()

    def make_move(self, row, col, player):
        self.board[row][col] = player
        self.buttons[row][col].config(text=player, state=tk.DISABLED)
        self.current_player = "X" if player == "O" else "O"

    def check_game_over(self):
        winner = self.game_ai.get_winner(self.board)
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.reset_game()
            return True
        if all(all(cell != "" for cell in row) for row in self.board):
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
            return True
        return False