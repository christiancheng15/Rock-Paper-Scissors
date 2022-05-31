from random import choice
import time
import os

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
os.system("title " + "Rock Paper Scissors by kChris")

def round(num):
    print(f"Round {num}/{q2}")
    user_turn = input(f"{q1}: ")
    while user_turn.lower() not in ["rock", "paper", "scissors"]:
        print("!! PLEASE PICK ROCK, PAPER OR SCISSORS !!")
        user_turn = input(f"{q1}: ")
    print("\nRock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(0.5)
    print("Shoot!\n")
    computer_turn = choice(["Rock", "Paper", "Scissors"])
    print(f"Computer: {computer_turn}\n")
    if user_turn.lower() == computer_turn.lower():
        print("Its a draw!")
        global user_score,computer_score
        user_score += 1
        computer_score += 1
        print(f"\n{q1}: {user_score} | Computer: {computer_score}\n")
    elif user_turn.lower() == "rock" and user_turn.lower() == "paper":
        print("Computer Wins!")
        computer_score += 1
        print(f"\n{q1}: {user_score} | Computer: {computer_score}\n")
    elif user_turn.lower() == "rock" and user_turn.lower() == "scissors":
        print(f"{q1} Wins!")
        user_score += 1
        print(f"\n{q1}: {user_score} | Computer: {computer_score}\n")
    elif user_turn.lower() == "paper" and user_turn.lower() == "rock":
        print(f"{q1} Wins!")
        user_score += 1
        print(f"\n{q1}: {user_score} | Computer: {computer_score}\n")
    elif user_turn.lower() == "paper" and user_turn.lower() == "scissors":
        print("Computer Wins!")
        computer_score += 1
        print(f"\n{q1}: {user_score} | Computer: {computer_score}\n")
    elif user_turn.lower() == "scissors" and user_turn.lower() == "paper":
        print(f"{q1} Wins!")
        user_score += 1
        print(f"\n{q1}: {user_score} | Computer: {computer_score}\n")
    else:
        print("Computer Wins!")
        computer_score += 1
        print(f"\n{q1}: {user_score} | Computer: {computer_score}\n")

def playagain():
    play_again_input = input("Would you like to play again? [y/n] ")
    while play_again_input.lower() not in ["y","n"]:
        print("!! PLEASE ENTER Y/N !!")
        play_again_input = input("Would you like to play again? [y/n] ")
    if play_again_input.lower() == "y":
        play_again = True
        clear()
    else:
        print("Thank you for playing! Program will close in 3 seconds.")
        time.sleep(3)
        exit()

user_score = 0
computer_score = 0

q1 = input("What is your name? ")
q1 = q1.title()

play_again = True
while play_again:
    q2 = input("Number of rounds: ")
    print(f"{q1}, prepare to lose...")
    clear()
    for num in range(1,int(q2)+1):
        round(num)
    if computer_score > user_score:
        print("Computer Wins!")
        playagain()
    elif computer_score < user_score:
        print(f"{q1} Wins!")
        playagain()
    else:
        print(f"Its a draw!")
        playagain()