import Base as base

class Player_Base(base.Base):

    def display_hand(self):
        for each_card in self._hand:
            print(each_card.name + ', ' + str(each_card.attack) + ', ' + str(each_card.defence))
        

    def turn():
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
        player_base.draw()

        #displays player's hand
        print('COMMAND MODULE V3.2.18')
        print('AVAILABLE UNITS: ')
        print()
        player_base.display_hand()

        #player acts as many times as they are possible
        action_number = 0

        #!! Refactor this
        while action_number < player_base.get_number_of_actions():
            action_number = player_act(action_number)
            display_board()


    #!! Still has enemy_base hardcoded
    #!! End the turn loop early if the player presses f
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
            self.attack(enemy_base)
            return action_no + 1
        elif action == 'p':
            self.prepare()
            return action_no + 1
        elif action == 'f':
            return player_base.get_number_of_actions();
