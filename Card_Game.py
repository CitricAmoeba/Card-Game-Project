"""
Written by Samuel Plane

Last edited on 07/01/2022

Notes:

- Randomly pick which player goes first, and give the other player an advantage to balance it out

- Future idea, let player choose the style of base they want e.g. high defences, low population etc.

- Hide enemy_base's sabotage unit

- Add docstrings

- Change hardcodings in Player_Base.player_act() and Player_Base.turn()


LOGBOOK

31/03/2020

Added documentation
Refactored player_act()

02/04/2020

Added update_ready()
Refactored player_turn()

07/06/2020

Continued work on attack(), allowing sabotage units to do increased damage

08/10/2020

Changed the Base attribute _field to be public
player_act stops repeating when the user presses f

25/12/2020

Prepared code to be uploaded to github
Corrected some documentation
Implemented most of the prepare() subroutine

26/12/2020

Finished prepare()
Added some docstrings and comments

08/03/2021
Created a method for Base, copy() creating a copy of the current Base
instance so it can be used by the AI to search through all possible actions

15/04/2021
Removed an outdated constructor for Base
Changed some variable names to better describe their function
Added isPlayer field to Base to determine if the Base is controlled by the player or the AI
Changed prepare into a method of Base & made it more modular so it can be used by both player and AI
Created Base methods to determine the unit to prepare by both human players and AI

16/04/2021
Changed attack into a method of Base
Created Base methods to determine the attacking unit by both human players and AI


07/01/2022
Reformatted project so that classes are now in their own file
Introducd Player_Base and AI_Base classes that inherits from Base
Removed isPlayer field from Base as the introduction of child classes of Base makes this obsolete
Combined Base.get_number_of_draws and Base.draw() into one subroutine
Changed turn and act subroutines into methods of their respective classes
"""

# User input adheres to zero-indexing
import random
import Base as base
import Card as card

##Instantiates variables and objects

#Instances of Card
card_values = [['Behemoth',700,600],['Mutated Scorpion',800,400],['Scrap Tank',400,800],['Veteran Scavenger',300,300],['Mercenaries',400,300],['Saboteurs',500,200],['Heavy Weaponeers',600,400],['Lookout',300,100],['Wanderer',700,700],['Renegade Master',600,500]]
all_cards = []
for each_value in card_values:
    all_cards.append(card.Card(each_value[0], each_value[1], each_value[2]))

#Instances of Base
#!! Remove bool argument from the end as the constructor has been modified
enemy_base = base.Base(8000,3500,3500,all_cards,[], [None, None, None, None, None], False) #When players can choose their own decks, change this as its just a list of all the cards I've created 
player_base = base.Base(8000,3500,3500,all_cards,[],[None, None, None, None, None], True)

#Global variables
game_finished = False

"""
Subroutines

display_board
player_act
"""


def display_board():
    """
    Displays the actual base in the shell
    """
    #Starts each line
    line_1 = '  |'
    line_2 = '  |'
    line_3 = '  |'
    line_4 = '  |'
    line_5 = '  |'
    line_6 = '  |'
    for each_space_in_field in enemy_base.field:
        #If the current space is empty, add a standard number of spaces to each line, followed by a '|'
        if each_space_in_field == None:
            line_1 += ' '*20
            line_1 += '|'
            line_2 += ' '*20
            line_2 += '|'
            line_3 += ' '*20
            line_3 += '|'
        #Else
        else:
            spaces = 20-len(each_space_in_field.name)
            pre_spaces = spaces // 2
            line_1 += ' '*pre_spaces
            line_1 += each_space_in_field.name
            line_1 += ' '*spaces-pre_spaces
            line_1 += '|'

            spaces = 20-len(str(each_space_in_field.attack))
            pre_spaces = spaces // 2
            line_2 += ' '*pre_spaces
            line_2 += str(each_space_in_field.attack)
            line_2 += ' '*spaces-pre_spaces
            line_2 += '|'

            spaces = 20 - len(str(each_space_in_field.defence))
            pre_spaces = spaces // 2
            line_3 += ' '*pre_spaces
            line_3 += str(each_space_in_field.defence)
            line_3 += ' '*spaces-pre_spaces
            
    for each_space_in_field in player_base.field:
        if each_space_in_field == None:
            line_4 += ' '*20
            line_4 += '|'
            line_5 += ' '*20
            line_5 += '|'
            line_6 += ' '*20
            line_6 += '|'
        else:
            spaces = 20-len(each_space_in_field.name)
            pre_spaces = spaces // 2
            line_4 += ' '*pre_spaces
            line_4 += each_space_in_field.name
            line_4 += ' '*spaces-pre_spaces
            line_4 += '|'

            spaces = 20-len(str(each_space_in_field.attack))
            pre_spaces = spaces // 2
            line_5 += ' '*pre_spaces
            line_5 += str(each_space_in_field.attack)
            line_5 += ' '*spaces-pre_spaces
            line_5 += '|'

            spaces = 20-len(str(each_space_in_field.defence))
            pre_spaces = spaces // 2
            line_6 += ' '*pre_spaces
            line_6 += str(each_space_in_field.defence)
            line_6 += ' '*spaces-pre_spaces
            line_6 += '|'

    shelter_display = open('shelter1.txt','r')

    for lines in shelter_display:
        print(lines,end="")

    shelter_display.close()

    print()
    print()
    print('  Population:',str(enemy_base.pop) + '                         Supply Lines:',str(enemy_base.supply_lines) + '                        Defences:' + str(enemy_base.defences))
    print()
    print('  |0                   |1                   |2                   |3                   |4                   |')
    print(line_1)
    print(line_2)
    print(line_3)
    print()
    print()
    print()
    print('  |0                   |1                   |2                   |3                   |4                   |')
    print(line_4)
    print(line_5)
    print(line_6)
    print()
    print('  Population:',str(player_base.pop) + '                         Supply Lines:',str(player_base.supply_lines) + '                        Defences:' + str(player_base.defences))
    print()




#Start of the Game
player_next = random.randint(0,1)

#Testing, remove later
display_board()

while game_finished == False:
    if player_next == 1:
        player_turn()
        player_next = 0
    else:
        ai_turn()
        player_next = 1
