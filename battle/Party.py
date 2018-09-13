from ui.UI import UI

# represents a party in a battle
# TODO:  You'll need to do a lot here when it's graphics time, and maybe separate these concerns

class Party:

    def __init__(self, party):
        self.party = party

    # gets the actionable members who haven't been defeated.
    def get_actionable_members(self):
        return [member for member in self.party if member.current_hp > 0]
        '''actionable_members = []
        for member in self.party:
            if member.current_hp > 0:
                actionable_members.append(member)
        return actionable_members'''

