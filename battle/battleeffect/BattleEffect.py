# parent class for different battle effects.


class BattleEffect:
    def __init__(self, source_fighter, effect_type):
        self.source_fighter = source_fighter
        self.effect_type = effect_type
        self.selection_strategy = None

    def get_battle_text(self):
        return "insert battle attack"

    def calculate_power(self):
        return 0

