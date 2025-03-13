import random


def create_board(size):
    """Create a game board with the specified size."""
    return [["~"] * size for _ in range(size)]


def print_board(board):
    """Print the game board."""
    for row in board:
        print(" ".join(row))
    print()  # Add a blank line for better readability


def place_ship(board):
    """Randomly place a ship on the board."""
    row = random.randint(0, len(board) - 1)
    col = random.randint(0, len(board) - 1)
    board[row][col] = "S"  # Mark the ship's location
    return (row, col)


def main():
    size = 5
    board = create_board(size)
    ship_location = place_ship(board)
    attempts = 0
    max_attempts = 10
    print("Welcome to Battleship!")

    while attempts < max_attempts:
        print_board(board)
        guess_row = int(input("Guess Row (0-4): "))
        guess_col = int(input("Guess Col (0-4): "))
        attempts += 1

        if (guess_row, guess_col) == ship_location:
            print("Congratulations! You sunk my battleship!")
            break
        elif guess_row < 0 or guess_row >= size or guess_col < 0 or guess_col >= size:
            print("Oops! That's not even in the ocean!")
        elif board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "O":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "O"  # Mark as a miss
            if attempts == max_attempts:
                print("Game Over! You've run out of guesses.")

    print(f"The ship was located at: {ship_location}")
    print_board(board)


if __name__ == "__main__":
    main()