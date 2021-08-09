from loki import *
from spiderman import *
print("Hey there! Yeah you!")
print("Let\'s play a game")
print("You will have 50 points.Each time you lose, 10 points will be reduced.Each time you win, 10 will be added.")
print("If you reach 100 points you win. If your points get reduced to 0 you lose.")
print("So, make good choices!")
print("Choose a character from the list below:")
character = [" 'l' for Loki"," 's' for Spider-Man"]
print(character)
user_char = input().lower()

if(user_char=='l'):
    loki()
elif(user_char=='s'):
    spider_man()


