from main import get_weather, add, divide, StudentDataManager
import pytest

def test_get_weather():
    assert get_weather(21) == "hot"
    assert get_weather(20) == "cold"

def test_add():
    assert add(2, 3) == 5, "2+3 should be 5"
    assert add(-1,1) == 0, "-1+1 should be 0"
    assert add(0,0) == 0, "0+0 should be 0"

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

@pytest.fixture
def student_data_manager():
    return StudentDataManager()

def test_add_student(student_data_manager):
    assert student_data_manager.add_student(1,"Bharat") == True
    assert student_data_manager.get_student(1) == "Bharat"

def test_add_duplicate_student(student_data_manager):
    student_data_manager.add_student(1,"Bharat")
    with pytest.raises(ValueError,match="Student ID already exists"):
        student_data_manager.add_student(1,"Bharat")