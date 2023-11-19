# codewars practice Sh.Artem
# Create a function that returns the name of the winner in a fight between two fighters.

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    __repr__ = __str__


fighter1 = Fighter("Lew", 10, 2)
fighter2 = Fighter("Harry", 5, 4)
first_attacker = "Harry"


def declare_winner(fighter1, fighter2, first_attacker):
    if first_attacker == fighter1.name:
        while fighter1.health != 0 or fighter2.health != 0:
            fighter2.health = fighter2.health - fighter1.damage_per_attack
            if fighter2.health <= 0:
                a = fighter1.name
                break
            fighter1.health = fighter1.health - fighter2.damage_per_attack
            if fighter1.health <= 0:
                a = fighter2.name
                break
    else:
        while fighter1.health != 0 or fighter2.health != 0:
            fighter1.health = fighter1.health - fighter2.damage_per_attack
            if fighter2.health <= 0:
                a = fighter1.name
                break
            fighter2.health = fighter2.health - fighter1.damage_per_attack
            if fighter1.health <= 0:
                a = fighter2.name
                break
    return a


print(declare_winner(fighter1, fighter2, first_attacker))
