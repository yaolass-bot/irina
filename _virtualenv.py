
import random
import math

class Warrior:

    def __init__(self, name="Warrior"):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.attkMax = attkMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() - 0.5)
        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() - 0.5)


class Battle:

    def startFight(self,warrior1, warrior2):

        while(True):
             if self.getAttackResult(warrior1, warrior2) == "Game Over":
                  print("Game Over")
                  break
    @staticmethod
    def getattackresult(warrior1, warrior2):
     warriorAAttAmt = warriorA.attack()
     warriorBlockAmt = warriorA.block()
     damage_to_warrior = math.ceil(warriorAAttAmt / warriorBlockAmt)
     warrior2.health = warriorA.health - damage_to_warrior



     if warriorA.health <= damage_to_warrior:
         print("{} has died and {] is Victorius".format(warrior1, warriorA.health))
         return "Game Over"
def main():
    Sam = warriors.Warrior("Sam", 50, 20,10)
    Paul = warriors.Warrior("Paul", 50, 20,10)

    battle = Battle()



