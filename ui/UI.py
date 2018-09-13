from ui.TextOutput import TextOutput

# Will serve as a proxy between output and output libraries
# For now, it just links to the TextOutput library.

class UI:
    def __init__(self):
        return

    def show_text(self, text):
        TextOutput().show(text)

    def show_line(self, text):
        TextOutput().line(text)

    def show_options(self, options):
        TextOutput().options(options)

    def list_targets(self, targets):
        TextOutput().targets(targets)