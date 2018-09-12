from battle.round.RoundAction import RoundAction
from battle.battleeffect.RunAction import RunAction
from battle.battlemenu.BattleOption import BattleOptions

# Run away!

class RunOption(BattleOptions):
    def __init__(self, fighter, targets):
        super().__init__("Run", fighter, targets)

    def generate_round_actions(self):
        return RoundAction(RunAction(self.fighter), None)

