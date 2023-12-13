# Import random to use for random int generation
import random
# Roll function from 1-6
def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)
# Function to save top score
def saveTopScore(nickname, TopScore):
    with open("topscore.txt", "w") as file:
        file.write(f"{nickname} - {TopScore}")
# Function to load top score 
def loadTopScore():
    try:
        with open("topscore.txt", "r") as file:
            content = file.read()
            if content:
                nickname, TopScore = content.split(" - ")
                return nickname, int(TopScore)
    except FileNotFoundError:
        pass
    return None, 0

while True:
    playerScore = 0
    current_score = 0
    # Show previous top score to user
    nickname, TopScore = loadTopScore()
    print(f"Top Score: {TopScore} (by {nickname})\n")

    while True:
        # Confirm player wishes to contine rolling 
        should_roll = input("Would you like to continue to roll (y)? ")
        if should_roll.lower() != "y":
            break
        value = roll()
        # Set score to 0 if player rolls a 1
        if value == 1:
            print("You rolled a 1! Turn done!")
            current_score = 0
            break
        # Add roll to current_score if player rolls a number other than 1
        else:
            current_score += value
            print("You rolled a:", value)
        # Print current total score
        print("Your score is:", current_score)
    # Add current score to player_score and display at end of turn
    playerScore += current_score
    print("Your total score is:", playerScore)
    # Check if player score is greater than the top score
    if playerScore > TopScore:
        # If player score greater than top score, ask user if they wish to save their score
        print("Congratulations! You've surpassed the top score!")
        save_score = input("Do you want to save your score? (y/n): ")
        if save_score.lower() == "y":
            nickname = input("Enter your nickname: ")
            # Call function to save top score
            saveTopScore(nickname, playerScore)
            print(f"Top score saved: {nickname} - {playerScore}")
    # Ask user if they wish to play again after their turn ends
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break


