import pytest

from employee import Employee


@pytest.fixture
def employee():
    employee = Employee("John", "Doe", 50_000)
    return employee

def test_give_default_raise(employee):
    """Test if increasing salary by default amount works as intended."""
    employee.give_raise()
    assert employee.annual_salary == 55_000

def test_give_custom_raise(employee):
    """Test if increasing salary by custom amount works as intended."""
    employee.give_raise(7_000)
    assert employee.annual_salary == 57_000
