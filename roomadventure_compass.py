#Text based adventure game

def print_house(season):
    
#    season -=1
    
    print season
    
    i = 0
    position1 = ''
    position2 = ''
    
    isInBox1 = '*\t********\t*\t\t\t*\t\t\t*'
    isInBox2 = '*\t\t\t*\t********\t*\t\t\t*'
    isInBox3 = '*\t\t\t*\t\t\t*\t********\t*'    
    
    positions = [isInBox1, isInBox2, isInBox3, isInBox1, isInBox2, isInBox3]
    
    edge = '*************************************************************************'
    name1 = '*\tSeason 1\t*\tSeason 2\t*\tSeason 3\t*'
    name2 = '*\tSeason 4\t*\tSeason 5\t*\tSeason 6\t*'
    building = '*\t\t\t*\t\t\t*\t\t\t*'


    print edge
    
    for i in range(2):
        print building
##        i++
##    i = 0
    print name1
    if season < 4:
        print positions[season-1]
    else:
        print building
    for i in range(2):
        print building
##        i++
##     i = 0
   
    print edge
    
    for i in range(2):
        print building
 ##       i++
 ##   i = 0
    print name2
    if season > 3:
        print positions[season-1]
    else:
        print building    
    for i in range(2):
        print building
 ##       i++
 ##   i = 0
        
    print edge


def season_one():
    
    out = False

    answer = ''
    answer_list = {'addison', 'addison montgomery', 'addison shepherd'}

    print_house(1)
    print "You are now in season One!"
    
    while(answer not in answer_list):
        answer = raw_input("Who showed up and surprised Meredith in episode 9?: ")
    
    turn = raw_input("Great job! Where do you want to go next? S/N/E/W: ")

    while out != True:
        if turn == 'east':
            #print "You will come to season Two"
            season_two()
            out = True
        elif turn == 'south':
            #print "You will come to season Four"
            season_four()
            out = True
        elif turn == 'north' or turn == 'west':
            turn = raw_input("You can't go here. Take another turn: ")
        else:
            turn = raw_input("You have to choose between south, north, east or west: ")

def season_two():
    
    out = False
    
    answer = ''
    answer_list = {'burke', 'preston', 'preston burke'}

    print_house(2)
    print "You are now in season Two!"
    
    while(answer not in answer_list):
        answer = raw_input("Who gets shot in the end of season 2?: ")
    
    turn = raw_input("Great job! Where do you want to go next? S/N/E/W: ")
    
    while out != True:
        if turn == 'south':
            season_five()
            out = True
        elif turn == 'east':
            #print "You will come to season Three"
            season_three()
            out = True            
        elif turn == 'north':
            turn = raw_input("You can't go here. Take another turn: ")            
        elif turn == 'west':
            season_one()
            out = True
        else:
            turn = raw_input("You have to choose between south, north, east or west: ")


def season_three():

    out = False
    
    answer = ''
    answer_list = {'callie', 'callie torres'}

    print_house(3)
    print "You are now in season Three!"
    
    while(answer not in answer_list):
        answer = raw_input("Who, besides Meredith, was Cristina's bridesmaid in the season three finale?: ")
    
    turn = raw_input("Great job! Where do you want to go next? S/N/E/W: ")

    while out != True:
        if turn == 'south':
            season_six()
            out = True                        
        elif turn == 'west':
            season_two()
            out = True            
        elif turn == 'east' or turn == 'north':
            turn = raw_input("You can't go here. Take another turn: ")
        else:
            turn = raw_input("You have to choose between south, north, east or west: ")


def season_four():

    out = False
    
    answer = ''
    answer_list = {'beth', 'beth monroe'}

    print_house(4)
    print "You are now in season Four!"
    
    while(answer not in answer_list):
        answer = raw_input("What was the name of the last patient in the clinical trial, who lived?: ")
    
    turn = raw_input("Great job! Where do you want to go next? S/N/E/W: ")

    while out != True:
        if turn == 'north':
            season_one()
            out = True                        
        elif turn == 'east':
            season_five()
            out = True            
        elif turn == 'west' or turn == 'south':
            turn = raw_input("You can't go here. Take another turn: ")
        else:
            turn = raw_input("You have to choose between south, north, east or west: ")


def season_five():
    
    out = False
    answer = ''
    answer_list = {'007'}

    print_house(5)
    print "You are now in season Five!"
    
    while(answer not in answer_list):
        answer = raw_input("What did the severely injured patient in the end of the season write in Meredith's hand to identify him?: ")
    
    turn = raw_input("Great job! Where do you want to go next? S/N/E/W: ")

    while out != True:
        if turn == 'east':
            season_six()
            out = True            
        elif turn == 'north':
            season_two()
            out = True            
        elif turn == 'west':
            season_four()
            out = True            
        elif turn == 'south':
            print "You will return outside. Goodbye."
        else:
            turn = raw_input("You have to choose between south, north, east or west: ")


def season_six():

    out = False
    
    answer = ''
    answer_list = {'charles', 'charles percy', 'percy'}

    print_house(6)
    print "You are now in season Six!"
    
    while(answer not in answer_list):
        answer = raw_input("What Mercy Wester died in Bailey's arms when he had been shot by Mr. Clarke in the season 6 finale?: ")
    
    turn = raw_input("Great job! Where do you want to go next? S/N/E/W: ")

    while out != True:
        if turn == 'north':
            season_three()
            out = True            
        elif turn == 'west':
            season_five()
            out = True            
        elif turn == 'east' or turn == 'south':
            turn = raw_input("You can't go here. Take another turn: ")            
        else:
            turn = raw_input("You have to choose between south, north, east or west: ")


print "Welcome to Grey's Anatomy! Make your way through the seasons by taking turns and answering questions!\n"
print_house(5)
season_five()
