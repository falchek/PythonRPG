from battle.battlemenu.BattleOption import BattleOptions
from battle.round.RoundAction import RoundAction
from battle.battleeffect.RegularAttack import RegularAttack

#  Represents just a regular attack:


class AttackOption(BattleOptions):
    def __init__(self, fighter, targets):
        super().__init__("Attack", fighter, targets)

    def generate_round_actions(self):
        action = RegularAttack(self.fighter, self.targets)
        target = action.selection_strategy.select_target()
        return RoundAction(action, target)