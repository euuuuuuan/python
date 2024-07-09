import random
import time

class Unit:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Player:
    def __init__(self):
        self.units = []

    def select_units(self):
        unit_names = ['Archer', 'Knight', 'Mage', 'Golem', 'Dragon']
        unit_count = random.randint(3, 5)  # Randomly select 3 to 5 units
        for _ in range(unit_count):
            name = random.choice(unit_names)
            damage = random.randint(10, 30)
            unit = Unit(name, damage)
            self.units.append(unit)

    def get_total_damage(self):
        total_damage = sum(unit.damage for unit in self.units)
        return total_damage

class Monster:
    def __init__(self, path_length):
        self.path_length = path_length
        self.position = 0
        self.attack_damage = random.randint(5, 15)

    def move(self):
        self.position += 1
        if self.position >= self.path_length:
            self.position = 0  # Reset position at the end of path

    def attack(self, player):
        player_damage = player.get_total_damage()
        player_health_loss = min(player_damage, self.attack_damage)
        player.units = [unit for unit in player.units if unit.damage > player_health_loss]
        print(f"Monster attacked! Player lost {player_health_loss} health.")

def main():
    path_length = 10  # Length of the player's defense path
    max_monsters = 150  # Maximum number of monsters
    player = Player()
    player.select_units()
    monsters = []
    monster_count = 0

    print("Welcome to Random Unit Defense!")
    print("Prepare your defenses...")

    while monster_count < max_monsters:
        time.sleep(1)  # Delay for better gameplay experience
        monster = Monster(path_length)
        monsters.append(monster)
        monster_count += 1

        for _ in range(path_length):
            print("-", end="")
        print("")

        for monster in monsters:
            print(" " * monster.position + "M")
            monster.move()

        print("Player's units: ", end="")
        for unit in player.units:
            print(f"{unit.name}({unit.damage}) ", end="")
        print("")

        print("Monsters: ", len(monsters))

        for monster in monsters:
            if monster.position == 0:
                monster.attack(player)

        if not player.units:
            print("Game over! All units destroyed.")
            break

    if monster_count >= max_monsters:
        print("Congratulations! You defended successfully against all monsters.")

if __name__ == "__main__":
    main()
