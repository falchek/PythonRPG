from fighters.Fighter import Fighter
from fighters.players.Mike import Mike
from fighters.players.Courtney import Courtney
from fighters.monsters.Imp import Imp
from fighters.monsters.Kobold import Kobold
from battle.battleeffect.magic.FireballSpell import FireballSpell
from battle.battleeffect.magic.MeteorSpell import MeteorSpell
from battle.Battle import Battle
from battle.Party import Party

mike = Mike()
courtney = Courtney()

courtney.spells = [FireballSpell(courtney),
                   MeteorSpell(courtney)]

party = Party([mike, courtney])

monsters = Party([Kobold(),
                  Imp(),
                  Kobold()])


battle = Battle(party, monsters)
battle.fight()

