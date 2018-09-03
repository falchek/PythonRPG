from fighters.Fighter import Fighter

# Kobold monster

class Kobold(Fighter):
    def __init__(self):
        super().__init__("Kobold", 10, 5, 0)