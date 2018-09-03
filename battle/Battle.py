from battle.round.Round import Round
from battle.BattleMenu import BattleMenu
from battle.round.Round import RoundAction
from operator import attrgetter

import random
# represents a battle


class Battle:
    def __init__(self, party, monsters):
        self.party = party
        self.monsters = monsters

    def print_battlefield(self):
        self.monsters.display_party()
        self.print_field()
        self.party.display_party()

    #TODO:  Maybe print some fun ascii art later
    def print_field(self):
        print()
        print()
        print()

    # the main loop for fights
    def fight(self):
        win = False
        lose = False
        while not win | lose:
            print("New Round!")
            self.print_battlefield()

            actions = BattleMenu(self.party, self.monsters).begin_menu_selection()
            actions.extend(self.get_random_monster_actions())

            actions = self.sort_actions_by_priority(actions)
            new_round = Round(actions)
            new_round.process_round_actions()

            if len(self.party.get_actionable_members()) == 0:
                lose = True
            elif len(self.monsters.get_actionable_members()) == 0:
                win = True

            print()
            print()
        if win:
            print("You've won the battle!!")
        elif lose:
            print("You've lost the battle...")

    def sort_actions_by_priority(self, actions):
        actions = sorted(actions, key=attrgetter('priority'), reverse=True)
        return actions

    def get_random_monster_actions(self):
        actions = []
        '''for member in self.party.get_actionable_members():
            action = member.create_round_action(random.choice(self.monsters.party))  # get rand
            actions.append(action)'''

        for monster in self.monsters.get_actionable_members():
            action = monster.create_round_action(random.choice(self.party.party))
            actions.append(action)
        return actions