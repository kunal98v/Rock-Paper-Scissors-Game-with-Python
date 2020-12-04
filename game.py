import random 
import emoji

score = 0
score_cpu = 0


while True:

    print("1: ROCK "+emoji.emojize(":raised_fist:"))
    print("2: PAPER "+emoji.emojize(":raised_hand:"))
    print("3: SCISSORS "+emoji.emojize(":victory_hand:"))

    
    def ans(n):
        if n == '1':
            return "ROCK "+ emoji.emojize(":raised_fist:")
        
        elif n == '2':
            return "PAPER "+ emoji.emojize(":raised_hand:")
        
        elif n == '3':
            return "SCISSORS "+ emoji.emojize(":victory_hand:")

        else :
            print("INVALID INPUT !")
            

    n = input()

    op = [1,2,3]

    k = str(random.choice(op))

    m = n+k
    print("Your input:"+ ans(n))
    if (m == '11') or (m =='22') or (m == '33'):

        print(ans(n) +"  WITH  " + ans(k))
        print("......................DRAW.......................")
    
    elif (m == '13') or (m == '21') or (m == '32'):

        print(ans(n) +"   BEATS   " + ans(k))
        print("......................YOU WIN !...................")
        score+=1
    
    else:
        print(ans(n) +"   BEATEN BY   " + ans(k))
        print("......................YOU LOST !...................")
        score_cpu+=1

    print(f'Your Score : {score}')
    print(f'CPU Score  : {score_cpu}')
    print(".......................................................")

    if score == 5 :
        print("CONGRATS ! YOU WON THE GAME.")
        break
    
    elif score_cpu == 5:
        print("YOU LOST ! BETTER LUCK NEXT TIME.")
        break
    



    
