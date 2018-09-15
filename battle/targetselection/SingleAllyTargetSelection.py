from battle.targetselection.TargetSelection import TargetSelection
from ui.UI import UI
from ui.UserInput import UserInput


class SingleAllyTargetSelection(TargetSelection):
    def __init__(self):
        super().__init__()

    # select from viable enemy targets
    def select_target(self, targets):
        allies = targets['ally']
        UI().show_text("Select your target:")
        UI().list_targets(allies)
        index = UserInput().select_index_from_options(allies)
        # always return an array!!!
        return [allies[index]]