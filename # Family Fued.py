# Family Fued
round1_answers=[("Ghosts", 25), ("Cobwebs", 25), ("Spiders", 19), ("Mice", 14), ("Dust", 6)]
round2_answers=[("Santa Claus", 30), ("Elves", 20), ("Snow", 15), ("Reindeer", 12), ("Sleigh", 6)]
def setup(ans):
    dict={}
    
    for i in range(len(ans)):
        
        dict[i+1]="______"
    return dict
        


def print_setup(dict,ans):
    for i in range(len(ans)):
        print(str(i+1)+" "+dict[i+1][0]+" "+str(dict[i+1][1]))


def points(dict):
    points=0
    for i in dict:
        if type(dict[i])==list:
            points+=dict[i][1]
    return points
def check_guess(guess,dict,ans):
    c=0
    
    for i in range(len(ans)):
        if guess.lower()==ans[i][0].lower():
            dict[i+1]=[guess,ans[i][1]]
            c+=1
            
            return True

    if c==0:
        return False
    
def first_guess(dict,ans):
    guess=input("enter guess of player1")
    if check_guess(guess,dict,ans)==True:
        controller='player1'

    else:
        controller='player2'
    print_setup(dict,ans)
    return controller
def play_game(dict,ans):
    print_setup(dict,ans)
    
    controller=first_guess(dict,ans)
    
    points1=0
    c=0
    s=0

    STRIKES=3
    #for i in range(4):
    while True:
        
        guess=input("enter guess of "+controller)
        if check_guess(guess,dict,ans)==True:

            print_setup(dict,ans)
            s+=1
            if s ==len(ans)-1:
                break

            print("strikes left=",STRIKES)

            
                
        else:
            STRIKES-=1
            print("strikes left=",STRIKES)

            c+=1
            
        if STRIKES==0:
            break
        
    if c>1:
        if controller=='player1':
            controller='player2'
        else:
            controller='player1'
        steal=input("enter guess for steal "+controller)
        if check_guess(steal,dict,ans)==True:
            print_setup(dict,ans)
            
            
            winner=controller
            print(controller+" wins round"+' with '+str(points(dict))+" points")
            return controller+" "+ str(points(dict))
        else:
            if controller=='player1':
                controller='player2'
            else:
                controller='player1'
                winner=controller
                print(controller+" wins round"+' with '+str(points(dict))+" points")
                return controller+" "+str(points(dict))
    else:
        print("winner of round is "+controller+" with "+str(points(dict))+" points")
        return controller+" "+str(points(dict))
print("What would you find in a haunted house?")   
a=play_game(setup(round1_answers),round1_answers)

print( 'What would you find at the North Pole?')
b=play_game(setup(round2_answers),round2_answers)
if a.split(' ')[0]==b.split(' ')[0]:
    print(a.split(' ')[0] +"points= ",int(a.split(' ')[1])+int(b.split(' ')[1]))
    if a.split(' ')[0]=='player1':
        print("player2 points= ",0)
    else:
        print("player1 points= ",0)


else:
    print(a.split(' ')[0]+"points= ",int(a.split(' ')[1]))
    print(b.split(' ')[0]+"points= ",int(b.split(' ')[1]))



        


                    
                
                

