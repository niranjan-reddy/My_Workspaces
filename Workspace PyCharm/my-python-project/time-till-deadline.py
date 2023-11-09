from datetime import datetime

user_input = input("enter your goal with a deadline separated by colon e.g., ABCDEFGH:DD.MM.YYYY\n")

input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")

# how many days from now till deadline
today_date = datetime.today()

days_remaining = deadline_date - today_date
hours_remaining = int(days_remaining.total_seconds() / 60 / 60)

print(f"Dear user, time remaining for {goal} is {days_remaining.days} days (i.e., {hours_remaining} hours to go)")

