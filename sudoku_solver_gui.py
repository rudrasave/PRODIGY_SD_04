import tkinter as tk
from tkinter import messagebox

# --- SOLVER LOGIC ---
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# --- GUI LOGIC ---
def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            row.append(int(val) if val.isdigit() else 0)
        board.append(row)
    return board

def set_board(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(board[i][j]))

def solve_puzzle():
    board = get_board()
    if solve(board):
        set_board(board)
    else:
        messagebox.showerror("Error", "No solution exists for this puzzle.")

# --- BUILD GUI ---
root = tk.Tk()
root.title("Sudoku Solver")

entries = [[None for _ in range(9)] for _ in range(9)]

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

for i in range(9):
    for j in range(9):
        entry = tk.Entry(frame, width=2, font=('Arial', 18), justify='center')
        entry.grid(row=i, column=j, padx=2, pady=2)
        entries[i][j] = entry

solve_btn = tk.Button(root, text="Solve Sudoku", command=solve_puzzle)
solve_btn.pack(pady=10)

root.mainloop()
