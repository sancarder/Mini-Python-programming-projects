#Text based adventure game

doorA = 'a'
doorB = 'b'
doorC = 'c'
doorD = 'd'
doorE = 'e'
doorF = 'f'
doorG = 'g'
doorH = 'h'


def season_one(door):
    #From door C: right = season 2, forward = CLOSED, left = CLOSED, back = season 4
    #From door D: right = CLOSED, forward = CLOSED, left = season 4, back = season 2

    answer = ''
    answer_list = {'addison', 'addison montgomery', 'addison shepherd'}

    print "You are now in season One!"
    print "Coming from " + door    
    
    while(answer not in answer_list):
        answer = raw_input("Who showed up and surprised Meredith in episode 9?: ")
    
    turn = raw_input("Great job! Where do you want to go next? R/L/F/B: ")

    if door == doorC:
        if turn == 'right':
            #print "You will come to season Two"
            season_two(doorD)
        elif turn == 'b' or turn == 'back':
            #print "You will come to season Four"
            season_four(doorC)
        elif turn == 'forward' or turn == 'left':
            turn = raw_input("You can't go here. Take another turn. R/L/F/B: ")
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")

    if door == doorD:
        if turn == 'left':
            #print "You will come to season Four"
            season_four(doorC)
        elif turn == 'back':
            #print "You will come to season Two"
            season_two(doorD)
        elif turn == 'right' or turn == 'forward':
            turn = raw_input("You can't go here. Take another turn. R/L/F/B: ")            
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")

def season_two(door):
    
    #From door D: right = season 5, forward = season 3, left = CLOSED, back = season 1
    #From door E: right = season 3, forward = CLOSED, left = season 1, back = season 5
    #From door F: right = CLOSED, forward = season 1, left = season 5, back = season 3

    answer = ''
    answer_list = {'burke', 'preston', 'preston burke'}

    print "You are now in season Two!"
    print "Coming from " + door    
    
    while(answer not in answer_list):
        answer = raw_input("Who gets shot in the end of season 2?: ")
    
    turn = raw_input("Great job! Where do you want to go next? R/L/F/B: ")
    
    if door == doorD:
        if turn == 'right':
            #print "You will come to season Five"
            season_five(doorE)
        elif turn == 'forward':
            #print "You will come to season Three"
            season_three(doorF)
        elif turn == 'left':
            turn = raw_input("You can't go here. Take another turn. R/L/F/B: ")            
        elif turn == 'back':
            #print "You will come to season One"
            season_one(doorD)
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")

    if door == doorE:
        if turn == 'right':
            #print "You will come to season Three"
            season_three(doorF)
        elif turn == 'forward':
            turn = raw_input("You can't go here. Take another turn. R/L/F/B: ")            
        elif turn == 'left':
            #print "You will come to season One"
            season_one(doorD)
        elif turn == 'back':
            #print "You will come to season Five"
            season_five(doorE)
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")

    if door == doorF:
        if turn == 'right':
            turn = raw_input("You can't go here. Take another turn. R/L/F/B: ")            
        elif turn == 'forward':
            #print "You will come to season One"
            season_one(doorD)
        elif turn == 'left':
            #print "You will come to season Five"
            season_five(doorE)
        elif turn == 'back':
            #print "You will come to season Three"
            season_three(doorF)
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")



def season_three(door):
    #From door F: right = season 6, forward = CLOSED, left = CLOSED, back = season 2
    #From door G: right = CLOSED, forward = CLOSED, left = season 2, back = season 6

    answer = ''
    answer_list = {'callie', 'callie torres'}

    print "You are now in season Three!"
    print "Coming from " + door    
    
    while(answer not in answer_list):
        answer = raw_input("Who, besides Meredith, was Cristina's bridesmaid in the season three finale?: ")
    
    turn = raw_input("Great job! Where do you want to go next? R/L/F/B: ")

    if door == doorF:
        if turn == 'right':
            #print "You will come to season Six"
            season_six(doorG)
        elif turn == 'b' or turn == 'back':
            #print "You will come to season Two"
            season_two(doorF)
        elif turn == 'forward' or turn == 'left':
            turn = raw_input("You can't go here. Take another turn. R/L/F/B: ")
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")

    if door == doorG:
        if turn == 'left':
            #print "You will come to season Two"
            season_two(doorF)
        elif turn == 'back':
            #print "You will come to season Six"
            season_six(doorG)
        elif turn == 'right' or turn == 'forward':
            turn = raw_input("You can't go here. Take another turn. R/L/F/B: ")            
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")

def season_four(door):
    #From door B: right = season 1, forward = CLOSED, left = CLOSED, back = season 5
    #From door C: right = CLOSED, forward = CLOSED, left = season 5, back = season 1

    answer = ''
    answer_list = {'beth', 'beth monroe'}

    print "You are now in season Four!"
    print "Coming from " + door    
    
    while(answer not in answer_list):
        answer = raw_input("What was the name of the last patient in the clinical trial, who lived?: ")
    
    turn = raw_input("Great job! Where do you want to go next? R/L/F/B: ")

    if door == doorB:
        if turn == 'right':
            #print "You will come to season One"
            season_one(doorC)
        elif turn == 'back':
            #print "You will come to season Five"
            season_five(doorB)
        elif turn == 'forward' or turn == 'left':
            turn = raw_input("You can't go here. Take another turn. R/L/F/B: ")
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")

    if door == doorC:
        if turn == 'left':
           #print "You will come to season Five"
            season_five(doorB)
        elif turn == 'back':
            #print "You will come to season One"
            season_one(doorC)
        elif turn == 'right' or turn == 'forward':
            turn = raw_input("You can't go here. Take another turn. R/L/F/B: ")            
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")

def season_five(door):
    
    #From door A: right = season 6, forward = season 2, left = season 4, back = out
    #From door B: right = out, forward = season 6, left = season 2, back = season 4
    #From door E: right = season 4, forward = out, left = season 6, back = season 2    
    #From door H: right = season 2, forward = season 4, left = out, back = season 6

    answer = ''
    answer_list = {'007'}

    print "You are now in season Five!"
    print "Coming from " + door    
    
    while(answer not in answer_list):
        answer = raw_input("What did the severely injured patient in the end of the season write in Meredith's hand to identify him?: ")
    
    turn = raw_input("Great job! Where do you want to go next? R/L/F/B: ")

    if door == doorA:
        if turn == 'right':
            #print "You will come to season Six"
            season_six(doorH)
        elif turn == 'forward':
            #print "You will come to season Two"
            season_two(doorE)
        elif turn == 'left':
            #print "You will come to season Four"
            season_four(doorB)
        elif turn == 'back':
            print "You will return outside"
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")

    if door == doorB:
        if turn == 'right':
            print "You will return outside"
        elif turn == 'forward':
            #print "You will come to season Six"
            season_six(doorH)
        elif turn == 'left':
            #print "You will come to season Two"
            season_two(doorE)
        elif turn == 'back':
            #print "You will come to season Four"
            season_four(doorB)
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")

    if door == doorE:
        if turn == 'right':
            #print "You will come to season Four"
            season_four(doorB)
        elif turn == 'forward':
            print "You will return outside"
        elif turn == 'left':
            #print "You will come to season Six"
            season_six(doorH)
        elif turn == 'back':
            #print "You will come to season Two"
            season_two(doorE)
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")

    if door == doorH:
        if turn == 'right':
            #print "You will come to season Two"
            season_two(doorE)
        elif turn == 'forward':
            #print "You will come to season Four"
            season_four(doorB)
        elif turn == 'left':
            print "You will return outside"
        elif turn == 'back':
            #print "You will come to season Six"
            season_six(doorH)
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")


def season_six(door):
    #From door H: right = CLOSED, forward = CLOSED, left = season 3, back = season 5
    #From door G: right = season 5, forward = CLOSED, left = CLOSED, back = season 3

    answer = ''
    answer_list = {'charles', 'charles percy', 'percy'}

    print "You are now in season Six!"
    print "Coming from " + door    
    
    while(answer not in answer_list):
        answer = raw_input("What Mercy Wester died in Bailey's arms when he had been shot by Mr. Clarke in the season 6 finale?: ")
    
    turn = raw_input("Great job! Where do you want to go next? R/L/F/B: ")

    if door == doorH:
        if turn == 'left':
            #print "You will come to season Three"
            season_three(doorG)
        elif turn == 'back':
            #print "You will come to season Five"
            season_five(doorH)
        elif turn == 'right' or turn == 'forward':
            turn = raw_input("You can't go here. Take another turn. R/L/F/B: ")            
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")

    if door == doorG:
        if turn == 'right':
            #print "You will come to season Five"
            season_five(doorH)
        elif turn == 'back':
            #print "You will come to season Three"
            season_three(doorG)
        elif turn == 'forward' or turn == 'left':
            turn = raw_input("You can't go here. Take another turn. R/L/F/B: ")
        else:
            turn = raw_input("You have to choose between right, left, back or forward: ")


print "Welcome to Grey's Anatomy! Make your way through the seasons by taking turns and answering questions!\n"
season_five(doorA)
