from battle.battleeffect.EffectType import EffectType
from battle.battleeffect.TargetSelection import SingleEnemyTargetSelection
import random
# the strategy by which a battle effect is used.


class BattleEffect:
    def __init__(self, source_fighter, effect_type):
        self.source_fighter = source_fighter
        self.effect_type = effect_type
        self.selection_strategy = None

    def get_battle_text(self):
        return "insert battle attack"

    def calculate_power(self):
        return 0


class RegularAttack(BattleEffect):
    def __init__(self, source_fighter, viable_targets):
        super().__init__(source_fighter, EffectType.physical)
        self.selection_strategy = SingleEnemyTargetSelection(viable_targets)

    def get_battle_text(self):
        return self.source_fighter.name + " attacks with a regular attack!"

    def calculate_power(self):
        return self.source_fighter.strength * 1 + random.randint(1, 12)

class RunAction(BattleEffect):
    def __init__(self, source_fighter):
        self.source_fighter = source_fighter
        self.effect_type = None

    def get_battle_text(self):
        return self.source_fighter.name + " tried to run... but couldn't!!"
        # TODO:  Implement...
