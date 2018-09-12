from battle.targetselection.TargetSelection import TargetSelection
from ui.UI import UI
from ui.UserInput import UserInput

class SingleEnemyTargetSelection(TargetSelection):
    def __init__(self, viable_targets):
        super().__init__(viable_targets)

    # select from viable enemy targets
    def select_target(self):
        UI().show_text("Select your target:")
        UI().list_targets(self.viable_targets)
        index = UserInput().select_index_from_options(self.viable_targets)
        # always return an array!!!
        return [self.viable_targets[index]]