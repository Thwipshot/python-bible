import random

class Coin:

    def __init__(self, rare = False, clean = True):
        self.is_rare = rare
        self.is_clean = clean

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self)
        self.colour = self.clean_colour

    def __del__(self):
        print("Coin spent!")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

class Pound:

    def __init__(self, rare=False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
        
        self.value = 1.00
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5 # mm
        self.thickness = 3.15 # mm
        self.heads = True

    def rust(self):
        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self):
        print("Coin spent!")



