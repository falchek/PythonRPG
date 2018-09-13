from battle.battlemenu.AttackOption import AttackOption
from battle.battlemenu.MagicOption import MagicOption
from battle.battlemenu.RunOption import RunOption
from ui.UserInput import UserInput
from ui.UI import UI
# Creates and accepts the input for the party against the monsters.

class BattleMenu:
    def __init__(self, targets):
        self.targets = targets

    # gets the user input for each round.

    def begin_menu_selection(self):
        round_actions = []
        for fighter in self.targets['ally']:
            UI().show_text(fighter.name + "'s turn!")
            # TODO:  Get the round options from the Fighter themselves.
            '''battle_options = [AttackOption(fighter, self.targets),
                              MagicOption(fighter, self.targets),
                              RunOption(fighter, None)]'''
            battle_options = self.get_options_for_fighter(fighter)
            self.show_options(battle_options)
            selected_actions = self.select_action(battle_options)
            # generate the action from battle effects and an array of selected targets, and add them the the queue

            round_actions.append(selected_actions)

        return round_actions

    # there is only one option right now:  Attack
    def show_options(self, battle_options):
        for count, option in enumerate(battle_options, start=1):
            UI().show_text(str(count) + ") " + option.name)

    # gets legal options for a fighter
    def get_options_for_fighter(self, fighter):
        battle_options = []
        battle_options.append(AttackOption(fighter, self.targets))
        if len(fighter.spells) > 0:
            battle_options.append(MagicOption(fighter, self.targets))
        battle_options.append(RunOption(fighter, None))
        return battle_options

    # gets an action by index
    def select_action(self, battle_options):
        index = UserInput().select_index_from_options(battle_options)
        return battle_options[index].generate_round_actions()
