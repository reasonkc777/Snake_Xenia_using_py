# Snake Xenia

This is a simple implementation of the classic Snake game using the Pygame library in Python. The game involves controlling a snake to eat food and grow longer while avoiding collisions with the boundaries and itself. The game includes a main menu with options to start or quit the game.

## Setup

To run the game, you need to have Python and Pygame installed. You can install Pygame using pip:

```
pip install pygame
```

## How to Play

- Use the arrow keys to control the direction of the snake.
- The snake will move continuously in the direction it was last directed.
- The objective is to eat the red food blocks to increase the length of the snake.
- Avoid collisions with the boundaries of the game screen and the snake's body.
- Press `1` to start the game from the main menu.
- Press `2` to quit the game from the main menu.

## Code Overview

The code consists of the following components:

- **SnakeGame:** Manages the overall game and contains the main game loop.
- **Snake:** Represents the snake in the game with methods for movement, collision detection, and segment addition.
- **Food:** Represents the food that the snake needs to eat, with methods to generate new food positions.
- **MainMenu:** Manages the main menu for the game.

## Requirements

- Python 3.x
- Pygame

## Running the Game

To run the game, execute the script in a Python environment with Pygame installed. Ensure that the necessary libraries are available before running the script.

```bash
python your_script_name.py
```

## Controls

- Use the arrow keys (up, down, left, right) to control the snake's direction.
- Press `1` to start the game.
- Press `2` to quit the game.

