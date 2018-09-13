from battle.targetselection.TargetSelection import TargetSelection
from ui.UI import UI
from ui.UserInput import UserInput


class AllEnemyTargetSelection(TargetSelection):
    def __init__(self):
        super().__init__()

    #select all enemy targets!
    def select_target(self, targets):
        return targets['enemy']

'''class SingleEnemyTargetSelection(TargetSelection):
    def __init__(self):
        super().__init__()

    # select from viable enemy targets
    def select_target(self, targets):
        enemies = targets['enemy']
        UI().show_text("Select your target:")
        UI().list_targets(enemies)
        index = UserInput().select_index_from_options(enemies)
        # always return an array!!!
        return [enemies[index]]'''