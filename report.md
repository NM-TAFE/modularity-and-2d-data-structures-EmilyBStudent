# Refactoring Tic-Tac-O-Oh

The purpose of this report is to explain the decision-making and process of refactoring the Tic-Tac-O-Oh code.

## Refactoring Decisions

I chose to break the code into three main modules, each containing one class: GameManager, Board, and ConsoleUI. This
separated the code by concept and purpose. GameManager handles the main program flow, Board manages game state and data,
and ConsoleUI provides UI code.

[TODO: say more about this]

Separating the UI code from the program flow and game data would make it much easier to use a different UI in future.
If we decided to create a graphical UI for the game instead, the GameManager and Board classes could still be used, and
minimal changes would be needed to connect them to the new UI code.

Rather than deleting the original program code, I initially moved it into the GameManager object. As I refactored parts
of the code, I updated the original code in GameManager to integrate the new changes. This meant that, although the
code in GameManager.main() still needed refactoring, I had a working program at each step of the process. After all
supporting code had been refactored, I finally refactored the main program flow code itself.

I started by building the Board class and its test case before integrating it into the game code. The game board and its
state management are the core of the Tic-Tac-Toe game, so I needed to know how it would work before I could refactor
parts of the code. I wrote the test case alongside each of the methods, so I could be reasonably sure the code was
working well even before I integrated it into the main program code. I then created and integrated the ConsoleUI class.
Knowing how the game data would be stored and used was helpful in deciding how to handle the UI.

The task was only to refactor the code, not to make improvements to the Tic-Tac-Toe gameplay. There are certainly
gameplay improvements that could be made, though. For instance, it would be helpful to give the player more specific
error messages in response to invalid input. In my refactored code, I added several ConsoleUI properties for different
types of error messages to be used in response to various input errors, so more specific error messages could be added
in future.

Another helpful gameplay improvement would be to allow the player to enter their move using row/column coordinates,
instead of the current system of numbering all the spaces consecutively from 0 to 8. I added a Board method to allow for
moves to be specified by row and column number instead of cell number. This will make it easier to add this feature to
the game later. It also allowed me to break up the code for adding a player move, keeping the code for calculating the
move coordinates separate from the code for adding the player's move to the board.

## Challenges Maintaining the Original Code

Since I chose to keep the original game code in place and update it gradually as I refactored the supporting modules, I
encountered much the same challenges as someone would if they were attempting to maintain the original code.

The original code mixed game logic, game state and UI code together in a way that was hard to untangle. It made a lot of
assumptions about how the game data was stored and handled. When I wanted to integrate some of my refactored code, I
sometimes had to rewrite the original code as well, because it made too many assumptions that were no longer valid.
Refactoring the code to use a 2D data structure instead of the original single list was particularly challenging, since
I needed to change all the places where the original code provided direct indexes into the old game data list.

The original code was difficult to understand. A good example is the code that checks for win conditions, which
hardcoded the possible win conditions, and checked the results in a single if statement with three chained equality
operators. If the developer found an error in the win conditions, it would be difficult to identify which of the
hardcoded win condition tuples was at fault. It would also be easy to introduce errors by hardcoding the win conditions
incorrectly.

The original code did not use appropriate error handling, and gave the player limited
feedback on incorrect input. It would not have been easy to add different error messages for different input errors
because all the different kinds of checks on the player's input were mixed together.

Finally, it would have been extremely difficult to extend the original code to create a Tic-Tac-Toe game on a larger
board, or with more than 2 players. The biggest issue is that the win conditions were hardcoded. To use a larger game
board, it would have been extremely time-consuming and error-prone to create the list of all possible win conditions.
After going up a few board sizes, the number of possible winning positions would have been too large for hardcoding them
to be practical.

## Custom-Sized Tic-Tac-Toe Games

To change the game to use a custom-sized tic-tac-toe board, all I would need to do is pass the new board size in when
initialising the game board in GameManager.__init__, e.g.

```python
self.board = Board(5)
```

The methods to check for a winning positions on the board do not assume that the board will be any particular size,
unlike the previous hardcoded win conditions. ConsoleUI's methods also do not assume the board will be any particular
size; they can draw the board to any size, and let the players input moves up to the highest-numbered cell of the board.

However, the old way of specifying the player's move by numbering all the cells on the board consecutively becomes very
difficult for the player to use after going up a board size or two. For larger game boards, it would be preferable to
let the player specify their move by using row/column coordinates. I have already created a function to get an int from
the player's input and a Board method to add the player's move using row/column coordinates. The next step to implement
this would be to change the ConsoleUI.get_current_player_move method to ask the player for first a row number and then a
column number, and pass both these numbers to Board.add_move_by_coordinates.