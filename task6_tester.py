import unittest

from tester_base import TesterBase, captured_output

class TestTask4(TesterBase):

    def test_limit(self):
        from poke_team import PokeTeam
        try:
            team = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("0 0 0 2\n1 1 1 1") as (inp, out, err):
                # 0 0 0 2 should fail. Too many missingos.
                # So 1 1 1 1 should be the correct team.
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()
        try:
            assert str(team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    ### ADD TESTS HERE
    def test_increase_hp(self):
        from pokemon import MissingNo
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"MissingNo could not be instantiated: {str(e)}.")
            return
        try:
            m.increase_hp(3)
            s = str(m)
            if s != "MissingNo's HP = 11 and level = 1":
                self.verificationErrors.append(f"Increase HP method did not increase HP correctly: {s}")
        except Exception as e:
            self.verificationErrors.append(f"Increase HP method failed. {e}")

    def test_super_power(self):
        from pokemon import MissingNo
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f"MissingNo could not be instantiated: {str(e)}.")
            return
        try:
            m.superpower()
            s = str(m)
            if s == "MissingNo's HP = 9 and level = 1":
                pass
            elif s == "MissingNo's HP = 9 and level = 2":
                pass
            elif s == "MissingNo's HP = 10 and level = 2":
                pass
            else:
                self.verificationErrors.append(f"SuperPower method is not implemented correctly: {s}")
        except Exception as e:
            self.verificationErrors.append(f"SuperPower method failed. {e}")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask4)
    unittest.TextTestRunner(verbosity=0).run(suite)