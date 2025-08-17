# COMBINED SUPERHERO (THE FLASH) AND POLYMORPHISM DEMONSTRATION

# ========================
# PART 1: THE FLASH CLASS
# ========================

class Superhero:
    def __init__(self, name, secret_identity, base_of_operations):
        self.name = name
        self.secret_identity = secret_identity
        self.base_of_operations = base_of_operations
        self.powers = []
        self.health = 100
    
    def add_power(self, power):
        self.powers.append(power)
        print(f"Added new power: {power}!")
    
    def use_power(self, power_index):
        if power_index < len(self.powers):
            print(f"{self.name} uses {self.powers[power_index]}!")
        else:
            print("Power not available!")
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage! Health: {self.health}")
        if self.health <= 0:
            print(f"{self.name} has been defeated! 😵")
    
    def display_info(self):
        print(f"\n{self.name} (Secret Identity: {self.secret_identity})")
        print(f"Base: {self.base_of_operations}")
        print(f"Health: {self.health}")
        print("Powers:")
        for i, power in enumerate(self.powers):
            print(f"  {i+1}. {power}")


class TheFlash(Superhero):
    def __init__(self, secret_identity="Barry Allen", base_of_operations="Central City"):
        super().__init__("The Flash", secret_identity, base_of_operations)
        self.speed = 0  # Mach speed
        self.add_power("Superhuman speed")
        self.add_power("Time travel")
        self.add_power("Phasing through objects")
        self.add_power("Speed Force aura")
    
    def run(self, mach_speed):
        self.speed = mach_speed
        if mach_speed > 10:
            print(f"⚡ {self.name} runs at Mach {mach_speed} - breaking the time barrier! ⏳")
        else:
            print(f"⚡ {self.name} runs at Mach {mach_speed} - faster than a bullet! 💨")
    
    def time_remnant(self):
        print(f"{self.name} creates a time remnant from the Speed Force! ⏳👥")
    
    def infinite_mass_punch(self):
        print(f"{self.name} delivers an INFINITE MASS PUNCH! 💥")
        return 50  # Damage amount
    
    def display_info(self):
        super().display_info()
        print(f"Current Speed: Mach {self.speed}")


# =============================
# PART 2: POLYMORPHISM CHALLENGE
# =============================

class HeroMovement:
    def move(self):
        pass


class SpeedsterMovement(HeroMovement):
    def __init__(self, hero_name):
        self.hero_name = hero_name
    
    def move(self):
        return f"⚡ {self.hero_name} runs at light speed, leaving a lightning trail!"


class FlyingMovement(HeroMovement):
    def __init__(self, hero_name):
        self.hero_name = hero_name
    
    def move(self):
        return f"🦅 {self.hero_name} soars through the clouds with majestic grace!"


class TeleportMovement(HeroMovement):
    def __init__(self, hero_name):
        self.hero_name = hero_name
    
    def move(self):
        return f"💫 {self.hero_name} disappears in a flash and reappears instantly!"


class SwingingMovement(HeroMovement):
    def __init__(self, hero_name):
        self.hero_name = hero_name
    
    def move(self):
        return f"🕷️ {self.hero_name} swings between buildings using web lines!"


# ===================
# DEMONSTRATION CODE
# ===================

def main():
    print("=== THE FLASH DEMONSTRATION ===")
    flash = TheFlash()
    flash.display_info()
    
    print("\n=== FLASH IN ACTION ===")
    flash.run(5)
    flash.run(15)  # Time travel speed
    flash.use_power(2)  # Phasing through objects
    flash.time_remnant()
    
    print("\n=== POLYMORPHISM DEMO ===")
    hero_movements = [
        SpeedsterMovement("The Flash"),
        FlyingMovement("Superman"),
        TeleportMovement("Nightcrawler"),
        SwingingMovement("Spider-Man")
    ]
    
    for movement in hero_movements:
        print(movement.move())
    
    print("\n=== FLASH SPECIAL MOVEMENT ===")
    for _ in range(3):
        print(SpeedsterMovement("Barry Allen").move())

if __name__ == "__main__":
    main()