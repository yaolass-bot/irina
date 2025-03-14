
def is_alive(self):
        return self.health > 0

def battle (warrior1,warrior2):
        print("--- Battle Start!")
        while warrior1.is_alive() and warrior2.is_alive():
               warrior1.attack_enemy(warrior2)
if not warrior2.is_alive():
        print(f"{warrior2.name}" is defeated)
if not warrior.is_alive():
        print(f"{warrior1.name}" is defaeated)
        breakpoint



