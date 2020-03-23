import unittest
from detect_copy        import detect_copy

tests = (
    (
        (
            '006.06.606.006.60.6',
            '6.006',
        ),
        True,
    ),
    (
        (
            'Are you cheating on this code submission?',
            'yes i am',
        ),
        False,
    ),
    (
        (
            'Are you cheating on this code submission?',
            'u cheat',
        ),
        True,
    ),
    (
        (
            'fmiwqpudlxryqsrkpdlueabjpftmlxalvunmimhddtkftjkscsjxtfckkpyd',
            'udlxryqsrkpd',
        ),
        True,
    ),
    (
        (
            'jordyufyyksxckxkvusdpktgmlqoxboijnpwrmpifrryhjemkisapsfwfecdduoptbmvmhhhodippsgarlryuivvmr',
            'isapsfwfeddduoptbm',
        ),
        False,
    ),
)

def check(test):
    args, staff_sol = test
    student_sol = detect_copy(*args)
    return staff_sol == student_sol

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
