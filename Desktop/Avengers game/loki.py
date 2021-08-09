import random
def loki():
        phr1 = ["The Tva is scared.Good move.","Awesome. You have weakened the TVA. Choose the next move wisely.","Good move.Keep it up."]
        phr2 = ["Whew, That was pretty close.","You are holding up good.Be bold and make the next move.","You dodged at the right time."]
        phr3 = ["The TVA is gaining on you. Be careful.","Running is fine.But, you are not getting any far.","The Tva is on your tail. Watch your back."]
        player_score = 50
        win_score = player_score+10
        lose_score = player_score-10
        tie_score =player_score
        scores =[win_score,lose_score,tie_score]
        print("You have chosen Loki Laufeyson, The god of mischeif and you are burdened with glorious purpose.")
        print("Now,Loki has to face the TVA. Help him escape from TVA")
        print("Good luck and don't die😉")
        print("Choose a weapon from the list below:")
        weapons = [" 's' for Staff"," 'd' for Dagger"]
        print(weapons)
        choosen_weapon = input().lower()
        if(choosen_weapon=='s'):
            print("You have choosen staff. You have three moves: stab, dodge,run. enter your move below:")
            while(player_score>0 and player_score<100):
                moves= input().lower()
                if(moves =="stab"):
                  print(random.choice(phr1) )
                  player_score += 10
                  print(f"Your current score: {random.choice(scores)}")
                elif(moves =="dodge"):
                  print(random.choice(phr2) )
                  print(f"Your current score: {random.choice(scores)}")
                elif(moves =="run"):
                  print(random.choice(phr3))
                  player_score -= 10
                  print(f"Your current score: {random.choice(scores)}")
            if(player_score == 100):
               print("You win. Yay🎉🎉")
            elif(player_score== 0):
               print("You lose ☹ Better luck next time.")
        elif(choosen_weapon=='d'):
            print("You have choosen dagger. You have three moves: stab, dodge ,run. enter your move below:")
            while(player_score>0 and player_score<100):
                moves= input().lower()
                if(moves =="stab"):
                  print(random.choice(phr1))
                  # player_score += 10
                  print(f"Your current score: {random.choice(scores)}")
                elif(moves =="dodge"):
                  print(random.choice(phr2))
                  print(f"Your current score: {random.choice(scores)}")
                elif(moves =="run"):
                  print(random.choice(phr3))
                  # player_score -= 10
                  print(f"Your current score: {random.choice(scores)}")
            if(player_score == 100):
               print("You win. Yay🎉🎉")
            elif(player_score== 0):
               print("You lose ☹.Better luck next time.")