# print to screen and stuff here.
# all text automatically flushes for ease of debugging


class TextOutput:
    def __init__(self):
        return

    def show(self, text):
        print(text, flush=True)

    def line(self, text):
        print(text, end="", flush=True)

    def targets(self, targets):
        for count, target in enumerate(targets, start=1):
            print(str(count) + ") " + target.name, flush=True)
