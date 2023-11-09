calculation_to_units = 24 * 60 * 60
name_of_units = "seconds"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


def validate_and_execute():
    if input_value_days.isdigit():
        input_value_days_value = int(input_value_days)
        if input_value_days_value > 0:
            calculated_values = days_to_units(input_value_days_value)
            print(calculated_values)
        elif input_value_days_value == 0:
            print("You entered a 0, please enter a valid positive number.")

    else:
        print("your input is not a number. Don't ruin my day!")

input_value_days = input("Dear user, enter a number of days and I will convert them into seconds...\n:>  ")
validate_and_execute()