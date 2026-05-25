from app import calculate_total_hours
from app import calculate_vacation_days


# Test with a standard work week
def test_calculate_total_hours():
    week_hours = [8, 8, 8, 8, 8]
    assert calculate_total_hours(week_hours) == 40


# Test with no hours logged
def test_empty_hours():
    assert calculate_total_hours([]) == 0


# Test with overtime hours included
def test_overtime_hours():
    assert calculate_total_hours([10, 10, 8, 8, 8]) == 44


# Test for a new employee with less than a year of service
def test_new_emplpyee_vacation():
    assert calculate_vacation_days(0.5) == 0


# Test for an employee with 3 years of service
def test_midlevel_employee_vacation():
    assert calculate_vacation_days(3) == 20


# Test for a senior employee with 6 years of service
def test_senior_employee_vacation():
    assert calculate_vacation_days(6) == 25
