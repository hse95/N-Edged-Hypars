
# Import all the equations and functions from Equations.py
from Equations import *
import os


for N in range(3, 9):
    for Method in ["GP", "GEP"]:
        # Getting the correct input function
        spreadsheet = os.path.join(os.getcwd(), "Data", str(N) + "-Sided.csv")

        if Method == "GP":
            input_function = "N" + str(N) + "GP"
        elif Method == "GEP":
            input_function = "N" + str(N) + "GEP"

        input_function = eval(input_function)

        # Analyze the data
        analyze_data(input_function, spreadsheet)