# PRODIGY_SD_04
# 🧩 Sudoku Solver GUI (Python + Tkinter)

A simple and interactive Sudoku Solver application built using **Python** and **Tkinter**. It uses the **backtracking algorithm** to solve any valid Sudoku puzzle and updates the GUI with the solution instantly.

![Sudoku Solver](./sudoku%20solver.png)

## 🎯 Features

- Enter your custom Sudoku puzzle.
- Click **Solve Sudoku** to get the solution instantly.
- Uses a **backtracking algorithm** to solve.
- Error handling for unsolvable puzzles.
- Clean and user-friendly GUI.

## 📁 Files

- `sudoku_solver_gui.py` – Main source code that includes GUI + solving logic.
- `sudoku solving (before).png` – Screenshot showing input puzzle before solving.
- `sudoku sloving after.png` – Screenshot showing puzzle after solving.

## ⚙️ How It Works

1. The user fills in the Sudoku board using the GUI.
2. On clicking the **Solve Sudoku** button, the program:
   - Reads the current board input.
   - Solves the puzzle using backtracking.
   - Displays the solution in the same interface.

If the puzzle is unsolvable, an error message is shown.

## 📸 Screenshots

**Before Solving:**

![Before](./sudoku%20solving%20(before).png)

**After Solving:**

![After](./sudoku%20sloving%20after.png)

## 🧠 Technologies Used

- Python 3.x
- Tkinter (GUI)
- Backtracking algorithm (recursive DFS)

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sudoku-solver-gui.git
   cd sudoku-solver-gui
