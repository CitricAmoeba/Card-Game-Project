import random

class Base(object):     #Add '_' to the start to signify that this is an abstract class
    """
    Fields:

    pop (short for population)
    supply lines
    defences
    _deck
    _hand
    field

    Methods:

    __init__
    draw
    get_number_of_actions
    attack
    prepare

    """


    #'d' is repeated for some parameters to differentiate them
    #from keywords and the fields
    def __init__(self,population,sup_lines,deff,deck,hand,fieldd):
        self.pop = population
        self.supply_lines = sup_lines
        self.defences = deff
        self._deck = deck
        self._hand = hand
        self.field = fieldd


    def draw(self):         #Change these from constants when other bases are introduced
        if self.supply_lines > 2000:
            draws = 3
        elif self.supply_lines > 1000:
            draws = 2
        else:
            draws = 1

        while draws > 0 and len(self._hand)<10:
            self._hand.append(random.choice(self._deck))
            draws -= 1
            

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


    def test_import(self):
        print('Module imported successfully')
