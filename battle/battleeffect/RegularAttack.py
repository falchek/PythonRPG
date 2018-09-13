from battle.battleeffect.EffectType import EffectType
from battle.battleeffect.BattleEffect import BattleEffect
from battle.targetselection.SingleEnemyTargetSelection import SingleEnemyTargetSelection
import random

# This will eventually be defunct as I create other kinds of attacks.


class RegularAttack(BattleEffect):
    def __init__(self, source_fighter, viable_targets):
        super().__init__(source_fighter, EffectType.physical)
        self.selection_strategy = SingleEnemyTargetSelection()

    def get_battle_text(self):
        return self.source_fighter.name + " attacks with a regular attack!"

    def calculate_power(self):
        return self.source_fighter.strength * 1 + random.randint(1, 12)