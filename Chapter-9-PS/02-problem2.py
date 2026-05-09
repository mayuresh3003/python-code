import random

def game():
    print("You are playing a game ...")
    score = random.randint(1,100)
    
    #Fetch the highscore
    with open("Highscore.txt") as f:
        highscore = f.read()
        if (highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0 
             
    print(f"Your score: {score}")
    if (score>highscore or highscore ==""):
        # write this highscore to the file 
        with open("Highscore.txt", "w") as f:
            f.write(str(score))
            
    return score 

game()