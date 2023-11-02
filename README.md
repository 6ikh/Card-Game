# Card Game 

## Overview

`cardGame.py` is a basic card game program that keeps track of card locations for as many hands as needed. It provides a foundation for building card games where you want to manage the state of the deck, player hands, and computer hands.

## Getting Started

To use this program, you can simply import the `cardGame.py` module into your Python project. The provided functions and variables allow you to simulate card games.

## Code Structure

The code consists of the following components:

- `clearDeck()`: This function initializes the card locations, ensuring that all cards are unassigned to any player or deck.

- `assignCard(y)`: This function assigns a card to the specified player or deck (PLAYER or COMP) by marking its location in the `cardLoc` list.

- `showDeck()`: This function displays the location of all cards, showing which player or deck each card belongs to.

- `showHand(y)`: This function displays the cards in a specific player's hand (PLAYER or COMP).

- `main()`: This is the entry point of the script, where you can call the functions to simulate a card game. It assigns cards to both the player and the computer, shows the deck, and displays each player's hand.

## Variables

The code uses several variables to manage the game:

- `NUMCARDS`: Represents the total number of cards in the deck (52 in a standard deck).

- `DECK`, `PLAYER`, and `COMP`: Constants representing the deck, player, and computer, respectively.

- `cardLoc`: A list to keep track of the location of each card, whether it's in the deck, the player's hand, or the computer's hand.

- `suitName`: A tuple containing the names of the four card suits (hearts, diamonds, spades, clubs).

- `rankName`: A tuple containing the names of the thirteen card ranks (Ace, Two, Three, ..., King).

- `playerName`: A tuple containing the names of entities involved (deck, player, computer).

## Usage

You can use this program to build various card games by calling the functions provided. The `main()` function demonstrates how to use the program by assigning cards, showing the deck, and displaying hands for both the player and computer.

## Example

Here's how you can use the code to simulate a simple card game:

```python
# Import the cardGame module
from cardGame import main

# Start the card game
main()
