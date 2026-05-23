# Number Guessing Game 🎯

A simple command-line Number Guessing Game written in Python.

The program generates a random number between **1 and 100**, and the player tries to guess it.  
After each incorrect guess, the score decreases by 10 points.

---

## Features

- Random number generation between 1 and 100
- Input validation
- Score tracking system
- "Too high" / "Too low" hints
- Replay functionality
- Quit anytime using `q`

---

## How the Game Works

1. The game randomly selects a number between **1 and 100**
2. The player enters a guess
3. The game provides feedback:
   - `Too low!`
   - `Too high!`
4. The score starts at **100**
5. Each incorrect guess decreases the score by **10**
6. The game ends when:
   - The player guesses correctly
   - The score reaches 0
   - The player enters `q`

---

## Requirements

- Python 3.12.11

No external libraries are required.

---

## Run the Program

Clone the repository or download the file, then run:

```bash
python solution_a/main.py
```

---

## Example Gameplay

```text
Guess a number between 1 and 100: 50
Too low!

Guess a number between 1 and 100: 75
Too high!

Guess a number between 1 and 100: 63
Congratulations! You guessed the correct number! Your score is 80.
```

---

## Project Structure

```text
NUMBER-GUESSING-GAME/
│
├── solution_a/
│   └── main.py
│
├── solution_b/
│   ├── src/
│       ├── game_logic/
│       │   ├── hint_generator.py
│       │   ├── number_generator.py
│       │   └── scorer.py
│       │
│       ├── utils/
│       │   └── input_validator.py
│       │
│       └── main.py
│    
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Future Improvements

Possible features to add in the future:

- Difficulty levels
- Limited number of attempts
- High score system
- Graphical interface (GUI)
- Multiplayer mode

---

## License


This project is licensed under the MIT License.  
You are free to use, modify, and distribute this software.

For more details, see the `LICENSE` file.