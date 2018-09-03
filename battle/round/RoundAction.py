# The battleeffect that a fighter is taking in the current round

class RoundAction:
    def __init__(self, battle_effect, target):
        self.battle_effect = battle_effect;
        self.target = target;
        self.priority = 0  #TODO: generate source from targetFighter and priority strategy

    def apply_battle_effect(self):
        print(self.battle_effect.get_battle_text());
        self.target.receive_battle_effect(self.battle_effect)

