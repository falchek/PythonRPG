from battle.BattleOption import BattleOptions
from battle.BattleOption import AttackOption
from battle.BattleOption import RunOption
# Creates and accepts the input for the party against the monsters.

class BattleMenu:
    def __init__(self, party, monsters):
        self.party = party
        self.monsters = monsters

    # gets the user input for each round.

    def begin_menu_selection(self):
        round_actions = []
        for fighter in self.party.get_actionable_members():
            print(fighter.name + "'s turn!")
            battle_options = [AttackOption(fighter, self.monsters.get_actionable_members()),
                              RunOption(fighter, None)]
            self.show_options(battle_options)
            selected_action = self.select_action(fighter, battle_options)
            round_actions.append(selected_action)

        return round_actions

    # there is only one option right now:  Attack
    def show_options(self, battle_options):
        index = 1
        for option in battle_options:
            print(str(index) + ") " + option.name)
            index += 1


    # gets an action
    def select_action(self, fighter, battle_options):
        need_option = True
        while need_option:
            try:
                option = int(input("Choose a selection!")) - 1
                if option in range(0, len(battle_options)):
                    need_option = False
                    return battle_options[option].get_action()
            except ValueError:
                print("Option needs to be numeric!")

