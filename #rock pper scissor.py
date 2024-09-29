#rock pper scissor
import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice
def user_choice(choice):
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)

    result = determine_winner(choice, computer_choice)
    update_scores(result)

    result_label.config(text=f"You chose: {choice}\nComputer chose: {computer_choice}\n{result}")
    scores_label.config(text=f"User Score: {user_score}  Computer Score: {computer_score}")

# Function to update the scores
def update_scores(result):
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

# Create the main window
app = tk.Tk()
app.title("Rock-Paper-Scissors Game")

# Create and configure buttons for user's choices
rock_button = tk.Button(app, text="Rock", command=lambda: user_choice("rock"))
paper_button = tk.Button(app, text="Paper", command=lambda: user_choice("paper"))
scissors_button = tk.Button(app, text="Scissors", command=lambda: user_choice("scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Create and configure labels for displaying results and scores
result_label = tk.Label(app, text="")
scores_label = tk.Label(app, text="User Score: 0  Computer Score: 0")

result_label.pack()
scores_label.pack()

# Run the application
app.mainloop()