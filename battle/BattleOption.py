from battle.round.RoundAction import RoundAction
from battle.battleeffect.BattleEffect import RegularAttack
from battle.battleeffect.BattleEffect import RunAction

class BattleOptions:
    def __init__(self, name, fighter, targets):
        self.name = name
        self.fighter = fighter
        self.targets = targets


    def generate_round_actions(self):
        return

#  Represents just a regular attack:

class AttackOption(BattleOptions):
    def __init__(self, fighter, targets):
        super().__init__("Attack", fighter, targets)

    def generate_round_actions(self):
        action = RegularAttack(self.fighter, self.targets)
        target = action.selection_strategy.select_target()
        return RoundAction(action, target)


class RunOption(BattleOptions):
    def __init__(self, fighter, targets):
        super().__init__("Run", fighter, targets)

    def generate_round_actions(self):
        return RoundAction(RunAction(self.fighter), None)

