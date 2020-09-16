import random
import sys

cashPrice = 100
stakes = 0
totalEarnings = 0
jackpot = 35
tenPercentBet = 0


def gameMenu():
    print("=*<*>*<*>=* (c)mBot '2020  =*<*>*<*>=* \n")
    print("W=*=E=*=L=*=C=*=O=*=M=*=E\n")
    print("Game Menu \n------------------ ")
    print("                  |__ 1. Coin Flip Game")
    print("                  |______ 2. Cho Han Game")
    print("                  |____________ 3. Card Game")
    print("                  |____________ 4. The Roulette")
    print("                  |______________________ 0. Exit\n")


def getUserInput():
    print("W=*=E=*=L=*=C=*=O=*=M=*=E TO **<>=====******<> COINFLIP **<>=====******<> ")
    print("${} up for Grabs!! \n${}-Stakes\n".format(cashPrice, stakes))
    while True:
        print("Enter your guess: [head or tail] or Enter q to quit:>>> ")
        guess = input(">>> ")
        if guess.lower() == "q":
            print("<>Exiting the console<> \nGoodBye!!")
            sys.exit()
        if guess.lower() == "head" or guess.lower() == "tail":
            print("You chose {}".format(guess))
            break
        print("Enter head or tail or q to quit:>>> ")

    while True:
        print("Place your wager; wager should be a positive value up to the Cash price")
        print("OR enter -1 to Exit")
        try:
            wager = int(input(">>> "))
            if wager == -1:
                print("<>Exiting the console<> \nGoodbye!!")
                print(
                    "\n(c) mBot '2020 *******   CoinFlip Console ***********************")
                sys.exit()
            if wager <= cashPrice:
                print("You have staked ${}".format(wager))
                break
            print("Invalid Input. See Instructions for details.")
        except ValueError:
            print(" **Error** Numeric Input Only!!. See Instructions for details.")
            print("<>Exiting the console<> \nGoodbye!!")
            print("\n(c) mBot '2020 *******   CoinFlip Console ***********************")
            sys.exit()
    print("Activity Summary:\n Guess:--> {} \n Stake:--> ${}".format(guess, wager))
    return (guess, wager)


def coinFlip():
    guess, wager = getUserInput()

    flip = random.randint(1, 2)
    print("Flipping Coin ..........")
    if flip == 1:
        print("The coin lands on head!")
    else:
        print("The coin lands on tail!")

    if guess == "head" and flip == 1:
        totalEarnings = wager + cashPrice
        print("CONGRATULATIONS!!! You just won ${}".format(totalEarnings))
        return wager
    elif guess == "head" and flip != 1:
        print("YOU LOSE!!!! Your wager of ${} is now on the house".format(wager))
        return -wager
    elif guess == "tail" and flip == 1:
        print("YOU LOSE!!!! Your wager of ${} is now on the house".format(wager))
        return -wager
    elif guess == "tail" and flip != 1:
        totalEarnings = wager + cashPrice
        print("CONGRATULATIONS!!! You just won ${}".format(totalEarnings))
        return wager


def testCoinFlip():
    coinFlip()
    print("\n(c) mBot '2020 *******   CoinFlip Console ***********************")


# testCoinFlip()


def getChoHanInput():
    print("W=*=E=*=L=*=C=*=O=*=M=*=E TO **<>=====******<> CHO-HAN **<>=====******<>")
    print("${} up for Grabs!! \n${}-Stakes".format(cashPrice, stakes))
    while True:
        print("Predict the outcome of the dice roll. \nEnter 'even' or 'odd' for predictions OR 'q' to quit: ")
        dicePrediction = input(">>> ")
        if dicePrediction.lower() == "q":
            print("<> Exiting the console<> \nGoodBye!!")
            print(
                "\n(c) mBot '2020 *******   ChoHan Console ***********************")
            sys.exit()
        if dicePrediction.lower() == "even" or dicePrediction.lower() == "odd":
            print("You predicted {}".format(dicePrediction))
            break
        print("Enter a valid input")

    while True:
        print("Place your wager; wager should be a positive value up to the Cash price")
        print("OR enter -1 to Exit")
        try:
            bet = int(input(">>> "))
            if bet == -1:
                print("<>Exiting the console<> \nGoodbye!!")
                print(
                    "\n(c) mBot '2020 *******   ChoHan Console ***********************")
                sys.exit()
            if bet <= cashPrice:
                print("You have staked ${}".format(bet))
                break
            print("Invalid Input. See Instructions for details.")
        except ValueError:
            print(" **Error** Numeric Input Only!!. See Instructions for details.")
            print("<>Exiting the console<> \nGoodbye!!")
            print("\n(c) mBot '2020 *******   ChoHan Console ***********************")
            sys.exit()
    print("Activity Summary:\n Prediction:--> {} \n Stake:--> ${}".format(dicePrediction, bet))
    return (dicePrediction, bet)


def choHan():
    dicePrediction, bet = getChoHanInput()

    diceOne = random.randint(1, 6)
    diceTwo = random.randint(1, 6)
    print("**** Rolling dice *****")
    diceOutcome = diceOne + diceTwo
    print(diceOutcome)

    if dicePrediction == "even" and diceOutcome % 2 == 0:
        totalEarnings = bet + cashPrice
        print("CONGRATULATIONS!!! You just won ${}".format(totalEarnings))
        return bet
    elif dicePrediction == "even" and diceOutcome % 2 != 0:
        print("YOU LOSE!!!! Your bet of ${} is now on the house".format(bet))
        return -bet
    elif dicePrediction == "odd" and diceOutcome % 2 == 0:
        print("YOU LOSE!!!! Your bet of ${} is now on the house".format(bet))
        return -bet
    elif dicePrediction == "odd" and diceOutcome % 2 != 0:
        totalEarnings = bet + cashPrice
        print("CONGRATULATIONS!!! You just won ${}".format(totalEarnings))
        return bet


def testChoHan():
    choHan()
    print("\n(c) mBot '2020 *******   ChoHan Console ***********************")


# testChoHan()


def setupCardGame():
    print("W=*=E=*=L=*=C=*=O=*=M=*=E TO **<>=====******<> CARD GAME **<>=====******<> ")
    print("${} up for Grabs!! \n${}-Stakes".format(cashPrice, stakes))
    player1Name = "House"
    print("Card Player '{}' joined the game".format(player1Name))
    while True:
        print("Enter your screenname or type 'q' to quit:>>>> ")
        player2Name = input(">>> ")
        if player2Name.lower() == "q":
            print("<>Exiting the console<> \nGoodbye!!")
            print("\n(c) mBot '2020 *********** The Card Game ***********************")
            sys.exit()
        if player2Name.lower() != "house":
            break
        print("Invalid Input")

    while True:
        print("{}, place your wager; the wager should be a positive value up to the Cash price".format(
            player2Name))
        print("OR enter -1 to Exit")
        try:
            stake = int(input(">>> "))
            if stake == -1:
                print("<>Exiting the console<> \nGoodbye!!")
                print(
                    "\n(c) mBot '2020 ******* The Card Game ***********************")
                sys.exit()
            if stake <= cashPrice:
                print("You have staked ${}".format(stake))
                break
            print("Invalid Input. See Instructions for details.")
        except ValueError:
            print(" **Error** Numeric Input Only!!. See Instructions for details.")
            print("<>Exiting the console<> \nGoodbye!!")
            print("\n(c) mBot '2020 ******* The Card Game ***********************")
            sys.exit()
    print("**Game Details**\nPlayers:--> \nPlayer1:- {} \nPlayer2:- {} \nStake:--> ${}".format(player1Name, player2Name, stake))
    return (player1Name, player2Name, stake)


def cardGame():
    player1Name, player2Name, stake = setupCardGame()

    cardDeck = list(range(1, 14))

    player1SelectionIndex = random.randint(0, len(cardDeck))
    # extract card
    player1Card = cardDeck[player1SelectionIndex]
    print("{} draws {}".format(player1Name, player1Card))
    cardDeck.pop(player1SelectionIndex)

    player2SelectionIndex = random.randint(0, len(cardDeck))
    # exctract card
    player2Card = cardDeck[player2SelectionIndex]
    print("{} draws {}".format(player2Name, player2Card))
    cardDeck.pop(player2SelectionIndex)

    if player1Card > player2Card:
        print("YOU LOSE!!!! Your stake of ${} is now on the house".format(stake))
        return -stake

    # This cannot occur cos i am popping the cards from the stack.
    elif player1Card == player2Card:
        totalEarnings = stake + 0
        print("Its a tie. Your stake of ${} is intact".format(stake))
        return stake

    else:
        totalEarnings = stake + cashPrice
        print("CONGRATULATIONS!!! You just won ${}".format(totalEarnings))
        return stake


def testCardGame():
    cardGame()
    print("\n(c) mBot '2020 *********** Card Game ***********************")


# testCardGame()


def getRouletteInput():
    print("W=*=E=*=L=*=C=*=O=*=M=*=E TO **<>=====******<> ROULETTE **<>=====******<> ")
    print("***** Welcome to The Roulette.*****")
    print("${} up for Grabs!! \n${}-Stakes".format(cashPrice, stakes))
    print("Enter your Numeric prediction below. Any positive value between 0 and 36 OR Enter 'q' to Quit")
    while True:
        try:
            numericPrediction = int(input(">>> "))
            if numericPrediction == -1:
                print("<>Exiting the console<> \nGoodbye!!")
                print(
                    "\n(c) mBot '2020 *********** The Roulette ***********************")
                sys.exit()
            if numericPrediction > 0 and numericPrediction <= 36:
                print("You Predicted {}".format(numericPrediction))
                break
            print("Invalid Selection; *Positive integers only*")
        except ValueError:
            print("Invalid Selection; *Positive integers only*")

    while True:
        print("Enter Non-numeric Prediction Below: Enter even, odd OR 'q' to QUIT ")

        stringPrediction = input(">>> ")
        if stringPrediction.lower() == 'q':
            print("<>Exiting the console<> \nGoodbye!!")
            print("\n(c) mBot '2020 *********** The Roulette ***********************")
            sys.exit()

        if stringPrediction.lower() == "even" or stringPrediction.lower() == "odd":
            print("You predicted: {}".format(stringPrediction))
            break
        print("Enter 'even', 'odd' or 'q' ")

    while True:
        print(
            "Place your wager; wager should be a positive value greater than [$50] and up to the Cash price")
        print("OR enter -1 to Exit")
        try:
            yourBet = int(input(">>> "))
            if yourBet == -1:
                print("<>Exiting the console<> \nGoodbye!!")
                sys.exit()
            if yourBet > 50 and yourBet <= cashPrice:
                print("You have staked ${}".format(yourBet))
                break
            print("Invalid Input. See Instructions for details.")
        except ValueError:
            print(" **Error** Numeric Input Only!!. See Instructions for details.")
            print("<>Exiting the console<> \nGoodbye!!")
            print("\n(c) mBot '2020 *******   The Roulette ***********************")
            sys.exit()
    print("**** Activity Summary **** \n Numeric Prediction:--> {} \n Non-Numeric:--> {} \n Stake:--> ${}".format(
        numericPrediction, stringPrediction, yourBet))
    return numericPrediction, stringPrediction, yourBet


def roulette():
    numericPrediction, stringPrediction, yourBet = getRouletteInput()

    ball = random.randint(0, 36)
    print("...... ball is spinning\n")
    print("And the ball stops at .............. ", ball)
    print(" =*=*=*=*=* Now Playing for the Jackpot =*=*=*=*=* \n")

    if numericPrediction == ball:
        totalEarnings = yourBet * jackpot + cashPrice
        print("***JACKPOT!!!***, You just won ${} on the Roulette\n".format(totalEarnings))
        return yourBet * jackpot

    elif numericPrediction != ball:
        totalEarnings = yourBet * jackpot + cashPrice
        print("Ouch!!!! You lost out on a Jackpot of ${}. Your stake of ${} is now on the house\n".format(
            totalEarnings, yourBet))
        tenPercentBet = yourBet * 0.1
        print("'10%' of your bet will be applied to the redemption stakes\n")

    print(" =*=*=*=*=* Playing for Redemption =*=*=*=*=*")

    if stringPrediction == "even" and ball % 2 == 0:
        totalEarnings = tenPercentBet + cashPrice * 0.5
        print("CONGRATULATIONS!!! You just won ${}\n".format(totalEarnings))
        return tenPercentBet

    elif stringPrediction == "even" and ball % 2 != 0:
        print("YOU LOSE!!!! Your stake of ${} is now on the house\n".format(
            tenPercentBet))
        return -tenPercentBet

    elif stringPrediction == "odd" and ball % 2 == 0:
        print("YOU LOSE!!!! Your stake of ${} is now on the house\n".format(
            tenPercentBet))
        return -tenPercentBet

    elif stringPrediction == "odd" and ball % 2 != 0:
        totalEarnings = tenPercentBet + cashPrice * 0.5
        print("CONGRATULATIONS!!! You just won ${}\n".format(totalEarnings))
        return tenPercentBet


def testRoulette():
    roulette()


# testRoulette()

def run():
    gameMenu()

    while True:
        print("To Select game, use Menu reference")
        print("Enter 1, 2, 3, 4 to select a game to play OR enter 0 to Exit")
        try:
            gameChoice = int(input(">>>> "))
            if gameChoice == 0:
                print("<>*<> Exiting the console <>*<> \nGoodbye!!")
                print("\n =*<*>*<*>=* (c)mBot '2020  =*<*>*<*>=* ")
                sys.exit()
            if gameChoice == 1:
                coinFlip()
            elif gameChoice == 2:
                choHan()
            elif gameChoice == 3:
                cardGame()
            elif gameChoice == 4:
                roulette()
                break
            print("Refer to the Menu Options\n")
        except ValueError:
            print("Enter a valid input\n")


def instructions():
    pass


run()
