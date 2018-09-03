from fighters.Fighter import Fighter
from fighters.players.Mike import Mike
from fighters.players.Courtney import Courtney
from fighters.monsters.Imp import Imp
from fighters.monsters.Kobold import Kobold
from battle.Battle import Battle
from battle.Party import Party

party = Party([Mike(), Courtney()])

monsters = Party([Kobold(),
                  Imp(),
                  Kobold(),
                  Imp(),
                  Imp(),
                  Kobold(),
                  Imp(),
                  Kobold(),
                  Imp(), ])

print("Welcome to le game")
print("------------------")


battle = Battle(party, monsters)
battle.fight()

