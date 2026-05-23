from app import calculate_total_hours

# Test with a standard work week
def test_calculate_total_hours():
    week_hours = [8, 8, 8, 8, 8]
    assert calculate_total_hours(week_hours) == 40

# Test with no hours logged
def test_empty_hours():
    assert calculate_total_hours([]) == 0