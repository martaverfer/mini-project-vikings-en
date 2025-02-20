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

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        if self.vikingArmy: 
            self.vikingArmy.append(viking)
        else: 
            self.vikingArmy = [viking]
    
    def addSaxon(self, saxon):
        # your code here
        if self.saxonArmy: 
            self.saxonArmy.append(saxon)
        else: 
            self.saxonArmy = [saxon]
    
    def vikingAttack(self):
        # your code here
        index_saxon = random.randint(0, 5)
        index_viking = random.randint(0, 5)
        damage = self.viking.strength
        self.saxon.health = self.saxon.receiveDamage(damage)
        print("A Saxon has died in combat")
        self.saxonArmy.pop(0)
        return 
    
    def saxonAttack(self):
        # your code here
        index_saxon = random.randint(0, 5)
        index_viking = random.randint(0, 5)
        damage = self.saxonArmy[0].strength
        print(f"{self.viking.name} has received {str(self.saxon.strength)} points of damage")
        self.vikingArmy.pop(0)
        return self.vikingArmy[0].receiveDamage(damage)
    
    def showStatus(self):
        # your code here
        string = ''
        if len(self.vikingArmy) == 0:
            string = 'Vikings have won the war of the century!'
        elif len(self.saxonArmy) == 0:
            string = 'Saxons have fought for their lives and survive another day...'
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            string = 'Vikings and Saxons are still in the thick of battle.'
        return string
    pass


