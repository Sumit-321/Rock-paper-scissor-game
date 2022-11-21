import random
import flask

app = flask.Flask(__name__)
print("Rock Paper Scissor game")

def game(user_selection):
    user_score= 0
    computer_score= 0
    options_list= ["rock", "paper", "scissor"]
    message_1= "You have selected : " + user_selection.capitalize()
    computer_selection= random.choice(options_list)
    message_2= "Computer selection is : " + computer_selection.capitalize()
    if user_selection== computer_selection:
        message_3 = "This game is a tie."
    elif ((user_selection== "rock" and computer_selection== "scissor") or 
    (user_selection== "paper" and computer_selection== "rock") or (user_selection== "scissor" and computer_selection== "paper")):
        message_3 = "You have won this round. Good!"
        user_score= user_score + 1
    else:
        message_3 = "You have lose this round. Please try again!"
        computer_score= computer_score + 1
    message_3= message_3 + " Your score is " + str(user_score) + " and Computer score is " + str(computer_score) + "."
    return message_1, message_2, message_3, user_score, computer_score

def game_choice():
    user_choice= str(input("Do you want to play the game : Yes or No ? "))
    if user_choice.lower() in "yes":
        game()
        print()
        game_choice()
    elif user_choice.lower() in "no":
        print("Ok")
        return None
    else:
        print("Invalid input")
        game_choice()

@app.route('/', methods=['GET', 'POST'])
def home():
    return flask.render_template("game.html")

@app.route('/game_choice', methods=['GET', 'POST'])
def game_choice():
    data = flask.request.form.to_dict()
    user_selection= list(data.keys())[0]
    user_selection= user_selection.split(".")[0]
    message_1, message_2, message_3, user_score, computer_score= game(user_selection)
    return flask.render_template("game.html", message_1= message_1, message_2= message_2, message_3= message_3, user_score= user_score, computer_score= computer_score)

# Running the application
if __name__ == '__main__':
    app.run(debug= True, port= 8009, threaded= True)