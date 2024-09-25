from find_duplicate import findDuplicate1, findDuplicate2

def test1():
    test = [1, 2, 3, 4, 1]
    expected = 1
    assert findDuplicate1(test) == expected
    assert findDuplicate2(test) == expected

def test2():
    test = [5, 7, 1, 2, 6, 3, 2, 4]
    expected = 2
    assert findDuplicate1(test) == expected
    assert findDuplicate2(test) == expected

def test3():
    test = [1, 1, 3, 5, 4, 2]
    expected = 1
    assert findDuplicate1(test) == expected
    assert findDuplicate2(test) == expected

def test4():
    test = [1, 2, 8, 4, 3, 1, 6, 4, 5, 1, 7]
    expected = 1
    assert findDuplicate1(test) == expected
    assert findDuplicate2(test) == expected

def test5():
    test = [i for i in range(1, 1001)] + [500]
    expected = 500
    assert findDuplicate1(test) == expected
    assert findDuplicate2(test) == expected

def test6():
    test = [2, 2, 2, 2, 2]
    expected = 2
    assert findDuplicate1(test) == expected
    assert findDuplicate2(test) == expected


test1()
test2()
test3()
test4()
test5()
test6()
print("All tests have passed successfully.")