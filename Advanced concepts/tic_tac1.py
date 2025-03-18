import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title("Tic-Tac")
player="x"
board=[""]*9
def b_click(b,index):
    global player
    if board[index] == "":
        board[index] = player
        b.config(text=player)
        if check_winner():
            messagebox.showinfo("game done", f"Player {player} wins")
            reset_board()
        elif "" not in board:
            messagebox.showinfo("game over", "draw game")
            reset_board()
        else:
            player = "O" if player == "x" else "x"
def check_winner():
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_patterns)
def reset_board():
    global board, player
    board = [""] * 9
    player ="x"
    for button in buttons:
        button.config(text="")
buttons = []
for i in range(9):
    button = tk.Button(window, text="", height=2, width=5, command=lambda i=i:b_click(buttons[i], i))
    button.grid(row=i//3, column=i%3)
    buttons=buttons+[button]
window.mainloop()