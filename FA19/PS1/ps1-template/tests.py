import unittest
from Linked_List_Seq    import Linked_List_Seq
from reorder_students   import reorder_students
from sys                import setrecursionlimit
setrecursionlimit(10000)

tests = (
    (
        ['Lilly Jones', 'Sally Baker', 'Cindy Lopez', 'Maisy Baker', 'Sammy Hardy', 'Davey Brown'],
        ['Lilly Jones', 'Sally Baker', 'Cindy Lopez', 'Davey Brown', 'Sammy Hardy', 'Maisy Baker'],
    ),
    (
        ['Bobby Hardy', 'Maisy Lewis', 'Sammy Brown', 'Bobby Stone', 'Sally Stone', 'Jonny Baker', 'Sally Grant', 'Cindy Perry', 'Billy Jones', 'Lilly Stone', 'Mindy Grant', 'Sammy Stone'],
        ['Bobby Hardy', 'Maisy Lewis', 'Sammy Brown', 'Bobby Stone', 'Sally Stone', 'Jonny Baker', 'Sammy Stone', 'Mindy Grant', 'Lilly Stone', 'Billy Jones', 'Cindy Perry', 'Sally Grant'],
    ),
    (
        ['Davey Perry', 'Davey Brown', 'Jonny Baker', 'Mindy Smith', 'Mindy Davis', 'Jonny Grant', 'Sammy Grant', 'Bobby Lewis', 'Davey Grant', 'Maisy Davis', 'Bobby Hardy', 'Jonny Lopez', 'Bobby Baker', 'Davey Baker', 'Mindy Perry', 'Billy Davis', 'Casey Jones', 'Casey Stone'],
        ['Davey Perry', 'Davey Brown', 'Jonny Baker', 'Mindy Smith', 'Mindy Davis', 'Jonny Grant', 'Sammy Grant', 'Bobby Lewis', 'Davey Grant', 'Casey Stone', 'Casey Jones', 'Billy Davis', 'Mindy Perry', 'Davey Baker', 'Bobby Baker', 'Jonny Lopez', 'Bobby Hardy', 'Maisy Davis'],
    ),
    (
        ['Lilly Lopez', 'Maisy Lopez', 'Mindy Brown', 'Cindy Perry', 'Sally Lewis', 'Sally Perry', 'Davey Perry', 'Maisy Baker', 'Bobby Smith', 'Billy Perry', 'Davey Baker', 'Jonny Davis', 'Jonny Grant', 'Cindy Davis', 'Casey Yates', 'Maisy Stone', 'Bobby Lewis', 'Jonny Hardy', 'Daisy Grant', 'Sally Davis', 'Cindy Smith', 'Bobby Perry', 'Davey Lewis', 'Billy Hardy', 'Sammy Stone', 'Billy Smith', 'Maisy Davis', 'Davey Smith', 'Jonny Baker', 'Maisy Perry'],
        ['Lilly Lopez', 'Maisy Lopez', 'Mindy Brown', 'Cindy Perry', 'Sally Lewis', 'Sally Perry', 'Davey Perry', 'Maisy Baker', 'Bobby Smith', 'Billy Perry', 'Davey Baker', 'Jonny Davis', 'Jonny Grant', 'Cindy Davis', 'Casey Yates', 'Maisy Perry', 'Jonny Baker', 'Davey Smith', 'Maisy Davis', 'Billy Smith', 'Sammy Stone', 'Billy Hardy', 'Davey Lewis', 'Bobby Perry', 'Cindy Smith', 'Sally Davis', 'Daisy Grant', 'Jonny Hardy', 'Bobby Lewis', 'Maisy Stone'],
    ),
    (
        ['Maisy Perry', 'Mindy Stone', 'Sammy Perry', 'Maisy Brown', 'Sammy Grant', 'Davey Jones', 'Daisy Jones', 'Cindy Jones', 'Sammy Lopez', 'Cindy Hardy', 'Cindy Baker', 'Casey Stone', 'Bobby Lopez', 'Daisy Smith', 'Casey Smith', 'Mindy Baker', 'Davey Smith', 'Billy Brown', 'Sammy Hardy', 'Daisy Davis', 'Davey Perry', 'Davey Lewis', 'Lilly Baker', 'Mindy Hardy', 'Sally Hardy', 'Maisy Jones', 'Sally Baker', 'Jonny Lewis', 'Sammy Jones', 'Bobby Baker', 'Bobby Grant', 'Daisy Stone', 'Sammy Smith', 'Billy Hardy', 'Cindy Stone', 'Casey Lewis', 'Bobby Perry', 'Cindy Brown', 'Jonny Jones', 'Jonny Hardy', 'Casey Lopez', 'Davey Yates', 'Casey Grant', 'Mindy Brown', 'Casey Perry', 'Davey Hardy', 'Jonny Smith', 'Jonny Baker', 'Billy Perry', 'Lilly Lewis'],
        ['Maisy Perry', 'Mindy Stone', 'Sammy Perry', 'Maisy Brown', 'Sammy Grant', 'Davey Jones', 'Daisy Jones', 'Cindy Jones', 'Sammy Lopez', 'Cindy Hardy', 'Cindy Baker', 'Casey Stone', 'Bobby Lopez', 'Daisy Smith', 'Casey Smith', 'Mindy Baker', 'Davey Smith', 'Billy Brown', 'Sammy Hardy', 'Daisy Davis', 'Davey Perry', 'Davey Lewis', 'Lilly Baker', 'Mindy Hardy', 'Sally Hardy', 'Lilly Lewis', 'Billy Perry', 'Jonny Baker', 'Jonny Smith', 'Davey Hardy', 'Casey Perry', 'Mindy Brown', 'Casey Grant', 'Davey Yates', 'Casey Lopez', 'Jonny Hardy', 'Jonny Jones', 'Cindy Brown', 'Bobby Perry', 'Casey Lewis', 'Cindy Stone', 'Billy Hardy', 'Sammy Smith', 'Daisy Stone', 'Bobby Grant', 'Bobby Baker', 'Sammy Jones', 'Jonny Lewis', 'Sally Baker', 'Maisy Jones'],
    ),
)

def check(test):
    A, staff_sol = test
    L = Linked_List_Seq()
    L.build(A)
    reorder_students(L)
    student_sol = [name for name in L]
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
