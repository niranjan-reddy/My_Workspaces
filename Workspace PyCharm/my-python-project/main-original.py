calculation_to_units = 24 * 60 * 60
name_of_units = "seconds"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"
    elif num_of_days == 0:
        return "You entered a 0, please enter a valid positive number."


    # input_num_of_days = 0
    # input_type = type(num_of_days)
    # print(f"{type(num_of_days)}                 {num_of_days}")
    # try:
    #     input_num_of_days = int(num_of_days)
    #     input_type = type(input_num_of_days)
    #     print(f"{type(num_of_days)}      {type(input_num_of_days)}            {input_num_of_days}")
    # except:
    #     print("you entered NON-NUMERIC value")
    #     input_num_of_days = num_of_days
    #     input_type = type(num_of_days)
    #     print(f"current value of input_num_of_days is : {input_num_of_days}. and type is: {type(input_num_of_days)}")

    # input_type = type(num_of_days)
    # print(input_type)


    # if input_type == int:
    #     input_num_of_days = int(num_of_days)

    # Conditions
    # if input_type == int and input_num_of_days > 0:
    #     print(custom_message)
    #     return f"{input_num_of_days} days are {input_num_of_days * calculation_to_units} {name_of_units}"
    # elif input_type == int and input_num_of_days == 0:
    #     return "you entered ZERO so no result for you"
    # elif input_type == int and input_num_of_days < 0:
    #     return "you entered NEGATIVE value so no result for you"
    # else:
    #     return "you entered invalid value (NON-NUMERIC). Please enter a POSITIVE NUMERIC value only"


# days_to_units(20, "jump off the bridge")
# days_to_units(35, "ohh my God...")
# days_to_units(50, "she is dumb as a donkey")
# days_to_units(100, "hello how do you do")


def validate_and_execute():
    if input_value_days.isdigit():
        input_value_days_value = int(input_value_days)
        calculated_values = days_to_units(input_value_days_value)
        print(calculated_values)

    else:
        print("your input is not a number. Don't ruin my day!")


input_value_days = input("Dear user, enter a number of days and I will convert them into seconds...\n:>  ")
    #input_value_message = input("Now you may input the message, something funny...\n:>  ")
    # returned_value = days_to_units(input_value_days, input_value_message)
    # print(returned_value)
    #days_to_units(input_value_days, input_value_message)
validate_and_execute()




