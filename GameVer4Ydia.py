# AUTHOR :SEBASTIAN YDIA
# PURPOSE: FUN GAME
# DESCRIPTION : KARDASHIAN PLANE WITH GOBLIN PRINCE HAHAHAHAHHHAHAHAAHHHAHAHAHAHHAAH
# FROM: GameVer1Ydia.py FROM SEBASTIAN JOAQUIN TO SEBASTIAAN JOAQUIN


## HOW TO RUN------------------------

# IF THE GAME DOES.NT WORK MAKE SURE PYTHON RUNS IT IN TERMINAL NOT HERE IN PYCHARM OR GO TO (rightclick the file in python)
# MORE RUN /DEBUG AND MODIFY RUN
# CONFIGURATIONS AND GO TO MORE OPTIONS AND TAP EMULATE TERMINAL IN OUTPUT CONSOLE


# VERSION 1.4 (09/17/26)
# ADDED:
# - THE END



# LINE import msvcrt IS THE HELPED AI(google gemini 15 date is 12 2026)(AND THE PARTS RELATED TO IT)

import msvcrt  # ME was helped with Google Gemini in code having this.
import random

# ----------------------------------------------------------------------------------------------------------------------------------#
# Oh em gee TEXT!!!-----------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------------------#
print("--- Windows Text Game ---")
abc = input('''Fun game by sebastian joaquin N. Ydia
Made for fun!!!

    Enter anything(or abc to go skip rules!): 
    ''')
if abc != 'abc':
    print('''by  sebastian joaquin n. ydia 
      MAIN Controls: 
          W (Up), S (Down), A (Left), D (Right)
      OTHER CONTROLS:
          E (Positions), Q (Quit)
      UNINTENTIONAL CONTROLS:
          Second option to quit: pressing any key that aint a letter,space or number              
                                                        ''')
    input("enter anything to see rules!:")

    input(''' 
           THIS IS A FUN PROJECT MDE BY SEBASTIAN(with help o gemini google)

                rules:
                - You are a princess saving a prince at one random location in a 
                Kardashian coordinate plane.
                - you must find him and save him
                - there are 4 goblins you MUST not touch, or you die, you dont know some of their positions hehe
                - the plane stretches out by 10 units in every direction!(20x20)

            enter anything to strt!:''')

# ----------------------------------------------------------------------------------------------------------------------------------#
# Oh em gee VALUES------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------------------#
moves = 0
catch = 0
# -------------------------------------------------#
player_x, player_y = 0, 0

# -------------------------------------------------#
prince_x = random.randint(-10, 10)
prince_y = random.randint(-10, 10)

# -------------------------------------------------#
goblin1_x = random.randint(-10, 10)
goblin1_y = random.randint(-10, 10)
#
while goblin1_x == 0 and goblin1_y == 0:
    goblin1_x = random.randint(-10, 10)
    goblin1_y = random.randint(-10, 10)

# -------------------------------------------------#
goblin2_x = random.randint(-10, 10)
goblin2_y = random.randint(-10, 10)
#
while goblin2_x == 0 and goblin2_y == 0:
    goblin2_x = random.randint(-10, 10)
    goblin2_y = random.randint(-10, 10)

# -------------------------------------------------#
goblin3_x = random.randint(-10, 10)
goblin3_y = random.randint(-10, 10)
#
while goblin3_x == 0 and goblin3_y == 0:
    goblin3_x = random.randint(-10, 10)
    goblin3_y = random.randint(-10, 10)

# -------------------------------------------------#
goblin4_x = random.randint(-10, 10)
goblin4_y = random.randint(-10, 10)
#
while goblin4_x == 0 and goblin4_y == 0:
    goblin4_x = random.randint(-10, 10)
    goblin4_y = random.randint(-10, 10)

# -------------------------------------------------#
while (prince_x == 0 and prince_y == 0) or -5 < prince_x < 5 or -5 < prince_y < 5:
    # WHEN PRINCE IS VERY NEAR ORIGIN(0,0) IT CHANGES POSITION
    prince_x = random.randint(-10, 10)
    prince_y = random.randint(-10, 10)
    # WHEN PRINCE POSITION IS THE SAME AS GOBLIN.
    while (prince_x == goblin1_x and prince_y == goblin1_y) or (prince_x == goblin2_x and goblin2_y == prince_y) or (
            prince_x == goblin3_x and prince_y == goblin3_y) or (prince_x == goblin4_x and prince_y == goblin4_y):
        prince_x = random.randint(-10, 10)
        prince_y = random.randint(-10, 10)

print("you start at 0,0")
print(f"Prince is at ({prince_x}, {prince_y})")
print(f"Goblin 1 is at ({goblin1_x}, ?)")  # change y to ?
print(f"Goblin 2 is at (?, {goblin2_y})")  # change x to ?
print(f"Goblin 3 is at (?, ?)")  # change to both question marks
print(f"Goblin 4 is at (?, ?)")  # change to both question marks
positions = f'''    POSITIONS:                MOVES-{moves}
    Prince - ({prince_x}, {prince_y})
    Goblin1 - ({goblin1_x}, ?)
    Goblin2 - (?, {goblin2_y})
    Goblin3 - (?, ?)
    Goblin4 - (?, ?)
    Princess(you) - ({player_x}, {player_y})'''
# -------------------------------------------------#
input(f"Enter anything to Start!")
# ----------------------------------------------------------------------------------------------------------------------------------#
# Oh em gee Game!!!!!!!!Moving Part-------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------------------#
print("Game Start!!")
while True:

    key = msvcrt.getch().decode('utf-8').lower()
    # lines with key == ... - Code generated with assistance from Google Gemini (Gemini 1.5)
    # Date: September 12, 2026
    # To help me with the keyboard functions
    if key == 'w':
        player_y += 1
        print(f"UP : ({player_x}, {player_y})        MOVES-{moves}")
        moves += 1
    # -------------------------------------------------#

    elif key == 's':
        player_y -= 1
        print(f"DOWN: ({player_x}, {player_y})      MOVES-{moves}")
        moves += 1
    # -------------------------------------------------#

    elif key == 'a':
        player_x -= 1
        print(f"LEFT: ({player_x}, {player_y})      MOVES-{moves}")
        moves += 1
    # -------------------------------------------------#

    elif key == 'd':
        player_x += 1
        print(f"RIGHT: ({player_x}, {player_y})      MOVES-{moves}")
        moves += 1
    # -------------------------------------------------#

    elif key == 'q':
        print(f"Thanks for playing(quitter...)!      MOVES-{moves} CATCHES-{catch}/5")
        break

    elif key == 'e':
        print(f"{positions}")
    # ----------------------------------------------------------------------------------------------------------------------------------#
    # OH em gee GAME!!!! Win-Lose-hhegegegeg--------------------------------------------------------------------------------------------#
    # ----------------------------------------------------------------------------------------------------------------------------------#
    if player_x == prince_x and player_y == prince_y:
        catch += 1
        if catch != 5:
            print(f"You got prince!!   BUT THEN HE GOT TELEPORTED!! CATCH HIM AGAIN!")
            print(f'''Moves: {moves}
Catches: {catch}/5''')
            prince_x = random.randint(-10, 10)
            prince_y = random.randint(-10, 10)
            while (prince_x == goblin1_x and prince_y == goblin1_y) or (
                    prince_x == goblin2_x and goblin2_y == prince_y) or (
                    prince_x == goblin3_x and prince_y == goblin3_y) or (
                    prince_x == goblin4_x and prince_y == goblin4_y) or (prince_x == player_x and prince_y == player_y):
                prince_x = random.randint(-10, 10)
                prince_y = random.randint(-10, 10)
            print(f"The prince is now at ({prince_x}, {prince_y})!!!!")
        else:
            print(f'''OMGGG YOU WON YOU CATCHED HIM 5 TIMES AND YOU SECURELY GOT THE PRINCE!!!
Moves: {moves}
Catches: 5/5   !!!!
''')
            print(f'''    POSITIONS:                MOVES-{moves}
                    Prince - ({prince_x}, {prince_y})
                    Goblin1 - ({goblin1_x}, {goblin1_y})
                    Goblin2 - ({goblin2_x}, {goblin2_y})
                    Goblin3 - ({goblin3_x}, {goblin3_y})
                    Goblin4 - ({goblin4_x}, {goblin4_y})
                    Princess(you) - ({player_x}, {player_y})''')
            break

        positions = f'''    POSITIONS:                MOVES-{moves}
        Prince - ({prince_x}, {prince_y})
        Goblin1 - (?, {goblin1_y})
        Goblin2 - ({goblin2_x}, ?)
        Goblin3 - (?, ?)
        Goblin4 - (?, ?)
        Princess(you) - ({player_x}, {player_y})'''

    # -------------------------------------------------#

    if player_x > 10 or player_x < -10 or player_y > 10 or player_y < -10:
        print(f"You LOSE(bro fell down to the lava(the plane is 20x20)!")
        print(f'''Moves: {moves}
Catches: {catch}/5''')
        print(f'''    POSITIONS:                MOVES-{moves}
                Prince - ({prince_x}, {prince_y})
                Goblin1 - ({goblin1_x}, {goblin1_y})
                Goblin2 - ({goblin2_x}, {goblin2_y})
                Goblin3 - ({goblin3_x}, {goblin3_y})
                Goblin4 - ({goblin4_x}, {goblin4_y})
                Princess(you) - ({player_x}, {player_y})''')
        break
    # -------------------------------------------------#

    if (player_x == goblin1_x and player_y == goblin1_y) or (player_x == goblin2_x and goblin2_y == player_y) or (
            player_x == goblin3_x and player_y == goblin3_y) or (player_x == goblin4_x and player_y == goblin4_y):
        print(f"You LOSE(goblins vs YOU rap battle and you died)!")
        print(f'''Moves: {moves}
Catches: {catch}/5''')
        print(f'''    POSITIONS:                MOVES-{moves}
                Prince - ({prince_x}, {prince_y})
                Goblin1 - ({goblin1_x}, {goblin1_y})
                Goblin2 - ({goblin2_x}, {goblin2_y})
                Goblin3 - ({goblin3_x}, {goblin3_y})
                Goblin4 - ({goblin4_x}, {goblin4_y})
                Princess(you) - ({player_x}, {player_y})''')
        break
    # -------------------------------------------------#
