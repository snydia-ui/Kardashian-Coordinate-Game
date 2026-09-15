#AUTHOR :SEBASTIAN YDIA
#PURPOSE: FUN GAME
#DESCRIPTION : KARDASHIAN PLANE WITH GOBLIN PRINCE HAHAHAHAHHHAHAHAAHHHAHAHAHAHHAAH


## HOW TO RUN
# IF THE GAME DOESNT WORK MAKE SURE PYTHON RUNS IT IN TERMINAL NOT HERE IN PYCHARM OR GO TO MORE RUN /DEBUG AND MODIFY RUN
# CONFIGURATIONS AND GO TO MORE OPTIONS AND TAP EMULATE TERMINAL IN OUTPUT CONSOLE


# FIRST VERSION
# ADDED:
# This is the firs version , added the game































#LINE 13 IS THE ONLY AI(AND THE PARTS RELATED TO IT)
import msvcrt # ME was helped with Google Gemini in code having this.
import random
#----------------------------------------------------------------------------------------------------------------------------------#
#Oh em gee TEXT!!!-----------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------#
print("--- Windows Text Game ---")
print('''by  sebastian joaquin n. ydia 
  MAIN Controls: 
      W (Up), S (Down), A (Left), D (Right), Q (Quit)
  UNINTENTIONAL CONTROLS:
      Second option to quit: pressing any key that aint a letter,space or number              
                                                    ''')
abc = input("enter anything to see rules!(enter abc to skip):")
if abc != "abc":
    input(''' 
       THIS IS A FUN PROJECT MDE BY SEBASTIAN(with help o gemini google)
       
            rules:
            - You are a princess saving a prince at one random location in a 
            Kardashian coordinate plane.
            - you must find him and save him
            - there are 4 goblins you MUST not touch, or you die, you dont know some of their positions hehe
            - the plane stretches out by 10 units in every direction!(20x20)
            
            enter anything to strt!:''')

#----------------------------------------------------------------------------------------------------------------------------------#
#Oh em gee VALUES------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------#
moves = 0
catch = 0
#-------------------------------------------------#
player_x, player_y = 0, 0
#
print("you start at 0,0")
#-------------------------------------------------#
prince_x = random.randint(-10,10)
prince_y = random.randint(-10,10)

#-------------------------------------------------#
goblin1_x = random.randint(-10,10)
goblin1_y = random.randint(-10,10)
#
while goblin1_x == 0 and goblin1_y == 0:
    goblin1_x = random.randint(-10,10)
    goblin1_y = random.randint(-10,10)

#-------------------------------------------------#
goblin2_x = random.randint(-10,10)
goblin2_y = random.randint(-10,10)
#
while goblin2_x == 0 and goblin2_y == 0:
    goblin2_x = random.randint(-10,10)
    goblin2_y = random.randint(-10,10)

#-------------------------------------------------#
goblin3_x = random.randint(-10,10)
goblin3_y = random.randint(-10,10)
#
while goblin3_x == 0 and goblin3_y == 0:
    goblin3_x = random.randint(-10,10)
    goblin3_y = random.randint(-10,10)

#-------------------------------------------------#
goblin4_x = random.randint(-10,10)
goblin4_y = random.randint(-10,10)
#
while  goblin4_x == 0 and  goblin4_y == 0:
     goblin4_x = random.randint(-10,10)
     goblin4_y = random.randint(-10,10)

#-------------------------------------------------#
while (prince_x == 0 and prince_y == 0) or -5 < prince_x < 5 or -5 < prince_y < 5:
    # WHEN PRINCE IS VERY NEAR ORIGIN(0,0) IT CHANGES POSITION
    prince_x = random.randint(-10, 10)
    prince_y = random.randint(-10, 10)
    # WHEN PRINCE POSITION IS THE SAME AS GOBLIN.
    while (prince_x == goblin1_x and prince_y == goblin1_y) or (prince_x == goblin2_x and goblin2_y == prince_y) or (prince_x == goblin3_x and prince_y == goblin3_y) or (prince_x == goblin4_x and prince_y == goblin4_y):
        prince_x = random.randint(-10, 10)
        prince_y = random.randint(-10, 10)

print(f"Prince is at ({prince_x}, {prince_y})")
print(f"Goblin 1 is at ({goblin1_x}, {goblin1_y})") #change y to ?
print(f"Goblin 2 is at ({goblin2_x}, {goblin2_y})") #change x to ?
print(f"Goblin 3 is at ({goblin3_x}, {goblin3_y})") #change to both question marks
print(f"Goblin 4 is at ({goblin4_x}, {goblin4_y})") #change to both question marks
#-------------------------------------------------#
input(f"Enter anything to Start!")
#----------------------------------------------------------------------------------------------------------------------------------#
#Oh em gee Game!!!!!!!!Moving Part-------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------#
print("Game Start!!")
while True:

    key = msvcrt.getch().decode('utf-8').lower()

    if key == 'w':
        player_y += 1
        print(f"UP : ({player_x}, {player_y})")
        moves += 1
    # -------------------------------------------------#

    elif key == 's':
        player_y -= 1
        print(f"DOWN: ({player_x}, {player_y})")
        moves += 1
    # -------------------------------------------------#

    elif key == 'a':
        player_x -= 1
        print(f"LEFT: ({player_x}, {player_y})")
        moves += 1
    # -------------------------------------------------#

    elif key == 'd':
        player_x += 1
        print(f"RIGHT: ({player_x}, {player_y})")
        moves += 1
    # -------------------------------------------------#

    elif key == 'q':
        print("Thanks for playing(quitter...)!")
        break
    # ----------------------------------------------------------------------------------------------------------------------------------#
    # OH em gee GAME!!!! Win-Lose-hhegegegeg--------------------------------------------------------------------------------------------#
    # ----------------------------------------------------------------------------------------------------------------------------------#
    if player_x == prince_x and player_y == prince_y:
        print(f"You win!(  but u actually dont, the prince does NOT love you :[   )")
        print(f'''Moves: {moves}''')
        break
    # -------------------------------------------------#

    if player_x > 10 or player_x < -10 or player_y > 10 or player_y < -10:
        print(f"You LOSE(bro fell down to the lava(the plane is 20x20)!")
        print(f'''Moves: {moves}''')
        break
    # -------------------------------------------------#

    if (player_x == goblin1_x and player_y == goblin1_y) or (player_x == goblin2_x and goblin2_y == player_y) or (player_x == goblin3_x and player_y == goblin3_y) or (player_x == goblin4_x and player_y == goblin4_y):
        print(f"You LOSE(goblins vs YOU rap battle and you died)!")
        print(f'''Moves: {moves}''')
        break
    # -------------------------------------------------#
