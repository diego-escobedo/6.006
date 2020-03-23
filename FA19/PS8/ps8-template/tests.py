import unittest
from count_paths    import count_paths
from sys            import setrecursionlimit

tests = (
    (
        [
            ['x', 'x', 't', 'x', 'm'],
            ['x', 'x', 'x', 'x', 'x'],
            ['m', 'm', 'x', 'x', 'm'],
            ['x', 'x', 't', 'm', 't'],
            ['x', 't', 'x', 'm', 'x'],
        ],
        1,
    ),
    (
        [
            ['x', 'm', 'x', 'x', 't', 'm', 'm'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'm'],
            ['x', 'm', 'x', 't', 'm', 't', 't'],
            ['m', 'x', 'x', 'x', 'x', 'x', 'm'],
            ['m', 't', 'm', 'm', 't', 'x', 'x'],
            ['m', 'x', 'm', 'x', 'x', 'x', 'm'],
            ['x', 'x', 'x', 'm', 't', 'm', 'x'],
        ],
        10,
    ),
    (
        [
            ['x', 'm', 't', 'm', 'x', 'x', 'x', 't', 'm', 'm'],
            ['x', 'm', 'm', 'x', 'x', 'm', 'x', 'x', 'x', 't'],
            ['x', 'm', 'm', 't', 'x', 't', 'x', 'x', 'x', 'x'],
            ['m', 'm', 'm', 'x', 'x', 'm', 'x', 'x', 'x', 'm'],
            ['x', 'm', 'm', 'x', 'x', 't', 'x', 'm', 'x', 'x'],
            ['x', 'm', 'x', 'm', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['m', 'm', 'm', 'm', 'x', 'm', 'x', 'x', 'x', 't'],
            ['m', 'x', 't', 'm', 'x', 'm', 'x', 'x', 'x', 't'],
            ['x', 'x', 'x', 'm', 't', 'x', 'm', 'x', 'x', 'x'],
            ['x', 'm', 'x', 'm', 'x', 'x', 'x', 'x', 'm', 'x'],
        ],
        13,
    ),
    (
        [
            ['x', 'x', 'm', 'm', 't', 'x', 'm', 'm', 'x', 'x', 'x', 'm', 'm', 'x', 'm'],
            ['m', 'x', 'x', 'm', 't', 'm', 'x', 't', 't', 'm', 'x', 't', 'x', 'm', 'x'],
            ['m', 'm', 'm', 'm', 'm', 'x', 'x', 'm', 'm', 'x', 'x', 'm', 'x', 't', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'm', 'x', 'm', 'x', 'm', 'x', 'x', 'x', 'm'],
            ['x', 'm', 'm', 'x', 'x', 'x', 'm', 'x', 'm', 'x', 'm', 'm', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 't', 'm', 'm', 'x', 'x', 'm', 'x', 'x', 'm', 'm', 'x'],
            ['x', 't', 'x', 'x', 'x', 'm', 'x', 'x', 'x', 'x', 'm', 'x', 'x', 't', 'x'],
            ['x', 'x', 'x', 'x', 'x', 't', 't', 'x', 'm', 'x', 'x', 'm', 'x', 'm', 'x'],
            ['x', 'x', 'm', 'x', 'm', 'x', 'x', 'x', 'x', 'm', 'x', 't', 'x', 'x', 'x'],
            ['m', 'x', 'x', 'm', 'm', 'x', 'm', 'x', 'x', 'x', 'x', 'x', 'm', 'x', 'm'],
            ['x', 'm', 'x', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'x', 'x', 'x', 'x', 'x'],
            ['m', 'm', 'm', 'x', 'x', 'm', 'm', 'x', 'x', 'm', 'm', 'x', 'x', 'x', 'm'],
            ['m', 'x', 'x', 'x', 'x', 't', 'm', 'm', 'x', 'x', 'm', 'x', 'm', 'x', 'x'],
            ['m', 'x', 'x', 'x', 'm', 'x', 'm', 'm', 'm', 'm', 'm', 'm', 't', 'x', 'm'],
            ['x', 'x', 'x', 'x', 'm', 'x', 'm', 't', 'm', 'x', 'm', 'x', 'x', 'x', 'x'],
        ],
        120,
    ),
    (
        [
            ['x', 'm', 'x', 'm', 'x', 'm', 'm', 'm', 'x', 'm', 'm', 'm', 'm', 'm', 'x', 'x', 'm', 'x', 'x', 'x'],
            ['m', 'm', 'x', 'm', 'x', 'm', 'x', 'x', 'x', 'm', 'x', 'x', 'm', 'x', 'x', 'm', 'm', 'x', 'm', 'x'],
            ['x', 'm', 'm', 'm', 'x', 'm', 'x', 'm', 'm', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'm', 'x', 'x', 'x'],
            ['x', 'm', 'm', 't', 'x', 'x', 'x', 'x', 'm', 'm', 'x', 'm', 'x', 'm', 'x', 'm', 'm', 'm', 'x', 'm'],
            ['m', 'm', 'x', 'm', 'm', 't', 'x', 'm', 'm', 'x', 'm', 'm', 'x', 'm', 'x', 'm', 'x', 't', 't', 'm'],
            ['x', 'x', 't', 'x', 'm', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'm', 'm', 'x', 'x', 'x', 'x', 'm', 'x'],
            ['m', 'm', 'x', 'm', 'x', 'x', 'x', 'm', 'x', 'm', 'x', 'm', 'x', 'x', 'm', 't', 'x', 'm', 'x', 'm'],
            ['m', 'x', 'm', 'x', 'x', 'm', 'x', 'x', 'x', 'x', 'm', 'x', 'x', 'x', 'm', 'x', 'x', 'x', 'x', 'x'],
            ['m', 'x', 'm', 'x', 'm', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'm', 'x', 'x', 'x', 'x', 'x', 'm', 'x'],
            ['m', 'x', 'x', 'm', 'm', 'x', 'x', 'x', 'x', 'x', 'm', 't', 'x', 'm', 't', 'm', 't', 'm', 'x', 'x'],
            ['x', 'x', 'm', 'm', 'm', 'm', 'x', 'x', 'x', 'x', 'm', 'x', 'x', 'x', 'm', 'x', 'm', 'x', 'x', 'x'],
            ['m', 'x', 'm', 'x', 'x', 'm', 'm', 'm', 'x', 'm', 'm', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 't', 'x'],
            ['x', 'x', 'm', 'x', 'x', 'x', 'x', 'x', 't', 'm', 'x', 'm', 't', 'm', 'm', 'm', 'x', 'm', 'm', 'x'],
            ['m', 'm', 'm', 'x', 'm', 'm', 'm', 'x', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'm', 't', 'x', 'x'],
            ['m', 'x', 'm', 'm', 'x', 'x', 'm', 'x', 'x', 'x', 'm', 'm', 'm', 'm', 'x', 'm', 'x', 'x', 'x', 'm'],
            ['x', 'x', 'm', 'x', 'm', 'x', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 't', 'x', 'm', 't', 'x', 'x', 'x'],
            ['x', 'm', 'x', 'x', 'x', 'x', 't', 't', 'x', 'm', 'x', 'x', 'm', 'x', 'x', 'x', 'm', 'x', 'm', 'x'],
            ['x', 'x', 'x', 't', 'm', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'm', 'x', 'x', 'x', 'x', 'x', 'x', 'm'],
            ['x', 'x', 'm', 'x', 'x', 'x', 'm', 'x', 'm', 'm', 'x', 'x', 'm', 'm', 't', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'm', 'x', 'm', 'x', 'x', 'm', 'x', 'x', 'm', 'x', 'x', 'm', 'm', 'x', 'x', 'x', 'm', 'x'],
        ],
        64,
    ),
)

def check(test):
    F, staff_sol = test
    student_sol = count_paths(F)
    return student_sol == staff_sol

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
