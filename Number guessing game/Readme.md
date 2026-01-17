# Number Guessing Game 🎲

A simple, interactive Desktop GUI application built with Python and **Tkinter**. This game challenges players to guess a randomly generated secret number within a limited number of attempts, featuring multiple difficulty levels.

## 📖 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Game Modes](#game-modes)
- [Prerequisites](#prerequisites)
- [How to Run](#how-to-run)
- [Screenshots](#screenshots)

## 🧐 About the Project
This project transforms the classic "Guess the Number" command-line game into a graphical user interface (GUI). It utilizes the `random` module to generate numbers and `tkinter` to manage window navigation, button clicks, and user input validation.

## ✨ Features
* **Interactive GUI:** No console required; plays entirely in a window.
* **Dual Difficulty:** Choose between Easy and Hard modes.
* **Smart Feedback:** The game tells you if your guess is "Higher" or "Lower" than the secret number.
* **Attempt Tracking:** Displays remaining attempts in real-time.
* **Input Validation:** Prevents the game from crashing if non-numeric characters are entered.
* **Menu System:** clean navigation between the Main Menu and the Game Screen.

## 🎮 Game Modes

### 🟢 Easy Mode
* **Range:** 1 to 20
* **Attempts Allowed:** 3
* **Best for:** Beginners or quick rounds.

### 🔴 Hard Mode
* **Range:** 1 to 100
* **Attempts Allowed:** 5
* **Best for:** Players who want a challenge.

## ⚙️ Prerequisites
You need **Python 3.x** installed on your system.
* **Tkinter:** This usually comes pre-installed with standard Python distributions.

## 🚀 How to Run
1.  **Download** the file `number guessing game.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the folder containing the script.
4.  Run the following command:
    ```bash
    python "number guessing game.py"
    ```
    *(Note: Use quotes around the filename because it contains spaces)*

## 📂 File Structure
```text
/
└── number guessing game.py   # The main application script
🔮 Future Improvements
Add a "Score" counter to track consecutive wins.

Add a "Play Again" button directly on the game over screen.

Add sound effects for correct/incorrect guesses.