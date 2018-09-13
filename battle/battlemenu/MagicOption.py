from battle.battlemenu.BattleOption import BattleOptions
from battle.round.RoundAction import RoundAction
from battle.battleeffect.RegularAttack import RegularAttack
from ui.UI import UI
from ui.UserInput import UserInput

#  Represents a menu of magical attacks:
#  viable targets are represented as a dictionary of arrays


class MagicOption(BattleOptions):
    def __init__(self, fighter, targets):
        self.targets = targets
        super().__init__("Magic", fighter, targets)

    def generate_round_actions(self):
        if len(self.fighter.spells) > 0:
            UI().show_options(self.fighter.spells)
            index = UserInput().select_index_from_options(self.fighter.spells)
            action = self.fighter.spells[index]
            target = action.selection_strategy.select_target(self.targets) # get selection strategy from action!
            return RoundAction(action, target)
        else:
            print("no spells.")  # this should never appear.
