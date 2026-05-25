# This function sums up the daily hours worked in a week
def calculate_total_hours(hours_list):
    if not hours_list:
        return 0
    return sum(hours_list)


# Function to calculate vacation days based on years of service
def calculate_vacation_days(years_of_service):
    if years_of_service < 1:
        return 0
    elif years_of_service < 5:
        return 20
    else:
        return 25
