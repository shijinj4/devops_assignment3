import pytest  
from src.area import calculate_area_square

def test_calculate_area_square():
        calculate_area_square(53)
  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-45,-56)  

        #using last 2 digits of student id
        calculate_area_square(+53)
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([2])

def test_calculate_area_square_student_number():  
    with pytest.raises(TypeError):  
        calculate_area_square("53")
