import Base as base

class AI_Base(base.Base):

    def turn()

    def copy(self):
        #Returns a copy of the current instance for use by the AI
        copy_pop = self.pop
        copy_sup = self.supply_lines
        copy_def = self.defences
        copy_deck = self._deck.copy()
        copy_hand = self._hand.copy()
        copy_field = self.field.copy()
        return Base(copy_deck, copy_pop, copy_sup, copy_def, copy_hand, copy_field)
