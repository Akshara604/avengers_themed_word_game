import random
def spider_man():
        phr1 = ["Just missed him.","Oops! That was not mysterio. It was one of the drones.","Come on. Missed again."]
        phr2 = ["Got stuck to one of the drones. Be fast and choose wisely.Also,","You are holding up good.But That was not mysterio you webbed.Also,","You destroyed the drone but aim for mysterio, next time.Also,"]
        phr3 = ["Good  move! You tased Mysterio.","Awesome. Keep it up.","Good, keep your heard straight and make the next move correctly."]
        player_score = 50
        print("You have chosen Spider-Man,Peter Parker")
        print("Peter needs to face Mysterio. Help him defeat him.")
        print("Good luck! Stick tight.")
        print("Choose a mode from the list below and start fighting.")
        modes = ["Stun web","Taser web","Sticky web"]
        print(modes)
        while (player_score>0 and player_score <100):
           choosen_mode = input().lower()
           if(choosen_mode=="stun web"):
                print("Karen use stun web.")
                print(random.choice(phr1) +" You lost 10 points.")
                player_score -= 10
                print(f"Your current score: {player_score}")
           elif(choosen_mode =="sticky web"):
                print("Karen, use sticky web.")
                print(random.choice(phr2) +" no score.")
                print(f"Your current score: {player_score}")
           elif(choosen_mode =="taser web"):
                print("Karen, use taser web.")
                print(random.choice(phr3) +" You got 10 points.")
                player_score += 10
                print(f"Your current score: {player_score}")
        if(player_score == 100):
               print("You win. Yay🎉🎉")
        elif(player_score== 0):
               print("You lose ☹ Better luck next time.")
        
