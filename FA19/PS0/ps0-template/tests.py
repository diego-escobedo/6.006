import unittest
from min_mod_tuple import min_mod_tuple

tests = (
    (
        (
            [66, 21, 327, 349, 475],
            2500,
        ),
        (2, 4),
    ),
    (
        (
            [83, 77, 81, 484, 316, 202, 196, 614],
            6400,
        ),
        (0, 2),
    ),
    (
        (
            [368, 1073, 639, 976, 31, 609, 926, 603, 384, 1073, 320],
            12100,
        ),
        (1, 5),
    ),
    (
        (
            [635, 1408, 605, 1413, 1383, 1705, 1454, 821, 904, 1489, 1268, 1696, 1207, 1525, 507, 1678, 700, 557],
            32400,
        ),
        (1, 14),
    ),
    (
        (
            [2087, 521, 845, 1800, 323, 1261, 452, 1277, 2415, 329, 1448, 1035, 1387, 954, 364, 545, 850, 55, 164, 1656, 484, 2388, 761, 1770, 712],
            62500,
        ),
        (1, 3),
    ),
)

def check(test):
    args, staff_sol = test
    A, k = args
    student_sol = min_mod_tuple(A, k)
    i1, j1 = staff_sol
    i2, j2 = student_sol
    v1 = (A[i1] * A[j1]) % k
    v2 = (A[i2] * A[j2]) % k
    return (v1 == v2) and (0 <= i2 < j2 < len(A))

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
