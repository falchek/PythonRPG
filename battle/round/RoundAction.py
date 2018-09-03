# The battleeffect that a fighter is taking in the current round

class RoundAction:
    def __init__(self, battle_effect, target):
        self.battle_effect = battle_effect;
        self.target = target;
        self.priority = battle_effect.source_fighter.get_priority_strategy()

    def apply_battle_effect(self):
        print(self.battle_effect.get_battle_text())
        if self.target is not None:
            self.target.receive_battle_effect(self.battle_effect)

