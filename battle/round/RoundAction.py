# The battleeffect that a fighter is taking in the current round

class RoundAction:
    def __init__(self, battle_effect, targets):
        self.battle_effect = battle_effect;
        self.targets = targets;
        self.priority = battle_effect.source_fighter.get_priority_strategy()

    def apply_battle_effect(self):
        print(self.battle_effect.get_battle_text())
        if self.targets is not None:
            for target in self.targets:
                if target.current_hp > 0:  # test if dead
                    target.receive_battle_effect(self.battle_effect)

