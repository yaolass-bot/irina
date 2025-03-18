
import random


class Warrior:

    def __init__(self, name="Warrior", health=0, damage=0, blockChance=0.0):
        self.name = name
        self.health = health
        self.damage = damage
        self.blockChance = blockChance

    def Attack(self, enemyWarrior):
        if enemyWarrior.TryBlock():
            print("Не удалось нанести урон по", enemyWarrior.name)
        else:
            enemyWarrior.health -= self.damage
            print(self.name, "наносит", self.damage, "урона по", enemyWarrior.name)

            def is_alive(self):

                return self.health > 0

        def battle(warrior1, warrior2):

            print("--- Battle Start!")

            while warrior1.is_alive() and warrior2.is_alive():
                warrior1.attack_enemy(warrior2)

        if not warrior2.is_alive():
            print(f"{warrior2.name}" is defeated)

        if not warrior.is_alive():
            print(f"{warrior1.name}" is defaeated)

            breakpoint


def TryBlock(self):
        roll = random.random()  # random.random() выдает рандомное вещественное число от 0 до 1

        if roll < self.blockChance:
            return True  # смог заблокировать

        return False  # не смог заблокировать











