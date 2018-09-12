from ui.UI import UI

# Gets user input from keyboardddd.

class UserInput:
    def __init__(self):
        pass

    def select_index_from_options(self, options):
        while True:
            selection = input("Choose a selection:  ")
            if selection.isdigit():
                selection = int(selection)
                if self.__within_bounds(selection, options):
                    # We're not zero indexing these,
                    return selection - 1
            else:
                UI().show_text("Input must be numeric!")


    def __within_bounds(self, index, options):
        if index - 1 in range(0, len(options)):
            return True
        else:
            UI().show_text("Pick a valid option!")
            return False

    # def select_target_from_list(self, options):
