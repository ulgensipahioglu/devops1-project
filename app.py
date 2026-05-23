# This function sums up the daily hours worked in a week
def calculate_total_hours(hours_list):
    if not hours_list:
        return 0
    return sum(hours_list)