import unittest

from tester_base import TesterBase, captured_output


class TestBattle(TesterBase):
    def test_normalBattle_example(self):
        from battle import Battle

        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1\n1 1 1") as (inp, out, err):
                # Here, Ash gets 1 Charmander,1 Bulbasaur and 1 Squirtle and Misty also gets one of each Pokemon like
                # Ash.
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Ash"
        except AssertionError:
            self.verificationErrors.append(f"Ash should win: {result}.")

    def test_rotatingBattle_example(self):
        from battle import Battle

        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 5 1\n5 1 0") as (inp, out, err):
                # Here, Ash gets 5 Bulbasaurs and 1 Squirtle , and Misty gets 5 Charmanders and 1 Bulbasaur.
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Misty"
        except AssertionError:
            self.verificationErrors.append(f"Misty should win: {result}.")

    def test_optimised_battle_1(self):
        from battle import Battle

        try:
            newBattle = Battle("Grim", "Cindy")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 1 1\n2 1 1") as (inp, out, err):
                result = newBattle.optimised_mode_battle("defence", "speed")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Cindy"
        except AssertionError:
            self.verificationErrors.append(f"Cindy should win: {result}.")
        try:
            assert str(newBattle.team2) == "Squirtle's HP = 3 and level = 2"
        except AssertionError:
            self.verificationErrors.append(f"Team 2 is not correct after battle: {str(newBattle.team2)}")

        ### DRAW CASE

    def test_optiminsed_battle_2(self):
        from battle import Battle

        try:
            test = Battle("Azusa", "Nakano")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("1 1 1\n1 1 1") as (inp, out, err):
                result = test.optimised_mode_battle("attack", "attack")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Draw"
        except AssertionError:
            self.verificationErrors.append(f"It should end in a draw: {result}.")
        try:
            assert str(test.team1) == ""
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(test.team1)}")
