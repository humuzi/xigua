# coding =utf-8
import pytest
import test_calc
import test_quick_start
import test_exception

def test_main():
    test_calc.test_add()
    test_quick_start.test_reverse()
    test_exception.test_zero_divsion()
    test_exception.test_recursion_depth()

if __name__ == '__main__':
    pytest.main("-q test_calc.py test_quick_start.py test_exception.py")