#Variables and Imported Random
import random
choice = ""
Coin = 0
Score = 0
Lost = ""
Breaker = "GAME ON"
NumPlayers = 0
#RulesOfTheGame
def rules():
    print("***WELCOME TO FLIP COIN GAME***\n**RULES OF THE GAME**\n1. MAXIMUM PLAYERS ALLOWED ON THIS GAME WILL BE 4.\n2. MINIMUM PLAYERS ALLOWED ON THIS GAME WILL BE 2.\n3. CHOICES ARE ONLY [1] HEADS OR [2] TAILS\n4. ONLY UP TO 10 ROUNDS\n(IF STILL NO ONE WINS on ROUND 10, THE GAME WILL RESET.)")
#PrintingOfDictionary(Players)
def Print(Player):
    for x,y in Player.items():
        print(x,":",y)

#AlphaValidationFunction
def AlphaVali(val,Type,Pnum):
    while True:
        if Type == 1:
            print("PLAYER [",Pnum,"]\n[A] Heads\n[B] Tails\n>> ")
            val = input("")
            if val.isalpha()==False:
                print("**INVALID INPUT!**\n***LETTERS ONLY!***")
                continue
            if val not in "AaBb":
                print("**Not on the choices!**\n***PLEASE TRY AGAIN!***")
                continue
            else:
                if val in "Aa" :
                    return 1
                elif val in "Bb" :
                    return 2
        if Type == 2:
            print("Do you want another game? Y/N\n>> ")
            val = input("")
            if val.isalpha()==False:
                print("**INVALID INPUT!**\n***LETTERS ONLY!***")
                continue
            elif val not in "YyNn":
                print("**Not on the choices!**\n***PLEASE TRY AGAIN!***")
                continue
            else:
                if val in "Yy":
                    return "Y"
                elif val in "Nn":
                    return "N"
        break
        
#TossCoinFunction
def TossCoin(coin,Type):
    if Type == 1:
        coin = random.randint(1,2)
        return coin
    elif Type == 2:
        if coin == 1:
            return "Heads"
        elif coin == 2:
            return "Tails"

#WinnerValidation
def WinnerVali(Player):
    for x in Player:
        if Player[x]!="OUT":
            return x

#LosserValidation
def LosserVali(Player,Score):
        if Player == "NOMINATED" or Player == "OUT":
                return "OUT"
        else:
            return Score
#QuantityVali
def QuantiVali(Quantity):
    while True:
        try:
            Quantity = int(input("Enter How Many Players: "))
            if Quantity>4:
                print("\n**MAXIMUM LIMIT FOR PLAYERS IS ONLY 4**")
                print("**PLEASE TRY AGAIN!**")
            elif Quantity<2:
                print("\n**MINIMUM LIMIT FOR PLAYERS IS ONLY 2**")
                print("**PLEASE TRY AGAIN!**")
            else:
                return Quantity
                break
        except:
            print("**INTEGERS ONLY!**\n**PLEASE TRY AGAIN!**")
            continue
while (Breaker == "GAME ON"):
#InputingOfPlayers
#Player'sDictionary
        rules()
        rounds = 1
        print("")
        Players = { }
        Score = 0
        NumPlayers = QuantiVali(NumPlayers)
        Champions = NumPlayers
        for x in range(1,NumPlayers+1,1):
            Player = {"Player "+str(x): 0}
            Players.update(Player)
        print("\n**LIST OF PLAYERS**")
        Print(Players)
#ActualGame
        while True:
            AValType = 1
            Duration = 0
            BValType = 1
            Coin = TossCoin(Coin,BValType)
            Score+=1
            Temp = Champions
            if Champions == 1:
                Players = WinnerVali(Players)
                print("\n***CONGRATULATIONS!***\n",Players,"YOU ARE THE CHAMPION!")
                AValType = 2
                choice = AlphaVali(choice, AValType, Duration)
                if choice == "N":
                    Breaker = "GAME OVER"
                break
            if rounds>10:
                print("\n**MAXIMUM ROUND HAS BEEN REACHED, THE GAME WILL RESET!**\n")
                break
            while True:
                print("")
                Duration+=1
                if Players["Player "+str(Duration)] == "OUT":
                        continue
                choice = AlphaVali(choice,AValType,Duration)
                if choice!=Coin:
                    Players["Player "+str(Duration)] = "NOMINATED"
                    Champions-=1
                else:
                    Players["Player "+str(Duration)] = Score
                if Champions == 0:
                    print("IT'S A DRAW PLEASE TRY AGAIN!")
                    Duration = 0
                    Champions = Temp
                    Coin = TossCoin(Coin,BValType)
                    continue
                elif Duration == NumPlayers:
                    break
            BValType = 2
            Coin = TossCoin(Coin,BValType)
            print("\n*** Coin: ",Coin,"***")
            for x in Players:
                Players[x] = LosserVali(Players[x],Score)
            print("\n**SCORE**\nRound: ",rounds,":")
            Print(Players)
            rounds+=1
    
        
