import random
def loki():
        phr1 = ["The Tva is scared.Good move.","Awesome. You have weakened the TVA. Choose the next move wisely.","Good move.Keep it up."]
        phr2 = ["Whew, That was pretty close.But,","You are holding up good.Be bold and make the next move.Also,","You dodged at the right time.But,"]
        phr3 = ["The TVA is gaining on you. Be careful.","Running is fine.But, you are not getting any far. Make a better move.","The Tva is on your tail. Watch your back."]
        player_score = 50
        print("You have chosen Loki Laufeyson, The god of mischeif and you are burdened with glorious purpose.")
        print("Now,Loki has to face the TVA. Help him escape from TVA")
        print("Good luck and don't die😉")
        print("Choose a weapon from the list below:")
        weapons = ["Staff","Dagger"]
        print(weapons)
        choosen_weapon = input().lower()
        if(choosen_weapon=="staff"):
            print("You have choosen staff. You have three moves: stab, dodge,run. enter your move below:")
            while(player_score>0 and player_score<100):
                moves= input().lower()
                if(moves =="stab"):
                  print(random.choice(phr1) +" 10 points to you.")
                  player_score += 10
                  print(f"Your current score: {player_score}")
                elif(moves =="dodge"):
                  print(random.choice(phr2) +" no score.")
                  print(f"Your current score: {player_score}")
                elif(moves =="run"):
                  print(random.choice(phr3) +" You lost 10 points.")
                  player_score -= 10
                  print(f"Your current score: {player_score}")
            if(player_score == 100):
               print("You win. Yay🎉🎉")
            elif(player_score== 0):
               print("You lose ☹ Better luck next time.")
        elif(choosen_weapon=="dagger"):
            print("You have choosen dagger. You have three moves: stab, dodge ,run. enter your move below:")
            while(player_score>0 and player_score<100):
                moves= input().lower()
                if(moves =="stab"):
                  print(random.choice(phr1) +" 10 points to you")
                  player_score += 10
                  print(f"Your current score: {player_score}")
                elif(moves =="dodge"):
                  print(random.choice(phr2) +" no score.")
                  print(f"Your current score: {player_score}")
                elif(moves =="run"):
                  print(random.choice(phr3) +" You lost 10 points.")
                  player_score -= 10
                  print(f"Your current score: {player_score}")
            if(player_score == 100):
               print("You win. Yay🎉🎉")
            elif(player_score== 0):
               print("You lose ☹.Better luck next time.")
