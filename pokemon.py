__author__ = "Mohamed Azhan"
__editor__ = "Syed Zubin Hafiz, Justin Chuah"
__last_modified__ = "30.04.2022"

import random
from pokemon_base import PokemonBase


class Charmander(PokemonBase):
    def __init__(self):
        """ Initialises life and experience of the Charmander
        """
        super().__init__(7, "FIRE")
        self.BASE_HP = 7
        self.POKE_TYPE = "FIRE"
        self.POKE_NAME = "Charmander"
        self.BASE_LEVEL = 1
        self.BASE_ATTACK = 6
        self.BASE_DEFENCE = 4
        self.BASE_SPEED = 7

    def get_poke_name(self) -> str:
        return self.POKE_NAME

    def get_poke_type(self) -> str:
        """ Returns Charmander's type
        """
        return self.POKE_TYPE

    def get_hp(self) -> int:
        """ Returns Charmander's base hp
        """
        return self.BASE_HP

    def set_hp(self, hp: int) -> None:
        self.BASE_HP = hp

    def get_level(self) -> int:
        """ Returns Charmander's level
        """
        return self.BASE_LEVEL

    def level_up(self) -> None:
        """increases level by 1
        """
        self.BASE_LEVEL += 1

    def defend(self, other: PokemonBase) -> None:
        """Damage after being attacked
        """
        damage = other.get_attack_damage()
        rate = 1
        if other.get_poke_type() == "WATER":
            rate = 2
        if other.get_poke_type() == "GRASS":
            rate = 0.5
        damage *= rate
        if damage > self.get_defence():
            self.BASE_HP = self.get_hp() - damage
        else:
            self.BASE_HP = self.get_hp() - damage // 2

    def get_defence(self) -> int:
        """ Returns Charmander's base defence
        """
        return self.BASE_DEFENCE

    def get_speed(self) -> int:
        """ Returns Charmander's speed
        """
        return self.BASE_SPEED + self.BASE_LEVEL

    def get_attack_damage(self) -> int:
        """ Returns Charmander's attack damage
        """
        return self.BASE_ATTACK + self.BASE_LEVEL

    def is_fainted(self) -> bool:
        """ Returns true or false on Charmander's death
        """
        if self.get_hp() <= 0:
            return True
        return False


class Bulbasaur(PokemonBase):
    def __init__(self):
        """ Initialises life and experience of the Bulbasaur
        """
        super().__init__(9, "GRASS")
        self.POKE_NAME = "Bulbasaur"
        self.BASE_LEVEL = 1
        self.BASE_ATTACK = 5
        self.BASE_DEFENCE = 5
        self.BASE_SPEED = 7
        self.BASE_HP = 9
        self.POKE_TYPE = "GRASS"

    def get_poke_name(self) -> str:
        return self.POKE_NAME

    def get_poke_type(self) -> str:
        """ Returns Bulbasaur's type
        """
        return self.POKE_TYPE

    def get_hp(self) -> int:
        """ Returns Bulbasaur's hp
        """
        return int(self.BASE_HP)

    def set_hp(self, hp: int) -> None:
        self.BASE_HP = hp

    def get_level(self) -> int:
        """ Returns Bulbasaur's level
        """
        return self.BASE_LEVEL

    def level_up(self) -> None:
        """increases level by 1
        """
        self.BASE_LEVEL += 1

    def defend(self, other: PokemonBase) -> None:
        """Damage after being attacked
        """
        damage = other.get_attack_damage()
        rate = 1
        if other.get_poke_type() == "FIRE":
            rate = 2
        if other.get_poke_type() == "WATER":
            rate = 0.5
        damage *= rate
        if damage > self.get_defence() + 5:
            self.BASE_HP = self.get_hp() - damage
        else:
            self.BASE_HP = self.get_hp() - damage // 2

    def get_defence(self) -> int:
        """ Returns Bulbasaur's defence
        """
        return self.BASE_DEFENCE

    def get_speed(self) -> int:
        """ Returns Bulbasaur's speed
        """
        return self.BASE_SPEED + self.BASE_LEVEL // 2

    def get_attack_damage(self) -> int:
        """ Returns Bulbasaur's attack damage
        """
        return self.BASE_ATTACK

    def is_fainted(self) -> bool:
        """ Returns true or false depending on Bulbasaur's death
        """
        if self.get_hp() <= 0:
            return True
        return False


class Squirtle(PokemonBase):
    def __init__(self):
        """ Initialises life and experience of the Squirtle
        """
        super().__init__(8, "WATER")
        self.POKE_NAME = "Squirtle"
        self.BASE_LEVEL = 1
        self.BASE_ATTACK = 4
        self.BASE_DEFENCE = 6
        self.BASE_SPEED = 7
        self.BASE_HP = 8
        self.POKE_TYPE = "WATER"

    def get_poke_name(self) -> str:
        return self.POKE_NAME

    def get_poke_type(self) -> str:
        """ Returns Squirtle's type
        """
        return self.POKE_TYPE

    def get_hp(self) -> int:
        """ Returns Squirtle's hp
        """
        return self.BASE_HP

    def set_hp(self, hp: int) -> None:
        self.BASE_HP = hp

    def get_level(self) -> int:
        """ Returns Squirtle's level
        """
        return self.BASE_LEVEL

    def level_up(self) -> None:
        """increases level by 1
        """
        self.BASE_LEVEL += 1

    def defend(self, other: PokemonBase) -> None:
        """Damage after being attacked
        """
        damage = other.get_attack_damage()
        rate = 1
        if other.get_poke_type() == "GRASS":
            rate = 2
        if other.get_poke_type() == "FIRE":
            rate = 0.5
        damage *= rate
        if damage > self.get_defence() * 2:
            self.BASE_HP = self.get_hp() - damage
        else:
            self.BASE_HP = self.get_hp() - damage // 2

    def get_defence(self) -> int:
        """ Returns Squirtle's defence
        """
        return self.BASE_DEFENCE + self.BASE_LEVEL

    def get_speed(self) -> int:
        """ Returns Squirtle's speed
        """
        return self.BASE_SPEED

    def get_attack_damage(self) -> int:
        """ Returns Squirtle's atack damage
        """
        return self.BASE_ATTACK + self.BASE_LEVEL // 2

    def is_fainted(self) -> bool:
        """ Returns true or false depending on Squirtle's death
        """
        if self.get_hp() <= 0:
            return True
        return False


"""
A Glitched pokemon that is an amalgamation of the previous 3 pokemons, while also having unique actions of its own
"""


class GlitchMon(PokemonBase):
    def __init__(self, hp: int, poke_type: str):
        # initializing at this stage provides no value, hence the default values
        super().__init__(hp, poke_type)

    # Method to increase hp of GlitchMon
    def increase_hp(self, hp: int) -> None:
        if hp <= 0:
            raise ValueError("You are supposed to increase the HP! ")
        else:
            self.hp += hp

    # Special move-set of the GlitchMon, where it randomly selects an option
    # Overall complexity of this function is O(1)
    def superpower(self) -> None:
        random_int = random.randint(0, 2)
        if random_int == 0:
            self.level_up()
            return
        elif random_int == 1:
            self.increase_hp(1)
            return
        else:
            self.level_up()
            self.increase_hp(1)
            return


"""
An unidentifiable character that does not even look remotely close to a pokemon!
How did this even enter the game!
"""


class MissingNo(GlitchMon):
    # Initializing the life and experience of an error pokemon
    def __init__(self):
        ave_attack = (Charmander.get_attack_damage(Charmander()) + Bulbasaur.get_attack_damage(Bulbasaur()) +
                      Squirtle.get_attack_damage(Squirtle())) // 3
        ave_defence = (Charmander.get_defence(Charmander()) + Bulbasaur.get_defence(Bulbasaur()) +
                       Squirtle.get_defence(Squirtle())) // 3
        ave_speed = (Charmander.get_speed(Charmander()) + Bulbasaur.get_speed(Bulbasaur()) +
                     Squirtle.get_speed(Squirtle())) // 3
        PokemonBase.__init__(self, 8, "NONE")
        self.POKE_NAME = "MissingNo"
        self.BASE_LEVEL = 1
        self.BASE_ATTACK = ave_attack
        self.BASE_DEFENCE = ave_defence
        self.BASE_SPEED = ave_speed
        self.POKE_TYPE = "NONE"

    # Returns the name of Pokemon
    def get_poke_name(self) -> str:
        return self.POKE_NAME

    def get_poke_type(self) -> str:
        """ Returns MissingNo's type
        """
        return self.POKE_TYPE

    def get_hp(self) -> int:
        """ Returns MissingNo's hp
        """
        return self.hp

    # Sets the HP of the Pokemon to a specified amount
    def set_hp(self, hp: int) -> None:
        self.hp = hp

    def get_level(self) -> int:
        """ Returns MissingNo's level
        """
        return self.BASE_LEVEL

    def level_up(self) -> None:
        """increases level by 1
        """
        self.BASE_LEVEL += 1
        self.BASE_ATTACK += 1
        self.BASE_SPEED += 1
        self.increase_hp(1)
        self.BASE_DEFENCE += 1

    def defend(self, other: PokemonBase) -> None:
        """
        Has a 75% chance of calculating the damage after being attacked
        Has a 25% chance of using superpower, instead of receiving damage from the attack, it powers up instead!
        """
        rand_int = random.randint(0, 3)
        damage = other.get_attack_damage()

        if rand_int == 0:
            if damage > self.get_defence():
                self.hp = self.get_hp() - damage
            else:
                self.hp = self.get_hp() - damage // 2

        elif rand_int == 1:
            if damage > self.get_defence() + 5:
                self.hp = self.get_hp() - damage
            else:
                self.hp = self.get_hp() - damage // 2

        elif rand_int == 2:
            if damage > self.get_defence() * 2:
                self.hp = self.get_hp() - damage
            else:
                self.hp = self.get_hp() - damage // 2

        else:
            self.superpower()

    def get_defence(self) -> int:
        """ Returns MissingNo's defence
        """
        return self.BASE_DEFENCE

    def get_speed(self) -> int:
        """ Returns MissingNo's speed
        """
        return self.BASE_SPEED

    def get_attack_damage(self) -> int:
        """ Returns MissingNo's attack damage
        """
        return self.BASE_ATTACK

    def is_fainted(self) -> bool:
        """ Returns true or false depending on MissingNo's death
        """
        if self.get_hp() <= 0:
            return True
        return False
