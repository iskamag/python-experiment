max_mistakes = 0
losing = False
out_of_guesses = False
mistakes = 5
reveal = False
while reveal == False:
    mistakes -= 1
    print("guess the secret word!\nits a red flower")
    print("you got " + str(float(mistakes) + 1) + " more tries")
    secret_word = input()
    if secret_word == "rose" or secret_word == "Rose":
        reveal = True
    elif mistakes == max_mistakes:
        out_of_guesses = True
    elif out_of_guesses == True:
        losing = True
        reveal = True
    else:
        print("try again")
if reveal == True and losing == True:
    print("Game Over")
if reveal == True and losing == False:
    print("Congratulations!\nYou won!")
