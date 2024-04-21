# Game Logic for AI and Human Player

This project provides a set of functions and classes to manage the logic of a game involving two players (AI vs AI, AI vs Human, or AI vs Monte Carlo simulation). The game is divided into three stages, and the provided functions help handle the various stages and evaluate game states using heuristics.

## Features

- **Print Board**: Displays the current state of the game board.
- **Adjacent Locations**: Provides a list of neighboring positions for a given position on the board.
- **Check for Player's Moves**: Determines if a player can make a mill in the next move.
- **Check for Mill Formation**: Checks if a player has a mill on the given position.
- **Count Pieces**: Counts the number of pieces a player owns on the board.
- **Remove Piece**: Removes a piece from the board and returns updated board states.
- **Possible Moves**: Generates all possible moves for different stages of the game.
- **Minimax Algorithm**: Uses the MiniMax algorithm for decision-making in the game.
- **Monte Carlo Simulation**: Simulates random games for AI decision-making.
- **AI vs AI**: Simulates AI vs AI gameplay.
- **AI vs Human**: Simulates AI vs Human gameplay.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Bilal-Ahmad102/9_men_morris
    ```

2. Navigate to the project directory:

    ```bash
    cd 9_men_morris
    ```

### Usage

- To simulate AI vs AI gameplay, you can use the `AI_VS_AI()` function.
- To simulate AI vs Human gameplay, use the `AI_VS_HUMAN()` function.
- To simulate AI vs Monte Carlo simulation, use the `min_vs_monte()`<repository-name> function.

### Running the Game

You can run the game using the provided functions in the code. For example, to simulate AI vs AI gameplay, run:
    Run `AI_vs_AI` file


## Code Overview

- **printBoard**: Displays the current state of the board.
- **adjacentLocations**: Returns a list of adjacent locations for a given position.
- **isPlayer**: Checks if two positions have the player on them.
- **checkNextMill**: Checks if a player can make a mill in the next move.
- **isMill**: Returns true if a player has a mill on a given position.
- **numOfPieces**: Returns the number of pieces owned by a player.
- **removePiece**: Removes a piece from the board.
- **possibleMoves_stage1, possibleMoves_stage2, possibleMoves_stage3**: Generate possible moves for different stages of the game.
- **possibleMoves_stage2or3**: Checks if the game is in stage 2 or 3 and returns possible moves.
- **minimax**: Implements the MiniMax algorithm for AI decision-making.
- **potentialMillsHeuristic**: A heuristic function to calculate potential mills as a factor.
- **monteCarlo**: Function to perform Monte Carlo simulations.
- **simulateRandomGame**: Simulates random games from a given board position.
- **mc**: Monte Carlo function to select the best move.
