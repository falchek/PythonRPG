from battle.battleeffect.EffectType import EffectType
from battle.battleeffect.BattleEffect import BattleEffect
from battle.targetselection.SingleAllyTargetSelection import SingleAllyTargetSelection
import random


class HealSpell(BattleEffect):
    def __init__(self, source_fighter):
        super().__init__(source_fighter, EffectType.healing)
        self.name = "Heal"
        self.selection_strategy = SingleAllyTargetSelection()

    def get_battle_text(self):
        return "Lowers his head and clears his mind..."

    def calculate_power(self):
        return self.source_fighter.magic * 10 + random.randint(1, 10)

'''class MeteorSpell(BattleEffect):
    def __init__(self, source_fighter):
        super().__init__(source_fighter, EffectType.magical)
        self.name = "Meteor"
        self.selection_strategy = AllEnemyTargetSelection()  # TODO:  Multiple target selection

    def get_battle_text(self):
        return ("The ground cracks around " + self.source_fighter.name + " as she gathers arcane energy!\n"
                + self.source_fighter.name + " casts Meteor!!")

    def calculate_power(self):
        return self.source_fighter.magic * 10 + random.randint(1, 25)'''
