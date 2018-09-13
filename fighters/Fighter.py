from battle.battleeffect.RegularAttack import RegularAttack
from battle.battleeffect.EffectType import EffectType
from battle.round.RoundAction import RoundAction
from ui.UI import UI

import random


# this represents a generic fighter of any kind.


class Fighter:
    def __init__(self, name, hp, strength, defense, agility, magic):
        self.name = name
        self.current_hp = hp
        self.max_hp = hp
        self.strength = strength
        self.defense = defense
        self.agility = agility
        self.magic = magic

        self.spells = []


    # for now, just create a normal attack
    def create_round_action(self, target_fighter):
        action = RegularAttack(self, None)
        # target = target_fighter
        return RoundAction(action, target_fighter)

    #todo:  Add defensive or healing strategies
    def receive_battle_effect(self, battle_effect):
        if battle_effect.effect_type == EffectType.physical:
            damage = battle_effect.calculate_power() - self.defense
            if damage > 0:
                UI().show_text(self.name + " takes " + str(damage) + " damage!!!")
                self.current_hp -= damage
                self.faint()
            # TODO: apply physical strategy
        elif battle_effect.effect_type == EffectType.magical:
            damage = battle_effect.calculate_power() # TODO:  magical damage?  Resistance?
            if damage > 0:
                UI().show_text(self.name + " takes " + str(damage) + " magical damage!!!")
                self.current_hp -= damage
            return 0

    def faint(self):
        if self.current_hp <= 0:
            self.current_hp = 0
            UI().show_text(self.name + " has fainted!")

    def get_priority_strategy(self):
        return self.agility + (self.agility / 10 * random.choice(range(0, 6)))

