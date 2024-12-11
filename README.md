# Tic Tac Toe Game

A simple, interactive Tic Tac Toe game built using Python and Tkinter.

## Features
- **Two Player Gameplay**: Play against yourself, alternating between `X` and `O`.
- **Random Player Start**: The game randomly selects which player goes first (`X` or `O`).
- **Win/Tie Detection**: The game highlights winning moves and announces ties.
- **Play Again**: Reset the board and start a new game with the "Play Again" button.
- **Responsive UI**: Buttons change color dynamically to indicate the game's state.

## Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)
- An icon file for the window (optional, replace with a valid path).

## How to Run
1. Clone or download this repository.
2. Make sure Python is installed on your system.
3. Run the Python script:

    ```bash
    python tictactoe.py
    ```

4. The game window will open, and you can start playing.

## Gameplay Instructions
1. The game begins with a random player (`X` or `O`).
2. Players take turns clicking on empty squares to mark their symbol.
3. The first player to align three symbols in a row, column, or diagonal wins.
4. If all squares are filled and no one wins, the game ends in a tie.
5. Click the "Play Again" button to reset the game and start over.

## Code Highlights
- **Dynamic Player Turns**: Uses the `next_turn` function to manage player switching and update the UI.
- **Winner/Tie Detection**: Includes comprehensive checks for rows, columns, and diagonals to determine the game's outcome.
- **Random Start**: The starting player is chosen randomly at the start of each game using Python's `random` module.
- **Custom Styling**: The game window and buttons are styled with custom colors, fonts, and button reliefs.

## File Structure
```plaintext
tictactoe.py  # Main game script
```

## Screenshot
![image at](https://github.com/0maaz-01/Tic-Tac-Toe/blob/main/Image/Tic%20Tac%20.png)


## License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute.

---
