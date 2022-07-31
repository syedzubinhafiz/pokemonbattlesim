from array_sorted_list import ArraySortedList
from poke_team import PokeTeam
from sorted_list import ListItem
from stack_adt import ArrayStack
from pokemon import PokemonBase

__author__ = "Mohamed Azhan"
__editor__ = "Syed Zubin Hafiz, Justin Chuah, Chua Jun Jie"
__last_modified__ = "30.04.2022"


class Battle:
    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        """Initializes necessary objects for battle"""
        self.trainer_one_name = trainer_one_name
        self.trainer_two_name = trainer_two_name
        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)
        self.battle_mode = None

    def set_mode_battle(self) -> str:
        """
        Sets the battle mode to be 0
        Creates both teams and calls the do_battle method to start the fight
        Worst case time complexity would be O(1)+O(n) or O(n) since the do_battle's time complexity takes
        precedence over the if-statements' complexities
        Best case time-complexity would be O(n)+O(1) or O(n)
        """
        self.battle_mode = 0
        self.team1.choose_team(self.battle_mode, None)
        self.team2.choose_team(self.battle_mode, None)
        self.do_battle()
        if self.team1.team.is_empty() and self.team2.team.is_empty():
            # if both the teams are empty, match results in a draw
            return "Draw"
        if self.team1.team.is_empty():
            # if team 1 is empty, this means team 1 lost all Pokemon and so team 2 won
            return self.team2.name
        if self.team2.team.is_empty():
            # if team 2 is empty, this means team 2 lost all Pokemon and so team 1 won
            return self.team1.name

    def do_battle(self):
        """
        In the worst case,time complexity would be O(n); the while loop will run multiple teams when
        both teams have a total of 6 pokemons and the length of the array doesn't decrement every round as two pokemons
        may fight multiple rounds before one of them faints. In the best case scenario, time complexity would be O(n)
        when the  battle will be only 1v1 where each team has just one player to start with and one of them faints after
        just one round
        """
        turn = 0
        while not self.team1.team.is_empty() and not self.team2.team.is_empty():
            turn += 1
            print("-------------------------turn %d-------------------------" % turn)
            print("team 1 has %d pokemon remaining!" % len(self.team1.team))
            print("team 2 has %d pokemon remaining!" % len(self.team2.team))
            #Take out the pokemon's at the top of the stack to make them fight
            pokemonOne = self.team1.team.peek()
            pokemonTwo = self.team2.team.peek()
            print("pokemon 1: %s" % str(pokemonOne))
            print("pokemon 2: %s" % str(pokemonTwo))
            #if pokemon one has a greater attack speed than that of pokemon two, pokemon one attacks first
            if pokemonOne.get_speed() > pokemonTwo.get_speed():
                print("pokemon 1 goes first!")
                pokemonTwo.defend(pokemonOne)
            #if pokemon two has not been knocked out by that attack,they attack next and pokemon one defends
                if not pokemonTwo.is_fainted():
                    print("pokemon 2 goes next!")
                    pokemonOne.defend(pokemonTwo)
            #alternatively if pokemon one has a slower attack speed than that of pokemon two, pokemon two attacks first and pokemon one defends
            elif pokemonOne.get_speed() < pokemonTwo.get_speed():
                print("pokemon 2 goes first!")
                pokemonOne.defend(pokemonTwo)
                #if pokemon one hasn't been knocked out yet, pokemon one attacks and pokemon two defends
                if not pokemonOne.is_fainted():
                    print("pokemon 1 goes next!")
                    pokemonTwo.defend(pokemonOne)
            else:
                #Another alternate scenario would be, both of them attacking and defending simultaneously given they have identical attack speed
                print("both pokemon attack simultaneously!")
                pokemonOne.defend(pokemonTwo)
                pokemonTwo.defend(pokemonOne)
            print("pokemon 1 has %d hp remaining!" % pokemonOne.get_hp())
            print("pokemon 2 has %d hp remaining!" % pokemonTwo.get_hp())

            #if pokemon two faints he gets popped out of the stack and pokemon one levels up
            if pokemonTwo.is_fainted():
                print("pokemon 2 fainted!")
                pokemonOne.level_up()
                self.team2.team.pop()
                # if pokemon one faints he gets popped out of the stack and pokemon two levels up
            elif pokemonOne.is_fainted():
                print("pokemon 1 fainted!")
                pokemonTwo.level_up()
                self.team1.team.pop()
            else:
                #if neither gets knocked out, we attrition occurs so we deduct 1 hp from each player
                print("neither pokemon fainted, so attrition occurs!")
                pokemonOne.set_hp(pokemonOne.get_hp() - 1)
                pokemonTwo.set_hp(pokemonTwo.get_hp() - 1)
                print("pokemon 1 has %d hp remaining!" % pokemonOne.get_hp())
                print("pokemon 2 has %d hp remaining!" % pokemonTwo.get_hp())

                #same process occurs here as before attrition
                if pokemonTwo.is_fainted():
                    print("pokemon 2 fainted!")
                    pokemonOne.level_up()
                    self.team2.team.pop()
                elif pokemonOne.is_fainted():
                    print("pokemon 1 fainted!")
                    pokemonTwo.level_up()
                    self.team1.team.pop()
                elif pokemonOne.is_fainted() and pokemonTwo.is_fainted():
                    self.team1.team.pop()
                    self.team2.team.pop()
                    print("Both the pokemons fainted!")

    def rotating_mode_battle(self):
        """
        Sets the battle mode to be 1
        Creates both teams and calls the do_battle method to start the fight
        Worst case time complexity would be O(1)+O(n) or O(n) since the do_battle's time complexity takes
        precedence over the if-statements' complexities
        Best case time-complexity would be O(n)+O(1) or O(n)
        """
        self.battle_mode = 1
        self.team1.choose_team(self.battle_mode, None)
        self.team2.choose_team(self.battle_mode, None)
        self.do_rotating_battle()
        if self.team1.team.is_empty() and self.team2.team.is_empty():
            # if both the teams are empty, match results in a draw
            return "Draw"
        if self.team1.team.is_empty():
            # if team 1 is empty, this means team 1 lost all Pokemon and so team 2 won
            return self.team2.name
        if self.team2.team.is_empty():
            # if team 2 is empty, this means team 2 lost all Pokemon and so team 1 won
            return self.team1.name

    def do_rotating_battle(self):
        """
        In the worst case,time complexity would be O(n); the while loop will run multiple teams when
        both teams have a total of 6 pokemons and the length of the array doesn't decrement every round as two
        pokemons may fight multiple rounds before one of them faints.In the best case scenario, time complexity would be O(n)
        when the  battle will be only 1v1 where each team has just one player to start with and one of them faints after
        just one round
        """
        turn = 0
        while not self.team1.team.is_empty() and not self.team2.team.is_empty():
            turn += 1
            print("-------------------------turn %d-------------------------" % turn)
            print("team 1 has %d pokemon remaining!" % len(self.team1.team))
            print("team 2 has %d pokemon remaining!" % len(self.team2.team))
            #Take out two pokemons from each ta=eam to make them fight
            pokemonOne = self.team1.team.serve()
            pokemonTwo = self.team2.team.serve()
            print("pokemon 1: %s" % str(pokemonOne))
            print("pokemon 2: %s" % str(pokemonTwo))
            #pokemon one goes first if its speed is > than that of pokemon two
            if pokemonOne.get_speed() > pokemonTwo.get_speed():
                print("pokemon 1 goes first!")
                pokemonTwo.defend(pokemonOne)
            # if pokemon one's attack doesn't knockout pokemon two, pokemon two attacks.
                if not pokemonTwo.is_fainted():
                    print("pokemon 2 goes next!")
                    pokemonOne.defend(pokemonTwo)
            #In an alternate scenario, if pokemon one has attack speed less than that of pokemon two, pokemon two attacks first
            elif pokemonOne.get_speed() < pokemonTwo.get_speed():
                print("pokemon 2 goes first!")
                pokemonOne.defend(pokemonTwo)
            #If pokemon one doesn't get knocked out by pokemon two, then pokemon one attacks while pokemon two defends
                if not pokemonOne.is_fainted():
                    print("pokemon 1 goes next!")
                    pokemonTwo.defend(pokemonOne)
            else:
            #In another scenario, if both of them have the same speed, the duo  attack and defend at the same time
                print("both pokemon attack simultaneously!")
                pokemonOne.defend(pokemonTwo)
                pokemonTwo.defend(pokemonOne)
            print("pokemon 1 has %d hp remaining!" % pokemonOne.get_hp())
            print("pokemon 2 has %d hp remaining!" % pokemonTwo.get_hp())
            #If pokemon two faints, pokemon one levels up
            if pokemonTwo.is_fainted():
                print("pokemon 2 fainted!")
                pokemonOne.level_up()
                # If pokemon one faints, pokemon two levels up
            elif pokemonOne.is_fainted():
                print("pokemon 1 fainted!")
                pokemonTwo.level_up()
            else:
                #Attrition occurs if none of them faint
                print("neither pokemon fainted, so attrition occurs!")
                # We deduct 1 hp from each pokemon
                pokemonOne.set_hp(pokemonOne.get_hp() - 1)
                pokemonTwo.set_hp(pokemonTwo.get_hp() - 1)
                print("pokemon 1 has %d hp remaining!" % pokemonOne.get_hp())
                print("pokemon 2 has %d hp remaining!" % pokemonTwo.get_hp())
                if pokemonTwo.is_fainted():
                    #now we repeat the same process before attrition to level up
                    print("pokemon 2 fainted!")
                    pokemonOne.level_up()
                elif pokemonOne.is_fainted():
                    print("pokemon 1 fainted!")
                    pokemonTwo.level_up()
                else:
                    print("move both pokemon to the back of the queue!")
            # add to back of the queue if not fainted yet
            if not pokemonTwo.is_fainted():
                self.team2.team.append(pokemonTwo)
            if not pokemonOne.is_fainted():
                self.team1.team.append(pokemonOne)

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str):
        """ Sets the battle mode to be 2
            Creates both teams and calls the do_battle method to start the fight
            Returns the team who wins by checking if the other team is empty, if both teams are empty, return Draw
            Worst case time complexity would be O(1)+O(n^2) or O(n^2) since the do_battle's time complexity takes
            precedence over the if-statements' complexities
            Best case time-complexity would be O(n)+O(1) or O(n)
        """
        self.battle_mode = 2
        self.team1.choose_team(self.battle_mode, criterion_team1)
        self.team2.choose_team(self.battle_mode, criterion_team2)
        self.do_optimised_battle(criterion_team1, criterion_team2)
        if self.team1.team.is_empty() and self.team2.team.is_empty():
            return "Draw"
        if self.team1.team.is_empty():
            return self.team2.name
        if self.team2.team.is_empty():
            return self.team1.name

    def do_optimised_battle(self, crit1: str, crit2: str):
        """ In the worst case,time complexity would be O(n^2), because it does not matter how many times the battle has run,
            the sorting part inside the do_optimised battle will be O(n^2).In the best case scenario, time complexity
            would be O(n) when the  battle will be only 1v1 where each team has just one player to start with and one
            of them faints after just one round
        """
        turn = 0
        crit1 = crit1.upper()
        crit2 = crit2.upper()
        missing_no_exist_team1 = False
        missing_no_valid_move_team1 = False
        missing_no_exist_team2 = False
        missing_no_valid_move_team2 = False
        while not self.team1.team.is_empty() and not self.team2.team.is_empty():

            """ worst = best = O(1)
            """
            turn += 1
            print("-------------------------turn %d-------------------------" % turn)
            print("team 1 has %d pokemon remaining!" % len(self.team1.team))
            print("team 2 has %d pokemon remaining!" % len(self.team2.team))

            pokemonOne = self.team1.team.peek()
            pokemonTwo = self.team2.team.peek()
            print("pokemon 1: %s" % str(pokemonOne))
            print("pokemon 2: %s" % str(pokemonTwo))
            if pokemonOne.get_speed() > pokemonTwo.get_speed():
                print("pokemon 1 goes first!")
                pokemonTwo.defend(pokemonOne)
                pokemonOne.set_battle_status(True)
                pokemonTwo.set_battle_status(True)
                if not pokemonTwo.is_fainted():
                    print("pokemon 2 goes next!")
                    pokemonOne.defend(pokemonTwo)
            elif pokemonOne.get_speed() < pokemonTwo.get_speed():
                print("pokemon 2 goes first!")
                pokemonOne.defend(pokemonTwo)
                pokemonOne.set_battle_status(True)
                pokemonTwo.set_battle_status(True)
                if not pokemonOne.is_fainted():
                    print("pokemon 1 goes next!")
                    pokemonTwo.defend(pokemonOne)
            else:
                print("both pokemon attack simultaneously!")
                pokemonOne.defend(pokemonTwo)
                pokemonTwo.defend(pokemonOne)
                pokemonOne.set_battle_status(True)
                pokemonTwo.set_battle_status(True)
            print("pokemon 1 has %d hp remaining!" % pokemonOne.get_hp())
            print("pokemon 2 has %d hp remaining!" % pokemonTwo.get_hp())
            if pokemonTwo.is_fainted() and pokemonOne.is_fainted():
                print("both pokemons fainted!")
                self.team1.team.pop()
                self.team2.team.pop()
            elif pokemonOne.is_fainted():
                print("pokemon 1 fainted!")
                pokemonTwo.level_up()
                pokemonTwo.set_battle_status(True)
                self.team1.team.pop()
            elif pokemonTwo.is_fainted():
                print("pokemon 2 fainted!")
                pokemonOne.level_up()
                pokemonOne.set_battle_status(True)
                self.team2.team.pop()
            else:
                print("neither pokemon fainted, so attrition occurs!")
                pokemonOne.set_hp(pokemonOne.get_hp() - 1)
                pokemonTwo.set_hp(pokemonTwo.get_hp() - 1)
                pokemonOne.set_battle_status(True)
                pokemonTwo.set_battle_status(True)
                print("pokemon 1 has %d hp remaining!" % pokemonOne.get_hp())
                print("pokemon 2 has %d hp remaining!" % pokemonTwo.get_hp())
                if pokemonTwo.is_fainted() and pokemonOne.is_fainted():
                    print("both pokemons fainted!")
                    self.team1.team.pop()
                    self.team2.team.pop()
                elif pokemonOne.is_fainted():
                    print("pokemon 1 fainted!")
                    pokemonTwo.level_up()
                    self.team1.team.pop()
                elif pokemonTwo.is_fainted():
                    print("pokemon 2 fainted!")
                    pokemonOne.level_up()
                    self.team2.team.pop()

            """sort team1"""
            """
            Best case for the algorithmic complexity of this section is O(1) where the length of the team is 1 and does
            not require to be sorted.
            Worst case for the algorithmic complexity of this section would be O(n) where the entire team has to be
            sorted.
    
            """
            if len(self.team1.team) > 1:
                # Retrieving counter to check validity of missing no attack
                team1counter = 0
                temp1 = ArrayStack(len(self.team1.team))
                # Checks through the current team to determine the existence of a MissingNo
                # Also checks whether the other Pokemon in the team(aside from MissingNo) have battled
                for i in range(len(self.team1.team)):
                    poke = self.team1.team.pop()
                    if poke.get_poke_type() != "NONE":
                        if poke.get_battle_status():
                            team1counter += 1
                    else:
                        missing_no_exist_team1 = True
                    temp1.push(poke)
                temp_len_holder = len(temp1)
                # If MissingNo is in team, and not all other Pokemon has battled, temporarily remove MissingNo from team
                # If MissingNo is in team, and all other Pokemon have battled, include it into the sorting algorithm
                if missing_no_exist_team1 and missing_no_valid_move_team1 == False:
                    for i in range(len(temp1)):
                        if i == 0:
                            missing_no_holder = temp1.pop()
                        else:
                            self.team1.team.push(temp1.pop())
                else:
                    for i in range(len(temp1)):
                        self.team1.team.push(temp1.pop())
                # If there exists a missing no in team, and all other Pokemon on the team have battled, allow the
                # MissingNo to enter the sorting algorithm. This will only occur once every battle.
                # Else, prepare a team that does not include the MissingNo before sorting.
                if missing_no_exist_team1 and team1counter == temp_len_holder - 1 and missing_no_valid_move_team1 == False:
                    missing_no_valid_move_team1 = True
                    self.team1.team.push(missing_no_holder)
                else:
                    temp1 = ArrayStack(len(self.team1.team))
                    for i in range(len(self.team1.team)):
                        poke = self.team1.team.pop()
                        temp1.push(poke)
                    for i in range(len(temp1)):
                        self.team1.team.push(temp1.pop())

                length_holder = len(self.team1.team)
                sortTeam1 = ArraySortedList(length_holder)

                for i in range(length_holder):
                    if crit1 == "HP":
                        poke = self.team1.team.pop()
                        sort = poke.get_hp()
                        sortTeam1.add(ListItem(poke, sort))
                    elif crit1 == "ATTACK":
                        poke = self.team1.team.pop()
                        sort = poke.get_attack_damage()
                        sortTeam1.add(ListItem(poke, sort))
                    elif crit1 == "SPEED":
                        poke = self.team1.team.pop()
                        sort = poke.get_speed()
                        sortTeam1.add(ListItem(poke, sort))
                    elif crit1 == "LVL":
                        poke = self.team1.team.pop()
                        sort = poke.get_level()
                        sortTeam1.add(ListItem(poke, sort))
                    elif crit1 == "DEFENCE":
                        poke = self.team1.team.pop()
                        sort = poke.get_defence()
                        sortTeam1.add(ListItem(poke, sort))
                # This is to re-append the MissingNo at the end of the team if it exists and is not allowed to enter
                # the sorting algorithm previously
                if missing_no_valid_move_team1 == False and missing_no_exist_team1:
                    self.team1.team.push(missing_no_holder)
                for j in range(sortTeam1.length):
                    item = sortTeam1.delete_at_index(0)
                    self.team1.team.push(item.value)

            """sort team2"""
            """
            Best case for the algorithmic complexity of this section is O(1) where the length of the team is 1 and does
            not require to be sorted.
            Worst case for the algorithmic complexity of this section would be O(n) where the entire team has to be
            sorted.
            """
            if len(self.team2.team) > 1:
                # Retrieving counter to check validity of missing no attack
                team2counter = 0
                temp2 = ArrayStack(len(self.team2.team))
                # Checks through the current team to determine the existence of a MissingNo
                # Also checks whether the other Pokemon in the team(aside from MissingNo) have battled
                for i in range(len(self.team2.team)):
                    poke = self.team2.team.pop()
                    if poke.get_poke_type() != "NONE":
                        if poke.get_battle_status():
                            team2counter += 1
                    else:
                        missing_no_exist_team2 = True
                    temp2.push(poke)
                temp_len_holder = len(temp2)
                # If MissingNo is in team, and not all other Pokemon has battled, temporarily remove MissingNo from team
                # If MissingNo is in team, and all other Pokemon have battled, include it into the sorting algorithm
                if missing_no_exist_team2 and missing_no_valid_move_team2 == False:
                    for i in range(len(temp2)):
                        if i == 0:
                            missing_no_holder2 = temp2.pop()
                        else:
                            self.team2.team.push(temp2.pop())
                else:
                    for i in range(len(temp2)):
                        self.team2.team.push(temp2.pop())
                # If there exists a missing no in team, and all other Pokemon on the team have battled, allow the
                # MissingNo to enter the sorting algorithm. This will only occur once every battle.
                # Else, prepare a team that does not include the MissingNo before sorting.
                if missing_no_exist_team2 and team2counter == temp_len_holder - 1 and missing_no_valid_move_team2 == False:
                    missing_no_valid_move_team2 = True
                    self.team2.team.push(missing_no_holder2)
                else:
                    temp2 = ArrayStack(len(self.team2.team))
                    for i in range(len(self.team2.team)):
                        poke = self.team2.team.pop()
                        temp2.push(poke)
                    for i in range(len(temp2)):
                        self.team2.team.push(temp2.pop())

                length_holder = len(self.team2.team)

                sortTeam2 = ArraySortedList(length_holder)
                for i in range(length_holder):
                    if crit2 == "HP":
                        poke = self.team2.team.pop()
                        sort = poke.get_hp()
                        sortTeam2.add(ListItem(poke, sort))
                    elif crit2 == "ATTACK":
                        poke = self.team2.team.pop()
                        sort = poke.get_attack_damage()
                        sortTeam2.add(ListItem(poke, sort))
                    elif crit2 == "SPEED":
                        poke = self.team2.team.pop()
                        sort = poke.get_speed()
                        sortTeam2.add(ListItem(poke, sort))
                    elif crit2 == "LVL":
                        poke = self.team2.team.pop()
                        sort = poke.get_level()
                        sortTeam2.add(ListItem(poke, sort))
                    elif crit2 == "DEFENCE":
                        poke = self.team2.team.pop()
                        sort = poke.get_defence()
                        sortTeam2.add(ListItem(poke, sort))

                # This is to re-append the MissingNo at the end of the team if it exists and is not allowed to enter
                # the sorting algorithm previously
                if missing_no_valid_move_team2 == False and missing_no_exist_team2:
                    self.team2.team.push(missing_no_holder2)
                for j in range(sortTeam2.length):
                    item = sortTeam2.delete_at_index(0)
                    self.team2.team.push(item.value)


"""In our implementation, this method tests the different battle modes,by changing the battle mode in the print statement below,
 using the print statements so each round can be observed.
"""

if __name__ == "__main__":
    battle = Battle("Ash", "Misty")
    print(battle.optimised_mode_battle("defence", "speed"))
    print(battle.team1)

#    test = battle.team1.team.pop()
#    test.get_hp()
#    print(battle.rotating_mode_battle())
