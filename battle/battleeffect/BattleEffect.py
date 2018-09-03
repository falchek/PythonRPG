from battle.battleeffect.EffectType import EffectType
import random
# the strategy by which a battle effect is used.


class BattleEffect:
    def __init__(self, source_fighter, effect_type):
        self.source_fighter = source_fighter
        self.effect_type = effect_type

    def get_battle_text(self):
        return "insert battle attack"

    def calculate_power(self):
        return 0;


class RegularAttack(BattleEffect):
    def __init__(self, source_fighter):
        self.source_fighter = source_fighter
        self.effect_strategy = 0 #TODO:  create normal attack strategy
        self.effect_type = EffectType.physical

    def get_battle_text(self):
        return self.source_fighter.name + " attacks with a regular attack!"

    def calculate_power(self):
        return self.source_fighter.strength * 1 + random.randint(1, 12)
