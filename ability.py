class Ability:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return self.damage

    def __repr__(self):
        return self.damage

