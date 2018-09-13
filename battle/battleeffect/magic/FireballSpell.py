from battle.battleeffect.EffectType import EffectType
from battle.battleeffect.BattleEffect import BattleEffect
from battle.targetselection.SingleEnemyTargetSelection import SingleEnemyTargetSelection
import random


class FireballSpell(BattleEffect):
    def __init__(self, source_fighter):
        super().__init__(source_fighter, EffectType.magical)
        self.name = "Fireball"
        self.selection_strategy = SingleEnemyTargetSelection()

    def get_battle_text(self):
        return (self.source_fighter.name + "'s hands glow with light and heat! "
                + self.source_fighter.name + " casts Fireball!!")

    def calculate_power(self):
        return self.source_fighter.magic * 2 + random.randint(1, 25)
