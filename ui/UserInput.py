

# Gets user input from keyboardddd.

class UserInput:
    def __init__(self):
        pass

    def select_index_from_options(self, options):
        while True:
            option = input("Choose a selection!")
            if option.isdigit():
                option = int(option)
                if self.__within_bounds(option, options):
                    # We're not zero indexing these,
                    return option - 1
            else:
                print("Input must be numeric!")


    def __within_bounds(self, index, options):
        if index - 1 in range(0, len(options)):
            return True
        else:
            print("Pick a valid option!")
            return False

    # def select_target_from_list(self, options):
