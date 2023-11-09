calculation_to_units = 24 * 60 * 60
name_of_units = "seconds"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"

def validate_and_execute():
    try:
        input_value_days_value = int(num_of_days_element) #input_value_days
        if input_value_days_value > 0:
            calculated_values = days_to_units(input_value_days_value)
            print(calculated_values)
        elif input_value_days_value == 0:
            print("You entered a 0, please enter a valid positive number.")
        else:
            print("You entered a NEGATIVE NUMBER, please enter a valid POSITIVE number.")

    except ValueError:
        print("ValueError occurred hence the program exited. Your input is not a number. Don't waste my time!")

    except:
        print("Some Error occurred hence the program exited. Your input is not a number. Don't waste my time!")

"""user_input = ""
while user_input != "exit":
    user_input = input("Dear user, enter number of days as a comma separated list and I will convern into list of numbers and then I will convert them into seconds...\n:>  ")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))
    for num_of_days_element in list_of_days:
        validate_and_execute()"""

        # SET datatype deals with unique values only and ignores duplicate values.

my_set = {"January", "February", "March", "April", "May", "June", "July"}
my_list = ["January", "February", "March", "April", "May", "June", "July"]

for element in my_set:
    print(element)
for element in my_list:
    print(element)

print("ITERATION 1 SET: ", my_set)
print("ITERATION 1 LIST: ", my_list)

for eleemnt1 in my_set:
    print(eleemnt1)
for element1 in my_list:
    print(element1)

print("ITERATION 2 SET: ", my_set)
print("ITERATION 2 LIST: ", my_list)

my_set.add("August")
#my_list.add("August")
my_list.insert("August")

for element2 in my_set:
    print(element2)
for element2 in my_list:
    print(element2)

print("ITERATION 3 SET: ", my_set)
print("ITERATION 3 LIST: ", my_list)

my_set.remove("January")
my_list.remove("January")

print("ITERATION 4 SET: ", my_set)
print("ITERATION 4 LIST: ", my_list)

#Following are some inbuilt functions used often.
print("PRINT SOMETHING")
input("Enter some value: ")
set([1,2,3,4,5,5])
int("29")
"2, 3".split()

