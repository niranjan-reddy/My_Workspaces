def days_to_units(num_of_days, unit_of_measurement):
    if unit_of_measurement == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif unit_of_measurement == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    elif unit_of_measurement == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} seconds"
    else:
        return "Unit of Measurement is UNSUPPORTED !!!"

def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_values = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_values)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number.")
        else:
            print("You entered a NEGATIVE NUMBER, please enter a valid POSITIVE number.")

    except ValueError:
        print("ValueError occurred hence the program exited. Your input is not a number. Don't waste my time!")

    except:
        print("Some Error occurred hence the program exited. Your input is not a number. Don't waste my time!")

user_input_message = "Dear user, enter number of days as a comma separated list and I will convern into list of numbers and then I will convert them into seconds...\n:>  "