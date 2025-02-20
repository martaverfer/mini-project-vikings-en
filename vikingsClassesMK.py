import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.strength = 150
        self.health = 300
    
    def attack(self):
      return self.strength

    def receiveDamage(self, damage):
      self.health = self.health - damage
      
    

# Viking
""" 
class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here

    def battleCry(self):
        # your code here

    def receiveDamage(self, damage):
        # your code here """

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
      self.health = 60
      self.strength = 25


    def receiveDamage(self, damage):
        self.health = self.health - damage
        string = ''
        if self.health > 0:
            string = (f"A Saxon has received {damage} points of damage")
        elif self.health == 0:
            string = 'A Saxon has died in combat'
        return string

# Davicente