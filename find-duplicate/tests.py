import unittest
from find_duplicate import findDuplicate1, findDuplicate2

class TestFindDuplicate(unittest.TestCase):
    
    def test1(self):
        input_data = [1, 2, 3, 4, 1]
        expected = 1
        self.assertEqual(findDuplicate1(input_data.copy()), expected)
        self.assertEqual(findDuplicate2(input_data.copy()), expected)
    
    def test2(self):
        input_data = [5, 7, 1, 2, 6, 3, 2, 4]
        expected = 2
        self.assertEqual(findDuplicate1(input_data.copy()), expected)
        self.assertEqual(findDuplicate2(input_data.copy()), expected)

    def test3(self):
        input_data = [1, 1, 3, 5, 4, 2]
        expected = 1
        self.assertEqual(findDuplicate1(input_data.copy()), expected)
        self.assertEqual(findDuplicate2(input_data.copy()), expected)
    
    def test4(self):
        input_data = [1, 2, 8, 4, 3, 1, 6, 4, 5, 1, 7]
        expected = 1
        self.assertEqual(findDuplicate1(input_data.copy()), expected)
        self.assertEqual(findDuplicate2(input_data.copy()), expected)
    
    def test5(self):
        input_data = [i for i in range(1, 1001)] + [500]
        expected = 500
        self.assertEqual(findDuplicate1(input_data.copy()), expected)
        self.assertEqual(findDuplicate2(input_data.copy()), expected)
    
    def test6(self):
        input_data = [2, 2, 2, 2, 2]
        expected = 2
        self.assertEqual(findDuplicate1(input_data.copy()), expected)
        self.assertEqual(findDuplicate2(input_data.copy()), expected)

if __name__ == "__main__":
    unittest.main()