import random

def game (comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True 
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer's turn : Snake(s) Water(w) or Gun(g) ?")
rand_no = random.randint(1,3)

if rand_no == 1:
    comp = 's'
elif rand_no == 2:
    comp = 'w'
else:
    comp = 'g'
 
you = input("Your turn : Snake(s) Water(w) or Gun(g) ? : ")
a = game(comp , you)
if a == None:
    print(f"The game is tie !! , Your choice : {you} , Computer choice : {comp}")
elif a :
     print(f"You win the game !! , Your choice : {you} , Computer choice : {comp}")
else :
     print(f"You loose the game !! , Your choice : {you} , Computer choice : {comp}")