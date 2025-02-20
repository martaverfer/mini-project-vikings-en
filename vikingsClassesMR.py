import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.strength = 150
        self.health = 300
    
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health = self.health - damage
    
# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
          # your code here
          super().__init__(health=health, strength=strength)
          self.name = name
        
    def battleCry(self):
        return 'Odin Owns You All!'

    def receiveDamage(self, damage):
        # your code here
        self.health = self.health - damage
        if damage != 0:
            if self.health >0:
                return f"{self.name} has received {damage} points of damage"
            elif self.health <= 0:
                return f"{self.name} has died in act of combat"

# Saxon

# class Saxon(Soldier):
#     def __init__(self, health, strength):
#         # your code here

#     def receiveDamage(self, damage):
#         # your code here

# # Davicente

# class War():
#     def __init__(self):
#         # your code here

#     def addViking(self, viking):
#         # your code here
    
#     def addSaxon(self, saxon):
#         # your code here
    
#     def vikingAttack(self):
#         # your code here
    
#     def saxonAttack(self):
#         # your code here

#     def showStatus(self):
#         # your code here
    


