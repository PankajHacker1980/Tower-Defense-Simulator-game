import random
import time

class TowerDefense:
    def __init__(self):
        self.path_length = 20  # Length of the path enemies travel
        self.enemy_types = ['Goblin', 'Orc', 'Troll']
        self.wave_number = 0
        self.enemy_wave = []
        self.towers = []
        self.gold = 100
        self.health = 10
    
    def generate_wave(self):
        self.wave_number += 1
        num_enemies = random.randint(3, 5) + self.wave_number
        self.enemy_wave = [random.choice(self.enemy_types) for _ in range(num_enemies)]
        print(f"Wave {self.wave_number} Incoming! Enemies: {', '.join(self.enemy_wave)}")
    
    def display_status(self):
        print(f"\nCurrent Status:")
        print(f"Gold: {self.gold}")
        print(f"Health: {self.health}")
    
    def place_tower(self):
        while True:
            print(f"Available Towers: Basic Tower (cost: 30 gold)")
            choice = input("Enter tower name to place or 'done' to finish: ").strip().lower()
            
            if choice == 'done':
                break
            elif choice == 'basic tower' and self.gold >= 30:
                self.towers.append('Basic Tower')
                self.gold -= 30
                print("Basic Tower placed!")
            else:
                print("Insufficient gold or invalid tower choice.")
    
    def run_wave(self):
        for enemy in self.enemy_wave:
            print(f"\nEnemy {enemy} is advancing!")
            time.sleep(1)
            if random.random() < 0.3:
                print(f"You defeated {enemy}!")
            else:
                self.health -= 1
                print(f"{enemy} reached the end! You lose 1 health.")
                if self.health <= 0:
                    print("Game Over! You lost all your health.")
                    return False
            time.sleep(1)
        print("Wave cleared!")
        self.gold += 10 + self.wave_number * 5
        return True
    
    def play_game(self):
        print("Welcome to Tower Defense Simulator!")
        print("Defend your path from waves of enemies.")
        
        while self.health > 0:
            self.generate_wave()
            self.display_status()
            self.place_tower()
            if not self.run_wave():
                break
            
            time.sleep(1)
        
        print(f"Game Over! Waves survived: {self.wave_number}")

if __name__ == "__main__":
    game = TowerDefense()
    game.play_game()
