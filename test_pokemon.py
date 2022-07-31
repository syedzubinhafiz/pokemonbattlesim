import unittest

from tester_base import TesterBase


class PokemonTester(TesterBase):

    def test_bulbasaur_string(self):
        from pokemon import Bulbasaur
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            s = str(b)
            if s != "Bulbasaur's HP = 9 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_squirtle_string(self):
        from pokemon import Squirtle
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            s = str(s)
            if s != "Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PokemonTester)
    unittest.TextTestRunner(verbosity=0).run(suite)