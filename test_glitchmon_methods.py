import unittest
from tester_base import TesterBase, captured_output

class TestMissingNo(TesterBase):
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
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMissingNo)
    unittest.TextTestRunner(verbosity=0).run(suite)