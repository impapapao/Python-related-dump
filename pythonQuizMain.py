# to run the game
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------------------------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        print("------------------------------------------------------------------------------")
        guess = input("Enter (A,B,C,D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)

# this function is to check the answers.
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

# this function is to display the result of guesses and the score of the player
def display_score(correct_guesses, guesses):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("results")
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ",end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))* 100)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Your Score is : " + str(score) + "%")

# this function is for when you want to answer the quiz again
def play_again():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

# this is the list of question it uses dictionary for the questions.
questions = {
    "1. Which among the following is not a computer language?": "D",
    "2. A sort malware computer program that keeps replicating\n itself and can easily get diffused into other computer through internet is know as?": "B",
    "3. Consider the following statements:\n a. A file is a characteristically collection of logically related information. \n b. In DOS system, there is a defined technique to put file name. \n Choose the correct answer from the coeds given below:": "C",
    "4. Who among the following designed the first \nelectronic computer namely Electronic Numerical Integrator and Computer?": "D",
    "5. Who among the following has designed the Python programming Lanuage?": "B"
}

# this is a list of choice it uses list for the choices.
options = [
    ["A. ALGOL", "B. COBOL", "C. PASCAL", "D. DRAM"],
["A. Virus", "B. Worms", "C. Trojans", "D. Spyware"],
["A. Only 1", "B. Only 2", "C. Both", "D. Neither 1 nor 2"],
["A. John Mauchly", "B. J. Presper Eckert", "C. Gladeon M. Barnes", "D. A & B both"],
["A. Larry Wall","B. Guido van Rossum", "C. Joe Armstrong", "D. Yukihiro Matsumoto"]
]

new_game()

# this while loop is for play again choices if you type yes in play again function it will restart the game.
while play_again():
    new_game()

print("End game")