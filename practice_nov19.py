# Rebecca Pedraza
# Nov 19


import random

def test_rps(p1, p2): 
    p1 = player_choice("h")
    p2 = player_choice("c")
p1 = input("Enter r for rock, p for paper and s for scissors: ")
p2 = input("Enter r for rock, p for paper and s for scissors: ")
def player_choice(ptype):
    if ptype == "c":
        p_choice = random.choice(["r", "p", "s"])
    else:
        return p_choice
    
    if p1 == rock and p2 == scissors: 
            return("Player1")
    if p1 == paper and p2 == rock:
            return("Player1")
    elif p1 == scissors and p2 == paper:
            return("Player1")
        
    if p1 == scissors and p2 == rock:
            return("Player2")
    if p1 == rock and p2 == paper:
            return("Player2")
    elif p1 == paper and p2 == scissors:
            return("Player2")
    
    else:
        p1 == p2
        return("Tie")
        pass

test_rps(p1, p2)


# Example
'''
if p1 == "rock":
    if p2[0] == "s"
        return("player1")
    elif p2[0] == "p"
        return("player2")
    else:
        return("tie")
'''
    
