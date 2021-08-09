import random
def spider_man():
        phr1 = ["Just missed him.","Oops! That was not mysterio. It was one of the drones.","Come on. Missed again."]
        phr2 = ["Got stuck to one of the drones. Be fast and choose wisely.Also,","You are holding up good.But That was not mysterio you webbed.","You destroyed the drone but aim for mysterio, next time."]
        phr3 = ["Good  move! You tased Mysterio.","Awesome. Keep it up.","Good, keep your heard straight and make the next move correctly."]
        player_score = 50
        win_score = player_score+10
        lose_score = player_score-10
        tie_score =player_score
        scores =[win_score,lose_score,tie_score]
        print("You have chosen Spider-Man,Peter Parker")
        print("Peter needs to face Mysterio. Help him defeat him.")
        print("Good luck! Stick tight.")
        print("Choose a mode from the list below and start fighting.")
        modes = [" 's' for Stun web"," 't' for Taser web"," 'st' for Sticky web"]
        print(modes)
        while (player_score>0 and player_score <100):
           choosen_mode = input().lower()
           if(choosen_mode=='s'):
                print("Karen use stun web.")
                print(random.choice(phr1))
               #  player_score -= 10
                print(f"Your current score: {random.choice(scores)}")
           elif(choosen_mode =="st"):
                print("Karen, use sticky web.")
                print(random.choice(phr2))
                print(f"Your current score: {random.choice(scores)}")
           elif(choosen_mode =='t'):
                print("Karen, use taser web.")
                print(random.choice(phr3))
               #  player_score += 10
                print(f"Your current score: {random.choice(scores)}")
        if(player_score == 100):
               print("You win. Yay🎉🎉")
        elif(player_score== 0):
               print("You lose ☹ Better luck next time.")
        