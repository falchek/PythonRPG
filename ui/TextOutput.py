# print to screen and stuff here.i


class TextOutput:
    def __init__(self):
        return

    def show(self, text):
        print(text)

    def line(self, text):
        print(text, end="")

    def targets(self, targets):
        for count, target in enumerate(targets, start=1):
            print(str(count) + ") " + target.name)
