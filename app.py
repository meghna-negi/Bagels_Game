from flask import Flask, request, redirect, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
import random

app = Flask(__name__)

app.config['MYSQL_HOST'] = '' #Enter the host name
app.config['MYSQL_USER'] = '' #Enter the user name 
app.config['MYSQL_PASSWORD'] = '' #Enter the password
app.config['MYSQL_DB'] = '' #Enter the database name
 
mysql = MySQL(app)
game_data = {}
number_of_guesses = 1


def number_to_be_guessed()->str:
    number = list(range(10))
    random.shuffle(number)
    secret_number = ''
    for num in range(3):
        secret_number += str(number[num])
    return secret_number

actual_number = number_to_be_guessed()

def get_game_clues(actual_number, guessed_number)->str:
    result = ''
    for guess in range(len(guessed_number)):
        if(actual_number[guess] == guessed_number[guess]):
            result += 'Fermi '
        elif(guessed_number[guess] in actual_number):
            result += 'Pico '
    if(len(result)==0):
        result = 'Bagels '
    return result 

@app.route('/')
def game_rules():
    return render_template('homepage.html')

@app.route('/start')
def load_user_page():
    return render_template('userpage.html')

@app.route('/confirm_user')
def add_user():
    username = request.args.get('username')  # Get username from the form
    if username:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        # Inserting the username in the database
        cursor.execute("""
            SELECT * from BagelUsers where UserName = %s
        """,
        (username,))
        user = cursor.fetchone()
        if user:
            cursor.close()
            error = "Username already exists, please choose a different one."
            return render_template('userpage.html',error = error)
            
        return redirect(f'/start_game/{username}')
    else:
        return "Username is required", 400
    

@app.route('/start_game/<username>')
def start_game(username):
     return render_template('gamepage.html',username=username,guessNo=1,clues = '')

@app.route('/start_game/<username>/<guessNo>', methods=['POST'])
def guessing_number(username,guessNo):

    global number_of_guesses
    if username not in game_data:
        game_data[username] = {'guesses': []}

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    print(actual_number)
    
    while(number_of_guesses < 11):
        guessed_number = str(request.form.get('guess'))

        if(actual_number == guessed_number):
            cursor.execute("""
            INSERT INTO BagelUsers (UserName,NoOfGuesses)
            VALUES (%s,%s)
            """,
            (username, number_of_guesses))
            mysql.connection.commit()
            cursor.close()
            print("You have done it!!!!!")
            return render_template('success.html')

        clues = get_game_clues(actual_number,str(guessed_number))
        game_data[username]['guesses'].append({
        'guessno': guessNo,
        'guess': guessed_number,
        'clue': clues
    })
        number_of_guesses = number_of_guesses + 1
        return render_template('gamepage.html',username = username,guessNo= number_of_guesses,clues = clues, guesses=game_data[username]['guesses'] )
        
    print("You ran out of guesses.")
    return redirect('tryagain.html')  
  

if __name__ == "__main__":
    app.run(debug=True)