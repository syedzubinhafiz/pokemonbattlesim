from __future__ import annotations
__author__ = "Mohamed Azhan"
__editor__ = "Syed Zubin Hafiz"
__last_modified__ = "19.04.2022"

from abc import abstractmethod


class PokemonBase:
    def __init__(self, hp: int, poke_type: str) -> None:
        """ initializes the variables using the amounts received as input.
        """
        BASE_LEVEL = 1
        self.hp = hp
        self.poke_type = poke_type
        self.level = BASE_LEVEL
        self.battle_status = False
        """ precondition
        """
        assert self.hp >= 0
        if not (self.poke_type == "GRASS" or self.poke_type == "FIRE" or self.poke_type == "WATER" or self.poke_type == "NONE" ):
            raise TypeError("please enter a string which  must be one of [GRASS, FIRE, WATER, NONE]")

    def get_hp(self) -> int:
        """returns pokemon's current hp
        """
        return self.hp

    def set_hp(self,hp:int) -> None:
        self.hp = hp

    def get_level(self) -> int:
        """returns pokemon's current level
        """
        return self.level

    def is_fainted(self) -> bool:
        """returns true if the pokemon has fainted
        """
        if self.hp <= 0:
            return True
        return False

    def level_up(self) -> None:
        """increases level by 1
        """
        self.level += 1

    @abstractmethod
    def get_speed(self) -> int:
        """ Returns pokemon's speed
        """
        pass

    @abstractmethod
    def get_attack_damage(self) -> int:
        """ Returns pokemon's attack damage
        """
        pass

    @abstractmethod
    def get_defence(self) -> int:
        """ returns the defence stat of the pokemon
        """
        pass

    def lose_hp(self, lost_hp: int) -> None:
        """ Decreases life by amount of lost_life
        :raises ValueError: if lost_life is negative
        """
        self.lost_hp = lost_hp

        # Assert that lost_life is positive
        if lost_hp <= 0:
            raise ValueError("lost_life must be a positive value")
        else:
            # Decrease life (update life value)
            self.hp = self.hp - self.lost_hp

    @abstractmethod
    def defend(self, other: PokemonBase) -> None:
        """  Evaluates the damage after being attacked and then changes hp accordingly.
        :raises ValueError: if damage is negative
        """
        damage = other.get_attack_damage()
        # Assert damage is >= 0
        if damage <= 0:
            raise ValueError("Damage must be a positive value")
        pass

    def get_poke_type(self) -> str:
        """returns the type fire/water/grass)
        """
        return self.poke_type

    def get_battle_status(self) -> bool:

        return self.battle_status

    def set_battle_status(self, status: bool) -> None:
        self.battle_status = status

    @abstractmethod
    def get_poke_name(self) -> str:
        """ Return pokemon's name
        """
        pass



    def __str__(self) -> str:
        """ Returns Charmander's ,Bulbasaur's and Squirtle's HP and Level units
        """
        return "{}'s HP = {} and level = {}".format(
            self.get_poke_name(), self.get_hp(), self.get_level())
