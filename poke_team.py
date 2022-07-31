__author__ = "Mohamed Azhan"
__editor__ = "Syed Zubin , Justin Chuah, Chua Jun Jie"
__last_modified__ = "30.04.2022"

from array_sorted_list import ArraySortedList
from pokemon import Charmander, Bulbasaur, Squirtle, MissingNo
from stack_adt import ArrayStack
from queue_adt import CircularQueue, Queue


def team_main(charmanders: int, bulbasaurs: int, squirtles: int, missingno: int) -> bool:
    """ Returns True if the total number of pokemons provided
    are less than or equal the allocated limit, and False otherwise.
    """
    limit = 6
    total_no__pokemon = charmanders + bulbasaurs + squirtles + missingno
    if charmanders >= 0 and bulbasaurs >= 0 and squirtles >= 0 and (missingno == 0 or missingno == 1) and total_no__pokemon <= limit:
        return True
    else:
        return False


class PokeTeam(Charmander, Bulbasaur, Squirtle, MissingNo):

    def __init__(self, name) -> None:
        """ Initialises the Name and team of the player
        """
        self.name = name
        self.team = None
        self.battle_mode = None

    def __assign_team(self, charm: int, bulb: int, squir: int, missingno: int, criterion: str) -> None:
        """ Sets formation of a team to a stack form.
        Creates the ADT in accordance with formation and adds the units to it appropriately.
        Binds the name and team variables.
        """
        # battle_mode 0 - Stack
        # battle_mode 1 - Circular Queue
        # battle_mode 2 - Stack
        if self.battle_mode != 0 and self.battle_mode != 1 and self.battle_mode != 2:
            raise ValueError("formation must be either 0 or 1 or 2")

        # Formation 0 - Stack:
        if self.battle_mode == 0:
            # Creates a stack of appropriate size
            length = charm + bulb + squir + missingno
            self.team = ArrayStack(length)

            # Push Pokemons into the player's stack in FILO..first in last out order
            for i in range(missingno):
                m = MissingNo()
                self.team.push(m)
            for i in range(squir):
                s = Squirtle()
                self.team.push(s)
            for i in range(bulb):
                b = Bulbasaur()
                self.team.push(b)
            for i in range(charm):
                c = Charmander()
                self.team.push(c)

        # Formation 1 - Circular Queue:
        if self.battle_mode == 1:
            length = charm + bulb + squir + missingno
            self.team = CircularQueue(length)
            for i in range(charm):
                c = Charmander()
                self.team.append(c)
            for i in range(bulb):
                b = Bulbasaur()
                self.team.append(b)
            for i in range(squir):
                s = Squirtle()
                self.team.append(s)
            for i in range(missingno):
                m = MissingNo()
                self.team.append(m)

        """ Worst case is O(n), best case is O(1)
        """
        # Formation 2 - Stack Queue:
        if self.battle_mode == 2:
            length = charm + bulb + squir + missingno
            self.team = ArrayStack(length)

            criterion = criterion.upper()
            if criterion == "HP":
                for i in range(missingno):
                    m = MissingNo()
                    self.team.push(m)
                for i in range(charm):
                    c = Charmander()
                    self.team.push(c)
                for i in range(squir):
                    s = Squirtle()
                    self.team.push(s)
                for i in range(bulb):
                    b = Bulbasaur()
                    self.team.push(b)

            elif criterion == "ATTACK":
                for i in range(missingno):
                    m = MissingNo()
                    self.team.push(m)
                for i in range(squir):
                    s = Squirtle()
                    self.team.push(s)
                for i in range(bulb):
                    b = Bulbasaur()
                    self.team.push(b)
                for i in range(charm):
                    c = Charmander()
                    self.team.push(c)

            elif criterion == "SPEED":
                for i in range(missingno):
                    m = MissingNo()
                    self.team.push(m)
                for i in range(squir):
                    s = Squirtle()
                    self.team.push(s)
                for i in range(bulb):
                    b = Bulbasaur()
                    self.team.push(b)
                for i in range(charm):
                    c = Charmander()
                    self.team.push(c)

            elif criterion == "LVL":
                for i in range(missingno):
                    m = MissingNo()
                    self.team.push(m)
                for i in range(squir):
                    s = Squirtle()
                    self.team.push(s)
                for i in range(bulb):
                    b = Bulbasaur()
                    self.team.push(b)
                for i in range(charm):
                    c = Charmander()
                    self.team.push(c)

            elif criterion == "DEFENCE":
                for i in range(missingno):
                    m = MissingNo()
                    self.team.push(m)
                for i in range(charm):
                    c = Charmander()
                    self.team.push(c)
                for i in range(bulb):
                    b = Bulbasaur()
                    self.team.push(b)
                for i in range(squir):
                    s = Squirtle()
                    self.team.push(s)

    def choose_team(self, battle_mode: int, criterion: str) -> None:
        """ Reads user input of integers, c, b, s, m(if exist) then calls:
        __correct_team_given(c, b, s, m(if exists)) and if this returns True:
        __assign_team(name, c, b, s, m(if exists))
        Otherwise player is repeatedly asked to provide the input again, until valid.
        """
        self.battle_mode = battle_mode
        flag = False
        while not flag:
            # User Input
            prompt = str(input(
                "Player " + self.name + ", Choose your team as C B S M  where \n C is the number of Charmanders, " +
                "\n B is the number of Bulbasaurs, \n S is the number of Squirtles, " +
                "\n M is the number of MissingNo, \n"))

            # Separate each integer in String
            sac = prompt.split(" ")

            # Convert to int
            c = int(sac[0])
            if type(c) is not int:
                raise ValueError("must be an integer")
            if c < 0:
                raise ValueError("must be positive")

            # Convert to int
            b = int(sac[1])
            if type(b) is not int:
                raise ValueError("must be an integer")
            if b < 0:
                raise ValueError("must be positive")

            # Convert to int
            s = int(sac[2])
            if type(s) is not int:
                raise ValueError("must be an integer")
            if s < 0:
                raise ValueError("must be positive")

            if len(sac) > 3:
                # Convert to int
                m = int(sac[3])
                if type(m) is not int:
                    raise ValueError("must be an integer")
                if m < 0:
                    raise ValueError("must be positive")
            else:
                m = 0

            # If correct team given, call __correct_team_given(c, b, s)
            if team_main(c, b, s, m) is True:
                flag = True
                self.__assign_team(c, b, s, m, criterion)
                output = self.__str__()
                print(output)

    def __str__(self) -> str:
        """ Returns a string containing the information of each PokeTeam element in team
        Example, if an PokeTeam is in stack formation with 1 Charmander on top of 1 Bulbasaur, both with health 1 and level 2,
        then str(PokeTeam) should return "Charmander's health = 1 and level = 2,Bulbasaur's health = 1 and level = 2"
        """
        size = self.team.length
        temp = ArrayStack(self.team.length)
        output = ""
        for i in range(self.team.length):
            pokemon = None
            if self.battle_mode == 0:
                pokemon = self.team.pop()
                temp.push(pokemon)
            elif self.battle_mode == 1:
                pokemon = self.team.serve()
                self.team.append(pokemon)
            elif self.battle_mode == 2:
                pokemon = self.team.pop()
                temp.push(pokemon)

            if i < size - 1:
                output += (str(pokemon) + ", ")
            else:
                output += (str(pokemon))
        if self.battle_mode == 0:
            for i in range(temp.length):
                self.team.push(temp.pop())
        elif self.battle_mode == 2:
            for i in range(temp.length):
                self.team.push(temp.pop())

        return output
