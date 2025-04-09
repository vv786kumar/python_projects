import random

def rock_paper_scissor():
    player = input("""
                What is your choice?
                'r' --> Rock
                'p' --> Paper
                's' --> Scissor
            """)
    computer = random.choice(['r', 'p', 's'])

    print(player, computer)
    print("Result is ==> ", isWin(player, computer))

def isWin(player, computer):
    # r>s , s>p , p>r
    if (player==computer):
        return "Tie!!!"
    elif (player=='r' and computer=='s') or \
        (player=='s' and computer=='p') or \
        (player=='p' and computer=='r'):
        return "You Won!!!"
    else:
        return "You Lost!!!"

if __name__=="__main__":
    rock_paper_scissor()