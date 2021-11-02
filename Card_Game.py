"""
Written by Samuel Plane

Last edited on 16/04/2021

Notes:

- Randomly pick which player goes first, and give the other player an advantage to balance it ot

- Future idea, let player choose the style of base they want e.g. high defences, low population etc.

- Finish player_act for 'p' action

- Hide enemy_base's sabotage unit

- Add docstrings

- Create an accessor for the Base's isPlayer field 


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

"""

# User input adheres to zero-indexing
import random

class Base(object):
    """
    Fields:

    pop (short for population)
    defences
    supply_lines
    _deck
    _hand
    field
    isPlayer

    Methods:

    __init__
    display_hand
    draw
    get_number_of_draws
    get_number_of_actions
    copy
    attack
    prepare

    """


    #'d' is repeated for some parameters to differentiate them
    #from keywords and the fields
    def __init__(self,population,sup_lines,deff,deck,hand,fieldd,isAPlayer):
        self.pop = population
        self.supply_lines = sup_lines
        self.defences = deff
        self._deck = deck
        self._hand = hand
        self.field = fieldd
        self.isPlayer = isAPlayer


    def display_hand(self):
        for each_card in self._hand:
            print(each_card.name + ', ' + str(each_card.attack) + ', ' + str(each_card.defence))


    def draw(self):
        #Ensures the number of cards in a player's hand never exceeds 10
        if len(self._hand)<10:
            #Adds a random card to the player's hand
            self._hand.append(random.choice(self._deck))


    def get_number_of_draws(self):
        #Calculates how many cards are drawn in this turn
        if self.supply_lines > 2000:
            return 3
        elif self.supply_lines > 1000:
            return 2
        else:
            return 1


    def get_number_of_actions(self):
        #Calculates how many actions can be taken this turn
        if self.defences > 2000:
            return 3
        elif self.defences > 1000:
            return 2
        else:
            return 1


    def getUnitToPrepare(self):
        return 1

    def calculateUnitToPrepare(self):
        return 1

    def getUnitToAttack(self):
        return 1

    def calculateUnitToAttack(self):
        return 1

    def getTarget(self):
        return 1

    def calculateTarget(self):
        return 1


    def prepare(self):
        """
            Places a card from the base's hand into it's field

            First it checks if there are any cards in the base's hand that can be placed, and then
            if there is any room on the field to place the card. If these two conditions are met,
            the base's controller (human or AI) will select a card to place and what position
            to place it im

        """
        #Checks for a unit to prepare in the players hand
        if len(self._hand) > 0:
            space = 0
            #Checks if there is a space available on the field for the unit
            while space < 5:
                if self.field[space] == None:
                    #As we have found an empty space we set space to prevent the loop from checking further spaces
                    space = 5
                    #User selects a valid unit to prepare from their hand
                    if self.isPlayer == True:
                        unit_to_prepare = self.getUnitToPrepare()
                    else:
                        unit_to_prepare = self.calculateUnitToPrepare()

                    #Can reuse this code to get players input for the unit to prepare
                    """
                    unit_to_prepare = -1
                    while (unit_to_prepare < 0) or (unit_to_prepare >= len(self._hand)):
                            unit_to_prepare = int(input('Which unit would you like to prepare?'))
                            if (unit_to_prepare < 0) or (unit_to_prepare < 9):
                                print('That number is invalid')
                    """

                    #User selects a valid position to place the selected unit in
                    prep_position = -1
                    while (prep_position < 0) or (prep_position > 4) or (self.field[prep_position] != None):
                        prep_position = int(input('Which position would you like to prepare in?'))
                        if (prep_position < 0) or (prep_position > 4):
                            print('That number is invalid')
                        elif (self.field[prep_position] != None):
                            print('That space is occupied')

                    #Places the selected unit into the selected position, and removes it from the player's hand
                    self.field[prep_position] = self._hand.pop(unit_to_prepare)

                space += 1


    def attack(self, target_base):
        #checks if there are any units to attack with
            can_attack = False
            position = 0
            while position < 5 and can_attack == False:
                if isinstance(self.field[position],Card):
                    if self.field[position].ready == 2:
                        can_attack = True
                    else:
                        position += 1
                else:
                    position += 1

            if can_attack == False:
                return
            else:
                can_attack = False

            if can_attack == True:

                #user selects valid attacker
                if self.isPlayer == True:
                    attacker = self.getUnitToAttack()
                else:
                    attacker = self.calculateUnitToAttack()
                """
                attacker = 100
                while attacker > 4 or attacker < 0:
                    attacker = int(input('Which unit should attack?'))
                    if (attacker >= 0) and (attacker < 5):
                        if not isinstance (self.field[attacker],Card):
                            print('There is no card in that spot')
                            attacker = 100
                """

                #If attacker is a sabotage unit, double attack
                #!! Should it be triple?
                if attacker != 5:
                    attacking_damage = self.field[attacker].attack
                else:
                    attacking_damage = self.field[attacker].attack * 2

                #user selects valid target
                if self.isPlayer == True:
                    target = self.getTarget()
                else:
                    target = self.calculateTarget()
                """
                print('Select 5 for population, 6 for defences, 7 for supply lines')
                target = 100
                
                while target > 7 or target < 0:
                    target = int(input('Which unit should be attacked?'))
                    if (target >= 0) and (target < 5):
                        if not isinstance (target_base.field[target],Card):
                            target = 100
                """
                    
                #Target has health removed    
                if target == 7:
                    target_base.supply_lines -= attacking_damage
                elif target == 6:
                    target_base.defences -= attacking_damage
                elif target == 5:
                    target_base.pop -= attacking_damage
                else:
                    #Both the attacker and target take damage based on the attack value of the other card
                    target_base.field[target].defence -= attacking_damage
                    self.field[attacker].defence -= target_base.field[target].attack // 2

                    #If either card has lost all their health they are removed from the field
                    if target_base.field[target].defence <= 0:
                        target_base.field[target] = None

                    if self.field[attacker].defence <= 0:
                        self.field[attacker] = None


    def copy(self):
        #Returns a copy of the current instance for use by the AI
        copy_pop = self.pop
        copy_sup = self.supply_lines
        copy_def = self.defences
        copy_deck = self._deck.copy()
        copy_hand = self._hand.copy()
        copy_field = self.field.copy()
        copyIsPlayer = self.isPlayer
        return Base(copy_deck, copy_pop, copy_sup, copy_def, copy_hand, copy_field, copyIsPlayer)

class Card(object):
    """
    Fields:
    _name
    _atk
    _def
    _ready

    Methods:
    __init__
    __str__
    Getters for _name, _atk, _def & _ready
    update_ready

    """

    def __init__(self, name, attack, defence):
        self._name = name
        self._atk = attack
        self._def = defence
        self._ready = 0


    def __str__(self):
        output = self._name +', '+str(self._atk)+', '+str(self._def)
        return output


    #Make sure this is only called when ready is less than 2
    def update_ready(self, position_on_field):
        if position_on_field == 5:
            self.ready += 1
        else:
            self.ready = 2


    #Getters
    @property
    def name(self):
        return self._name

    
    @property    
    def attack(self):
        return self._atk


    @property
    def defence(self):
        return self._def


    @property
    def ready(self):
        return self._ready

##End of classes

##Instantiates variables and objects

#Instances of Card
card_values = [['Behemoth',700,600],['Mutated Scorpion',800,400],['Scrap Tank',400,800],['Veteran Scavenger',300,300],['Mercenaries',400,300],['Saboteurs',500,200],['Heavy Weaponeers',600,400],['Lookout',300,100],['Wanderer',700,700],['Renegade Master',600,500]]
all_cards = []
for each_value in card_values:
    all_cards.append(Card(each_value[0], each_value[1], each_value[2]))

#Instances of Base
enemy_base = Base(8000,3500,3500,all_cards,[], [None, None, None, None, None], False) #When players can choose their own decks, change this as its just a list of all the cards I've created 
player_base = Base(8000,3500,3500,all_cards,[],[None, None, None, None, None], True)

#Global variables
game_finished = False

"""
Subroutines

display_board
player_act
player_turn
ai_turn
attack
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
                                    

# !! End the turn loop early if the player presses f
def player_act(action_no):
    """
    User takes an action in the game based on their input

    User is repeatedly asked for a character to determine the action they wish to take until they enter a valid one, then a
    dedicated subroutine is called based on which action the user chose to take. We then return a number to represent how many actions
    the player has taken this turn, and thus how many actions they can still take.

    Parameters:

        action_no: Represents the number of actions the player has taken this turn so far

    Returns:

        action_no: action_no has been increased before being returned, either by 1 to represent the new action taken, or all the way
                   to the total number of actions the player can take in the turn if they choose to take no further actions
    """
    #Gets valid input for which action to take
    action = 'z'
    while (action in ['a','p','f']) == False:
        print('Press a to attack, p to prepare a unit or f to finish your turn')
        print()
        action = str(input('Awaiting your command: '))

    #Calls subroutine based on which action the player has chosen to take
    if action == 'a':
        player_base.attack(enemy_base)
        return action_no + 1
    elif action == 'p':
        player_base.prepare()
        return action_no + 1
    elif action == 'f':
        return player_base.get_number_of_actions();


def player_turn():
    """
    Goes through the entire process of the player taking their turn, showing the necessary information and allowing them to make
    their moves.

    Starts by updating the readiness state of the cards on the player's field allowing cards that were placed the previous turn
    to now attack (unless it is in the sabotage position in which case it takes an extra turn), adds cards from the player's deck
    to their hand, then displays the state of the board and the player's hand to the player. From here we repeatedly call
    player_act(), allowing the player to take actions
    """
    #Iterates through the field, updating each card to be ready that isn't already
    for each_position in range(5):
        if player_base.field[each_position] != None:
            if player_base.field[each_position].ready != 2:
                player_base.field[each_position].update_ready(each_position)

    #player draws
    for cards_drawn in range(player_base.get_number_of_draws()):
        player_base.draw()

    #displays player's hand
    print('COMMAND MODULE V3.2.18')
    print('AVAILABLE UNITS: ')
    print()
    player_base.display_hand()

    #player acts as many times as they are possible
    action_number = 0
    while action_number < player_base.get_number_of_actions():
        action_number = player_act(action_number)
        display_board()


def ai_turn():
    pass



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

