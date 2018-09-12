from ui.UI import UI

# represents a party in a battle
# TODO:  You'll need to do a lot here when it's graphics time, and maybe separate these concerns

class Party:

    def __init__(self, party):
        self.MAX_ROW_SIZE = 4
        self.party = party

    # gets the actionable members who haven't been defeated.
    def get_actionable_members(self):
        actionable_members = []
        for member in self.party:
            if member.current_hp > 0:
                actionable_members.append(member)
        return actionable_members

    # These are for the battle display
    def display_party(self):
        actionable_members = self.get_actionable_members()
        rows = self.create_battle_rows(actionable_members)
        for row in rows:
            self.print_horizontal_bar(row)
            self.print_party_names(row)
            self.print_party_hp(row)
            self.print_horizontal_bar(row)

    def create_battle_rows(self, party):
        for i in range(0, len(party), self.MAX_ROW_SIZE):
            yield party[i:(i + self.MAX_ROW_SIZE)]

    def print_horizontal_bar(self, row):
        self.get_indent(row)
        for member in row:
            UI().show_line("-" * 22)
        UI().show_text("")

    def print_party_names(self, row):
        self.get_indent(row)
        for member in row:
            UI().show_line("|{:^20}|".format(member.name))
        UI().show_text("")

    def print_party_hp(self, row):
        self.get_indent(row)
        for member in row:
            UI().show_line("|{:<20}|".format("HP: "+ str(member.current_hp) + "/"+str(member.max_hp)))
        UI().show_text("")

    # Gets the proper indent for the party
    def get_indent(self, row):
        UI().show_line(" " * 11 * (self.MAX_ROW_SIZE - len(row)))
