
import random
import math

class Warrior:

    def __init__(self, name="Warrior",health = 0, attkMax = 0, blockMax = 0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() - 0.5)
        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() - 0.5)


class Battle:

    def startFight(self,warriorA, warriorB):

        while(True):
             if self.getAttackResult(warrior1, warrior2) == "Game Over":
                  print("Game Over")
                  break
             elif self.getattackresult(warrior1, warrior2) == "Game Over":
                 print("Game Over")
                 break

    @staticmethod
    def getattackresult(warriorA, warriorB):
     warriorAAttAmt = warriorA.attack()
     warriorBBlockAmt = warriorB.block()
     damage_to_warrior = math.ceil(warriorAAttAmt - warriorBlockAmt)
     warriorB.health = warriorB.health - damage_to_warriorB
     print("{} attack {} and deals {} damage".format(warriorA.name, warriorA.health, damage_to_warrior))

     if warriorB.health <= damage_to_warrior:
         print("{} has died and {] is Victorius".format(warriorB, warriorA.health))
         return "Game Over"
     else:
         return "Fight again"

def main():
    Sam = warriors.Warrior("Sam", 50, 20,10)
    Paul = warriors.Warrior("Paul", 50, 20,10)

    battle = Battle()



