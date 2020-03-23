import unittest
from min_time   import min_time

tests = (
    (
        (
            [('code.cpp', 1), ('system.c', 5), ('file.bin', 5), ('program.cpp', 3), ('process.c', 4)],
            [('code.cpp', 'file.bin'), ('file.bin', 'system.c'), ('file.bin', 'process.c'), ('program.cpp', 'process.c'), ('code.cpp', 'system.c'), ('program.cpp', 'system.c')],
        ),
        11,
    ),
    (
        (
            [('design.c', 6), ('code.cpp', 2), ('program.cpp', 8), ('process.c', 2), ('file.bin', 9), ('system.c', 3), ('process.bin', 1), ('file.exe', 9), ('project.exe', 8), ('system.py', 7)],
            [('code.cpp', 'program.cpp'), ('file.bin', 'design.c'), ('file.bin', 'process.bin'), ('file.exe', 'design.c'), ('process.c', 'project.exe'), ('code.cpp', 'project.exe'), ('process.c', 'process.bin'), ('program.cpp', 'design.c'), ('system.c', 'system.py'), ('design.c', 'project.exe'), ('program.cpp', 'system.py'), ('system.c', 'project.exe'), ('file.exe', 'project.exe'), ('system.py', 'process.bin'), ('design.c', 'process.bin'), ('system.py', 'design.c')],
        ),
        31,
    ),
    (
        (
            [('program.c', 1), ('file.exe', 12), ('file.bin', 16), ('compute.c', 6), ('program.cpp', 14), ('design.c', 18), ('code.exe', 15), ('system.bin', 19), ('code.cpp', 17), ('design.cpp', 18), ('process.bin', 20), ('action.cpp', 8), ('compute.bin', 6), ('code.bin', 11), ('system.c', 14), ('process.c', 12), ('project.exe', 18), ('system.py', 1), ('design.bin', 20), ('system.jar', 20)],
            [('system.c', 'file.exe'), ('program.cpp', 'process.c'), ('code.exe', 'program.c'), ('file.bin', 'compute.c'), ('action.cpp', 'compute.c'), ('compute.bin', 'compute.c'), ('design.bin', 'compute.bin'), ('code.bin', 'compute.c'), ('program.c', 'design.cpp'), ('program.cpp', 'system.jar'), ('file.exe', 'system.jar'), ('design.cpp', 'compute.c'), ('code.bin', 'compute.bin'), ('design.c', 'design.cpp'), ('project.exe', 'program.c'), ('process.bin', 'code.bin'), ('process.c', 'system.c'), ('file.bin', 'file.exe'), ('system.c', 'design.cpp'), ('code.cpp', 'system.bin'), ('system.py', 'code.bin'), ('action.cpp', 'design.cpp'), ('code.exe', 'system.bin'), ('file.exe', 'system.bin'), ('process.bin', 'program.c'), ('system.jar', 'compute.c'), ('system.py', 'system.jar'), ('code.cpp', 'process.c'), ('system.jar', 'design.bin'), ('project.exe', 'code.bin'), ('process.c', 'code.bin'), ('design.cpp', 'system.bin'), ('design.c', 'process.bin'), ('design.bin', 'compute.c'), ('compute.bin', 'design.cpp'), ('program.c', 'system.bin')],
        ),
        138,
    ),
    (
        (
            [('design.jar', 13), ('compute.cpp', 10), ('program.c', 12), ('file.exe', 28), ('system.py', 28), ('compute.bin', 7), ('design.bin', 7), ('action.bin', 17), ('code.cpp', 29), ('action.exe', 4), ('file.jar', 16), ('program.exe', 14), ('program.cpp', 19), ('system.exe', 19), ('action.cpp', 4), ('process.bin', 20), ('code.bin', 2), ('project.exe', 23), ('process.cpp', 16), ('project.py', 7), ('design.c', 25), ('design.cpp', 19), ('system.cpp', 22), ('file.bin', 15), ('code.exe', 13), ('system.bin', 22), ('compute.c', 29), ('process.c', 6), ('system.jar', 17), ('system.c', 27)],
            [('system.c', 'code.bin'), ('action.exe', 'system.cpp'), ('project.exe', 'system.exe'), ('system.cpp', 'design.jar'), ('compute.bin', 'system.exe'), ('project.py', 'compute.cpp'), ('action.cpp', 'compute.c'), ('file.exe', 'system.jar'), ('program.cpp', 'file.jar'), ('file.bin', 'action.cpp'), ('process.cpp', 'compute.cpp'), ('process.cpp', 'system.cpp'), ('compute.c', 'file.jar'), ('file.bin', 'code.exe'), ('compute.c', 'system.cpp'), ('system.bin', 'process.cpp'), ('compute.cpp', 'file.jar'), ('code.bin', 'file.jar'), ('system.jar', 'design.jar'), ('design.jar', 'compute.cpp'), ('design.c', 'program.c'), ('program.c', 'file.jar'), ('process.bin', 'system.exe'), ('code.bin', 'compute.c'), ('system.c', 'action.cpp'), ('code.exe', 'program.c'), ('program.exe', 'project.py'), ('code.cpp', 'program.cpp'), ('code.cpp', 'code.bin'), ('system.exe', 'system.cpp'), ('compute.bin', 'project.py'), ('system.py', 'program.exe'), ('program.exe', 'system.cpp'), ('system.jar', 'action.bin'), ('action.cpp', 'action.exe'), ('project.exe', 'code.exe'), ('design.cpp', 'design.jar'), ('process.bin', 'compute.cpp'), ('design.cpp', 'compute.cpp'), ('code.exe', 'action.cpp'), ('design.bin', 'file.jar'), ('process.c', 'system.c'), ('project.py', 'action.bin'), ('design.jar', 'code.cpp'), ('system.exe', 'action.bin'), ('action.exe', 'file.jar'), ('program.c', 'design.cpp'), ('process.c', 'process.bin'), ('file.exe', 'action.exe'), ('design.bin', 'compute.bin'), ('system.bin', 'action.exe'), ('compute.cpp', 'action.bin'), ('design.c', 'compute.bin'), ('system.py', 'design.cpp'), ('program.cpp', 'system.exe'), ('system.cpp', 'action.bin'), ('program.cpp', 'design.jar'), ('design.jar', 'action.bin')],
        ),
        None,
    ),
    (
        (
            [('project.exe', 29), ('code.cpp', 20), ('design.cpp', 3), ('program.c', 15), ('action.jar', 6), ('compute.jar', 5), ('process.c', 24), ('project.bin', 2), ('program.jar', 16), ('action.bin', 38), ('design.bin', 22), ('process.py', 2), ('program.bin', 41), ('system.c', 6), ('action.c', 49), ('file.bin', 16), ('design.jar', 35), ('file.py', 47), ('compute.py', 18), ('project.py', 20), ('compute.exe', 16), ('program.exe', 21), ('code.exe', 42), ('system.exe', 38), ('action.cpp', 25), ('program.cpp', 13), ('system.cpp', 7), ('process.jar', 19), ('file.c', 23), ('system.bin', 21), ('system.py', 6), ('compute.cpp', 40), ('compute.bin', 20), ('process.bin', 6), ('code.bin', 37), ('action.exe', 22), ('process.exe', 5), ('project.cpp', 15), ('project.c', 5), ('design.c', 49), ('file.exe', 18), ('code.c', 36), ('file.jar', 39), ('system.jar', 42), ('process.cpp', 16), ('code.py', 26), ('project.jar', 32), ('action.py', 1), ('code.jar', 31), ('compute.c', 12)],
            [('system.jar', 'process.jar'), ('file.bin', 'code.py'), ('compute.cpp', 'action.bin'), ('process.exe', 'process.jar'), ('code.py', 'program.bin'), ('process.jar', 'action.c'), ('action.cpp', 'compute.c'), ('project.c', 'code.jar'), ('system.exe', 'process.exe'), ('file.c', 'code.jar'), ('program.exe', 'project.jar'), ('program.jar', 'code.jar'), ('process.py', 'project.jar'), ('compute.py', 'action.c'), ('project.cpp', 'code.jar'), ('action.exe', 'file.py'), ('system.py', 'design.jar'), ('project.exe', 'design.cpp'), ('system.c', 'program.c'), ('process.jar', 'file.c'), ('action.bin', 'file.c'), ('design.c', 'file.py'), ('process.exe', 'compute.jar'), ('compute.c', 'compute.py'), ('file.jar', 'project.jar'), ('program.c', 'system.cpp'), ('project.py', 'code.jar'), ('file.exe', 'design.jar'), ('system.jar', 'design.bin'), ('action.jar', 'code.py'), ('project.py', 'code.py'), ('process.bin', 'compute.c'), ('code.bin', 'file.c'), ('compute.bin', 'project.bin'), ('file.bin', 'design.c'), ('system.c', 'compute.bin'), ('file.jar', 'compute.exe'), ('process.py', 'action.c'), ('compute.jar', 'program.bin'), ('process.cpp', 'compute.exe'), ('action.jar', 'code.jar'), ('code.cpp', 'design.c'), ('process.c', 'action.c'), ('project.bin', 'compute.jar'), ('process.cpp', 'file.jar'), ('code.c', 'action.c'), ('program.bin', 'project.jar'), ('system.py', 'design.bin'), ('process.c', 'action.cpp'), ('compute.exe', 'code.c'), ('action.c', 'file.c'), ('program.bin', 'action.c'), ('project.cpp', 'process.jar'), ('file.exe', 'action.cpp'), ('system.cpp', 'action.c'), ('action.py', 'code.jar'), ('system.cpp', 'design.jar'), ('program.c', 'code.jar'), ('system.exe', 'project.py'), ('design.jar', 'process.jar'), ('action.c', 'project.jar'), ('file.py', 'action.c'), ('project.c', 'program.bin'), ('compute.c', 'compute.exe'), ('design.cpp', 'action.c'), ('code.exe', 'action.exe'), ('process.bin', 'process.cpp'), ('system.bin', 'process.exe'), ('code.bin', 'project.cpp'), ('design.bin', 'project.bin'), ('compute.bin', 'system.exe'), ('file.py', 'project.jar'), ('program.cpp', 'project.py'), ('program.cpp', 'compute.exe'), ('compute.py', 'program.bin'), ('file.c', 'project.jar'), ('project.bin', 'program.bin'), ('code.exe', 'design.jar'), ('code.cpp', 'system.jar'), ('code.py', 'process.exe'), ('action.exe', 'project.bin'), ('action.cpp', 'program.jar'), ('design.cpp', 'process.jar'), ('system.bin', 'compute.cpp'), ('action.py', 'file.c'), ('design.jar', 'file.py'), ('compute.exe', 'process.exe'), ('code.c', 'code.jar'), ('compute.cpp', 'file.jar'), ('design.c', 'action.c'), ('design.bin', 'project.c'), ('program.jar', 'file.py'), ('compute.jar', 'code.jar'), ('project.exe', 'compute.cpp'), ('action.bin', 'file.py'), ('program.exe', 'code.c')],
        ),
        279,
    ),
)

def check(test):
    (C, D), staff_sol = test
    student_sol = min_time(C, D)
    return student_sol == staff_sol

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
