from ui.UserInput import UserInput

class TargetSelection:
    def __init__(self, viable_targets):
        self.viable_targets = viable_targets

    def select_target(self):
        return


class SingleEnemyTargetSelection(TargetSelection):
    def __init__(self, viable_targets):
        super().__init__(viable_targets)

    # select from viable enemy targets
    def select_target(self):
        print("Select your target:")
        index = UserInput().select_index_from_options(self.viable_targets)
        # always return an array!!!
        return [self.viable_targets[index]]

