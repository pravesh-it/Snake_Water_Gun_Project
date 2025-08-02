# 🐍 Snake, Water, Gun Game

A simple Python implementation of the classic game "Rock, Paper, Scissors," reimagined as "Snake, Water, Gun." Challenge the computer and see if you can outsmart it!

## 🧠 Overview
This project is a command-line Python game where you play against the computer. The game offers three choices:

Snake 🐍

Water 💧

Gun 🔫

The objective is to choose an option that defeats the computer's choice based on the following rules:

Snake 🐍 beats Water 💧

Water 💧 beats Gun 🔫

Gun 🔫 beats Snake 🐍

The game is designed to be simple and fun, perfect for beginners looking to practice Python programming.

## 🚀 Features
Play against the computer

Randomized computer choices

Clear win/loss/draw outcomes

User-friendly command-line interface

## 🛠️ Installation
To run this game, ensure you have Python 3.x installed on your system. No additional libraries are required.

1. Clone the repository:
git clone https://github.com/pravesh-it/Snake-Water-Gun-Project.git
cd Snake-Water-Gun-Project
2. Run the project
python main.py
python main_code_in_shortcut.py

## 🎮 Usage
Upon running the game, you'll be prompted to enter your choice:

Enter your choice: snake
Valid inputs are:

snake

water

gun

After entering your choice, the computer will randomly select its option, and the result will be displayed.

## 🧩 Code Explanation
- The game logic is implemented in Python using the random module to simulate the computer's choice.

- User Input: The game prompts the user to enter their choice.

- Computer Choice: The computer's choice is randomly selected from snake, water, and gun.

- Outcome Determination: A dictionary maps each choice to a unique integer, and the outcome is determined by comparing the user's choice with the computer's.
