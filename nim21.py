print("***HELLO! WELCOME TO NIM-21 GAME***")
player = 1
numberOfCoins = 21              #We have 21 Nim Coins
print("The Total Number of Coins is: ",numberOfCoins)

while True:
        print("Player ",player," is your turn")
        while True:
            choice = int(input("How many coins are you going to pick?, "))
            if choice in [1,2,3] and choice<numberOfCoins :
                    break
            print("you choose the wrong move")
        numberOfCoins = numberOfCoins - choice
        print("Now number of Coins is: ",numberOfCoins)
        if numberOfCoins==1:
            print("Congratulations! Player ", player, " is the Winner!")
            break
        if player==1:
            player=2
        else:
            player=1
print("The Game Over.")
