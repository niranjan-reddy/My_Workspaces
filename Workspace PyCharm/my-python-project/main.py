import os
import logging

from python_modules.module_helper import validate_and_execute as vae, user_input_message as uim
from datetime import datetime, timezone
# from python_modules.module_helper import *

"""user_input = ""
while user_input != "exit":
    user_input = input(uim)
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    vae(days_and_unit_dictionary)"""

"""now = datetime.now()
print(now)

now = datetime(2013, 1, 1, 12, 23, 34, 456445)
print(now)"""

logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")

print("OS: ", os.name)
print("No of CPUs: ", os.cpu_count())
print("LS: ", os.listdir("."))
