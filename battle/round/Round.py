from battle.round.RoundAction import RoundAction
# Contains the processing for fighters and round actions

class Round:
    def __init__(self, round_actions):
        self.round_actions = round_actions

    # processes the round actions one by one...
    def process_round_actions(self):
        for action in self.round_actions:
            if action.targets is None:
                print(action.battle_effect.get_battle_text())
            elif action.battle_effect.source_fighter.current_hp > 0:
                action.apply_battle_effect()
