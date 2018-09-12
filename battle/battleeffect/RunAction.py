from battle.battleeffect.BattleEffect import BattleEffect

class RunAction(BattleEffect):
    def __init__(self, source_fighter):
        self.source_fighter = source_fighter
        self.effect_type = None

    def get_battle_text(self):
        return self.source_fighter.name + " tried to run... but couldn't!!"
        # TODO:  Implement...