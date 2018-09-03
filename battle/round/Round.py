from battle.round.RoundAction import RoundAction
# Contains the processing for fighters and round actions

class Round:
    def __init__(self, round_actions):
        self.round_actions = round_actions

    def process_round_actions(self):
        for action in self.round_actions:
            if action.battle_effect.source_fighter.current_hp > 0 and action.target.current_hp > 0:
                action.apply_battle_effect()
