from battle.battleeffect.BattleEffect import RegularAttack
from battle.battleeffect.EffectType import EffectType
from battle.round.RoundAction import RoundAction
import random
from battle.BattleOption import AttackOption
from battle.BattleOption import RunOption
# this represents a generic fighter of any kind.


class Fighter:
    def __init__(self, name, hp, strength, defense, agility):
        self.name = name
        self.current_hp = hp
        self.max_hp = hp
        self.strength = strength
        self.defense = defense
        self.agility = agility


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
                print(self.name + " takes " + str(damage) + " damage!!!")
                self.current_hp = self.current_hp - damage
                self.faint()
            # TODO: apply physical strategy
        elif battle_effect.effect_type == EffectType.magical:
            # TODO:  Add magic damage
            return 0

    def faint(self):
        if self.current_hp <= 0:
            self.current_hp = 0
            print(self.name + " has fainted!")

    def get_priority_strategy(self):
        return self.agility # + (self.agility / 10 * random.random(0, 6))

