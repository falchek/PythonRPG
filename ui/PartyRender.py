from ui.UI import UI
from battle.Party import Party

class PartyRender:
    # These are for the battle display
    def __init__(self, party):
        self.party = party
        self.MAX_ROW_SIZE = 4

    def display_party(self):
        actionable_members = self.party.get_actionable_members()
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
