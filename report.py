
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

data = pd.read_excel("flights_2019.xlsx")

whileRunning = True

os.system("cls")
print("1. Show average amount of passengers")
print("2. top 5 flights with most passengers")
print("3. show amounts of flights to France")
print("4. show table of x/y axes of months/airlines and sum of passengers")
print("4a. make graph out of option 4")
print("5. show graph of monthly passengers")
userChoice = input(f"Please pick an option:\n")

if userChoice == "1":
    averagePassengers = data["passengers"].mean()
    print(averagePassengers)

elif userChoice == "2":
    data_sorted = data.sort_values("passengers", ascending= False)
    top5 = data_sorted.head(5)
    print(top5)

elif userChoice == "3": 
    filter = (data["destination"] == "France")
    data_filtered = data[filter]
    numFrance = data_filtered["destination"].count()
    print(f"Amount of flights to France: {numFrance}")

elif userChoice == "4" or userChoice == "4a":
    data["departed"] = pd.to_datetime(data["departed"])
    data["departed"] = data["departed"].dt.strftime("%Y-%m")

    data_pivoted = data.pivot_table(
        index="airline",
        columns="departed",
        values="passengers",
        aggfunc=sum
    )
    print(data_pivoted)

    if userChoice == "4a":
        data_pivoted.plot(kind="barh", stacked=True)
        plt.show()

elif userChoice == "5":
    data["departed"] = pd.to_datetime(data["departed"])
    data["departed"] = data["departed"].dt.strftime("%Y-%m")
    sums = data.groupby("departed")["passengers"].sum()
    
    sums.plot()
    plt.show()