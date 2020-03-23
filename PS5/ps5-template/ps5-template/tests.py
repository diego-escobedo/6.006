import unittest
from pocketcube     import check as cube_check
from pocketcube     import solve

tests = (
    (
        '004320325411103253442155',
        ((2, 1), (0, -1)),
    ),
    (
        '004221015341103233442555',
        ((1, -1), (0, 1), (1, 1), (0, -1)),
    ),
    (
        '012435303042141103455225',
        ((2, 1), (0, 1), (2, 1), (2, 1), (1, -1), (0, 1)),
    ),
    (
        '145043234510112203425305',
        ((1, -1), (0, -1), (2, -1), (0, 1), (1, -1), (0, -1), (2, 1), (1, -1)),
    ),
    (
        '005123245231412013405435',
        ((0, -1), (1, 1), (2, -1), (0, 1), (2, 1), (1, 1), (2, 1), (2, 1), (1, 1), (1, 1)),
    ),
)

def check(test):
    config, staff_sol = test
    student_sol = solve(config)
    if len(staff_sol) != len(student_sol):
        return False
    return cube_check(config, student_sol)

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
