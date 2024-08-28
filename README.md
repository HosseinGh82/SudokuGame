# 🧩 Sudoku Solver
Welcome to the Sudoku Solver project! This is a Python implementation of a Sudoku puzzle solver using a backtracking algorithm. The solver can take a partially filled Sudoku grid and fill in the missing numbers to complete the puzzle.

## ✨ Features

🧮 **Sudoku Board Representation**: The Sudoku grid is represented as a 9x9 matrix where 0 represents an empty cell.

🚀 **Backtracking Algorithm**: Efficiently solves the Sudoku puzzle by trying all possible numbers in empty cells while ensuring the Sudoku rules are followed.

✔️ **Validation**: Checks the validity of the number placement according to Sudoku rules (row, column, and 3x3 sub-grid).

📋 **Puzzle Display**: Neatly prints the Sudoku grid before and after solving.


## 🧩 Example
Below is an example of a Sudoku puzzle before and after being solved:

Before:

![Puzzle before solving](https://github.com/user-attachments/assets/0413fb81-ee0e-4e20-b65f-8bcb34e1fa70)


After:

![Puzzle after solving](https://github.com/user-attachments/assets/888bc543-2486-46af-a603-d54002d57da3)


## 🧑‍💻 Code Overview

sudoku_solver.py: Contains the core logic for the Sudoku solver. The Game class is responsible for handling the grid, validating moves, and solving the puzzle using a backtracking approach.

- `printTable()`: Prints the Sudoku grid in a formatted manner.
- `validNum(x, y, number)`: Checks if placing a number at a specific position is valid.
- `solveProblem(x, y)`: Recursively solves the Sudoku puzzle.


## 🛠️ Getting Started

### 📋 Prerequisites

🐍 Python 3.x installed on your system

### 🚀 Running the Solver

1. Clone the repository:

  ```bash
  git clone https://github.com/yourusername/sudoku-solver.git
  cd sudoku-solver
  ```

2. Run the `sudoku_solver.py` file:

  ```bash
  python sudoku_solver.py
  ```
  The program will print the initial Sudoku grid, and then, if solvable, it will print the solved grid.


## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.

1. Fork the repository.
2. Create your feature branch:
   
  ```bash
  git checkout -b feature/your-feature
  ```

3. Commit your changes:
   
  ```bash
  git commit -m 'Add some feature'
  ```

4. Push to the branch:
   
  ```bash
  git push origin feature/your-feature
  ```

5. Open a pull request.
