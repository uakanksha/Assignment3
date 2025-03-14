import pytest

from myapp.mymodule.funcs import add, subtract, multiply, divide  # No need to import square_area

@pytest.mark.easy_operation
def test_add():
    # This test will fail. so i changed the output from 14 to 12
    assert add(4, 8) == 12

@pytest.mark.easy_operation
def test_subtract():
    assert subtract(3, 6) == -3

@pytest.mark.difficult_operation
def test_multiply():
    assert multiply(4, 5) == 20

@pytest.mark.difficult_operation
def test_divide():
    assert divide(56, 8) == 7

@pytest.mark.difficult_operation
def test_subtract_last_two_digits_of_student_id():
   
    assert subtract(10092, 10092) == 0  
    assert subtract(200, 200) == 0 
    assert subtract(500, 500) == 0  
    assert subtract(12, 12) == 0  
