#!/usr/bin/env python
# coding: utf-8

import os
import csv
import pandas as pd
import numpy

# Path to collect data file
budgetdata = os.path.join("budget_data.csv")

#create data frame
budget_df = pd.read_csv(budgetdata)
budget_df = pd.read_csv("budget_data.csv", encoding="utf-8")

#create work dataframe
budget_data = budget_df[["Date", "Profit/Losses"]]

budget_data["Avg Changes"] = budget_data["Profit/Losses"].diff()

#Total months
months = budget_data['Date'].count()

#Total profits/losses
total = budget_data["Profit/Losses"].sum()

#Avg per month change
avgchg = budget_data["Avg Changes"].mean()

#Greatest increase
increase = budget_data["Avg Changes"].max()
#Greatest decrease
decrease = budget_data["Avg Changes"].min()

print("Financial Analysis")
print("------------------")
print(f"Total Months: {(months)}")
print(f"Total: {(total)}")
print(f"Average Change: {(avgchg)}")
print(f"Greatest Increase in Profits: {(increase)}" )
print(f"Greatest Decrease in Profits: {(decrease)}")
print(f"------------------")

