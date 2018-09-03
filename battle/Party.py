# represents a party in a battle

class Party:
    def __init__(self, party):
        self.party = party

    # gets the actionable memebrs who haven't been defeated.
    def get_actionable_members(self):
        actionable_members = []
        for member in self.party:
            if member.current_hp > 0:
                actionable_members.append(member)
        return actionable_members

    # These are for the battle display
    def display_party(self):
        self.print_horizontal_bar()
        self.print_party_names()
        self.print_party_hp()
        self.print_horizontal_bar()

    def print_horizontal_bar(self):
        for member in self.party:
            print("-" * 22, end="")
        print()

    def print_party_names(self):
        for member in self.party:
            print("|{:^20}|".format(member.name), end="")
        print()

    def print_party_hp(self):
        for member in self.party:
            print("|{:<20}|".format("HP: "+ str(member.current_hp) + "/"+str(member.max_hp)), end="")
        print()
