import tkinter as tk
from gui import TicTacToeGUI

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()