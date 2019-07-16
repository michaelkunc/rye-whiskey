import random


class Whiskey:
    def __init__(self):
        self.name = random.choice(["Whistle Pig", "Jameson", "Four Roses", "Koval"])
        self.type = random.choice(["Bourbon", "Scotch", "Rye", "Irish", "Canadian"])

    def __repr__(self):
        return f"name: {self.name} type: {self.type}"
