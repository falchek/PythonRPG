from battle.round.RoundAction import RoundAction
from battle.battleeffect.BattleEffect import RegularAttack
from battle.battleeffect.BattleEffect import RunAction

class BattleOptions:
    def __init__(self, name, fighter, targets):
        self.name = name
        self.fighter = fighter
        self.targets = targets # represents valid targets


    def get_action(self):
        return

    # strategy chooses a single target!
    def choose_single_target(self):
        print("Select your target:")
        self.print_targets()
        need_target = True
        while need_target:
            try:
                target_index = int(input("Select target")) - 1
                if target_index in range(0, len(self.targets)):
                    return self.targets[target_index]
                else:
                    print("Select a number between 1 and " + str(len(self.targets - 1)))
            except ValueError:
                print("Must be a number!")

    def print_targets(self):
        index = 1
        for target in self.targets:
            print(str(index) + ")" + target.name)
            index += 1


#  Represents just a regular attack:

class AttackOption(BattleOptions):
    def __init__(self, fighter, targets):
        super().__init__("Attack", fighter, targets)

    def get_action(self):
        target = self.choose_single_target()
        return RoundAction(RegularAttack(self.fighter), target)


class RunOption(BattleOptions):
    def __init__(self, fighter, targets):
        super().__init__("Run", fighter, targets)

    def get_action(self):
        return RoundAction(RunAction(self.fighter), None)

