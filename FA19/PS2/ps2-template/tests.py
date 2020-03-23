import unittest
from get_damages    import get_damages

tests = (
    (
        [5, 0, 19, 20, 19],
        [2, 1, 1, 2, 1],
    ),
    (
        [81, 13, 68, 6, 51, 85, 62, 58, 59, 39],
        [9, 2, 7, 1, 2, 5, 4, 2, 2, 1],
    ),
    (
        [278, 249, 16, 331, 270, 368, 330, 364, 115, 42, 208, 65, 286, 262, 32, 359, 214, 346, 374, 241],
        [12, 9, 1, 12, 9, 14, 10, 12, 4, 2, 3, 2, 5, 4, 1, 4, 1, 2, 2, 1],
    ),
    (
        [193, 546, 193, 61, 419, 374, 742, 491, 755, 804, 236, 661, 758, 445, 731, 37, 529, 19, 254, 462, 106, 558, 876, 895, 749, 739, 481, 12, 296, 516],
        [6, 18, 6, 4, 9, 8, 18, 11, 18, 19, 5, 13, 16, 7, 12, 3, 9, 2, 3, 4, 2, 5, 7, 7, 6, 5, 3, 1, 1, 1],
    ),
    (
        [1153, 1365, 403, 142, 1156, 800, 2380, 262, 1365, 1804, 2498, 629, 1760, 1084, 1788, 1887, 375, 1832, 891, 108, 332, 553, 469, 1121, 1806, 1038, 1493, 1024, 2217, 2109, 1696, 373, 1873, 1756, 330, 301, 310, 361, 264, 1953, 1114, 143, 1958, 1181, 1848, 852, 605, 111, 312, 1996],
        [28, 30, 15, 3, 26, 18, 43, 4, 25, 30, 40, 16, 27, 20, 26, 30, 12, 26, 16, 1, 8, 11, 10, 15, 19, 13, 15, 12, 22, 21, 14, 9, 15, 13, 7, 4, 4, 5, 3, 9, 6, 2, 7, 5, 5, 4, 3, 1, 1, 1],
    ),
)

def check(test):
    H, staff_sol = test
    student_sol = get_damages(H)
    n1 = len(staff_sol)
    n2 = len(student_sol)
    if n1 != n2: return False
    for i in range(n1):
        if staff_sol[i] != student_sol[i]: return False
    return True

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
