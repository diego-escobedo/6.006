import unittest
from build_wall         import build_wall

# Change to False to supress output of placement
verbose = True

tests = (
    (
        (
            '.....',
            '.....',
            '.....',
            '..#..',
            '###.#',
        ),
        [(0, 0, 'D'), (0, 2, 'R'), (0, 3, 'R'), (1, 0, 'R'), (1, 1, 'R'), (2, 2, 'R'), (3, 0, 'R'), (3, 1, 'R'), (3, 3, 'D'), (4, 2, 'D')],
    ),
    (
        (
            '..........',
            '..........',
            '..........',
            '.....#.##.',
            '..#..####.',
        ),
        [(0, 0, 'D'), (0, 2, 'D'), (0, 4, 'R'), (1, 0, 'R'), (1, 1, 'R'), (1, 2, '1'), (1, 3, 'R'), (2, 2, 'R'), (3, 0, 'D'), (3, 3, 'R'), (3, 4, 'R'), (4, 0, 'R'), (4, 1, 'R'), (4, 2, 'R'), (6, 0, 'D'), (6, 2, 'R'), (6, 3, '1'), (7, 0, 'D'), (8, 0, 'D'), (8, 2, 'R'), (9, 0, 'D'), (9, 3, 'D')],
    ),
    (
        (
            '...............',
            '...............',
            '............#..',
            '............#.#',
            '#.#########.###',
        ),
        [(0, 0, 'D'), (0, 2, 'R'), (0, 3, '1'), (1, 0, 'R'), (1, 1, 'R'), (1, 3, 'D'), (2, 2, 'R'), (2, 3, 'R'), (3, 0, 'D'), (4, 0, 'D'), (4, 2, 'R'), (4, 3, 'R'), (5, 0, 'D'), (6, 0, 'D'), (6, 2, 'R'), (6, 3, 'R'), (7, 0, 'D'), (8, 0, 'D'), (8, 2, 'D'), (9, 0, 'R'), (9, 1, 'D'), (9, 3, 'R'), (10, 1, 'D'), (11, 0, 'R'), (11, 1, 'D'), (11, 3, 'D'), (12, 1, 'R'), (13, 0, 'R'), (13, 2, 'D'), (14, 1, 'D')],
    ),
    (
        (
            '....................',
            '..........#.........',
            '.........##.........',
            '#.###..####.....##..',
            '#.###..############.',
        ),
        [(0, 0, 'R'), (0, 1, 'R'), (0, 2, '1'), (1, 2, 'R'), (1, 3, 'D'), (2, 0, 'R'), (2, 1, 'R'), (3, 2, 'R'), (4, 0, 'R'), (4, 1, 'R'), (5, 2, 'D'), (5, 4, 'R'), (6, 0, 'R'), (6, 1, 'R'), (6, 2, 'D'), (7, 2, 'R'), (8, 0, 'D'), (9, 0, 'D'), (10, 0, 'R'), (11, 1, 'R'), (11, 2, 'D'), (12, 0, 'R'), (12, 2, 'D'), (13, 1, 'R'), (13, 2, 'D'), (14, 0, 'R'), (14, 2, 'D'), (15, 1, 'R'), (15, 2, 'D'), (16, 0, 'R'), (16, 2, 'R'), (17, 1, 'R'), (18, 0, 'R'), (18, 2, 'D'), (19, 1, 'D'), (19, 3, 'D')],
    ),
    (
        (
            '.........................',
            '.........................',
            '....................#....',
            '...........#....#...##..#',
            '..#.#.#.#.####.##.#.#####',
        ),
        [(0, 0, 'D'), (0, 2, 'D'), (0, 4, 'R'), (1, 0, 'D'), (1, 2, 'D'), (2, 0, 'D'), (2, 2, 'D'), (3, 0, '1'), (3, 1, 'R'), (3, 2, '1'), (3, 3, 'D'), (4, 0, 'R'), (4, 2, 'D'), (5, 1, 'R'), (5, 2, '1'), (5, 3, 'R'), (5, 4, '1'), (6, 0, 'R'), (6, 2, 'R'), (7, 1, 'R'), (7, 3, 'R'), (7, 4, '1'), (8, 0, 'R'), (8, 2, 'R'), (9, 1, 'R'), (9, 3, 'D'), (10, 0, 'R'), (10, 2, 'D'), (11, 1, 'D'), (12, 0, 'R'), (12, 1, 'D'), (12, 3, 'R'), (13, 1, 'D'), (14, 0, 'R'), (14, 1, 'D'), (14, 3, 'D'), (15, 1, 'R'), (15, 2, 'D'), (16, 0, 'R'), (16, 2, 'R'), (17, 1, 'R'), (17, 3, 'D'), (18, 0, 'R'), (18, 2, 'D'), (19, 1, 'D'), (19, 3, 'D'), (20, 0, 'R'), (20, 1, 'R'), (21, 2, 'R'), (22, 0, 'D'), (22, 3, 'R'), (23, 0, 'D'), (23, 2, 'R'), (24, 0, 'D')],
    ),
)

def check(test):
    B, staff_sol = test
    P = build_wall(B)
    sol_count = 0
    for i, j, t in staff_sol:
        if t == '1':
            sol_count += 1
    D = [[c for c in row] for row in B]
    n = len(B[0])
    count = 0
    for i, j, t in P:
        if (not (0 <= i < n)) or (not (0 <= j < 5)):
            raise Exception('(%s, %s) is out of range' % (i, j))
        if D[j][i] != '.':
            raise Exception('(%s, %s) already covered' % (i, j))
        if t == '1':
            D[j][i] = 'O'
            count += 1
        elif t == 'D':
            if (not (0 <= j + 1 < 5)):
                raise Exception('(%s, %s) is out of range' % (i, j + 1))
            if D[j + 1][i] != '.':
                raise Exception('(%s, %s) already covered' % (i, j + 1))
            D[j][i], D[j + 1][i] = '|', '|'
        elif t == 'R':
            if (not (0 <= i + 1 < n)):
                raise Exception('(%s, %s) is out of range' % (i + 1, j))
            if D[j][i + 1] != '.':
                raise Exception('(%s, %s) already covered' % (i + 1, j ))
            D[j][i], D[j][i + 1] = '-', '-'
    for i in range(n):
        for j in range(5):
            if D[j][i] == '.':
                raise Exception('(%s, %s) not covered in placement' % (i, j))
    if verbose:
        print('# of 1s: %s' % count)
        print('\n'.join([''.join(row) for row in D]))
    return count == sol_count

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
