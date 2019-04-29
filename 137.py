def hangman():
    correct = []
    secret = input("Type the secret phrase here: ")
    low_sec = secret.lower()
    print(low_sec)
    hidden_secret_lst = []
    hidden_secret = ""
    prev_guessed = []
    pgis = ""
    tries = 6
    complete = False

    for char in secret:
        if char != " ":
            hidden_secret_lst += "-"
            hidden_secret += "-"
        else:
            hidden_secret_lst += " "
            hidden_secret += " "

    print(hidden_secret_lst)
    for i in range(10):
        print()

    print('Try to guess a letter in the hidden phrase:')
    print(hidden_secret)

    while complete == False:
        correct.clear()
        print('You have', tries, end=' tries left. ')
        if tries > 0:
            guess = input('Type your guess: ')
            if guess.lower() == low_sec:
                print('The phrase was ', secret, sep="")
                break
            if guess.lower()not in prev_guessed:
                if guess.lower() in low_sec:
                    for char in range(len(low_sec)):
                        if guess.lower() == low_sec[char]:
                            correct.append(char)
                    for item in correct:
                        hidden_secret_lst[item] = guess.lower()
                    hidden_secret = ""
                    for item in hidden_secret_lst:
                        hidden_secret += item
                    prev_guessed.append(guess.lower())
                    if hidden_secret != low_sec:
                        print()
                        print('Guess again.')
                        print(hidden_secret)
                        print('You already guessed: ', pgis, sep=" ")
                else:
                    pgis += guess.lower()
                    pgis += " "
                    tries -= 1
                    prev_guessed.append(guess.lower())
                    print()
                    print('Incorrect')
                    print('Try again.')
                    print('You already guessed: ', pgis, sep=" ")
                    print(hidden_secret)
            else:
                print('You already guessed that letter.')
                print()
                print('Try again.')
                print('You already guessed: ', pgis, sep=" ")
                print(hidden_secret)
        else:
            print(' You are out of tries')
            print('The phrase was ', secret, sep="")
            break
        if hidden_secret == low_sec:
            for i in range(5):
                print()
            complete = True
            print('YOU WON!')
            print('The phrase was: ', secret, sep="")


hangman()


