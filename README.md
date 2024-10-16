# Bagels_Game
This web application is a guessing game where a player has to guess a three digit number generated by the program. Player has 10 guesses to correctly guess the number.
After each guess, game provides a clue to the player to tell them how close is their guess to the actual number. These clues are explained before the start of the game.

If the player guesses the number within the 10 guesses, they win the game. Else they are provided with the 'You ran out of guesses' message and they lose.

**Technology Stack**

1. **Flask** for backend
2. **MySQL** for storing the users data
3. **HTML** and **CSS** for the frontend

The user's name and the number of guesses taken by them is stored in database 'BagelGame' in a table 'BagelUsers'.
The application reads the user's name from the database to check and avoid users having same name, while the insert query is used to update the table with user name and the number of guesses taken by them to get the actual number.

**Web application layout**

The entry point of the game where the game clues which are useful for the players is explained.

![Screenshot (300)](https://github.com/user-attachments/assets/e364c47d-b5ae-43a4-9324-4628c664def9)

This is the layout of the game, players can see their previous guesses and clues for that guess to make more informed guesses in future.
The last guess is also displayed below the box used for entering the current guess.

![Screenshot (304)](https://github.com/user-attachments/assets/11687ad3-b2b0-4190-b228-d697395546b3)

Layout of webpage after correctly guessing the number chosen by the game.

![Screenshot (306)](https://github.com/user-attachments/assets/e5fcd172-4c9d-4b7f-bb07-b06a9d81f95c)

The webpage to enter the player's name, and throw a message incase name already exists in the database.
![Screenshot (302)](https://github.com/user-attachments/assets/9565d8ec-1ba3-4d29-ab3b-0c3901722bff)





