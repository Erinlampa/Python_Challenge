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

print((f"Financial Analysis\n---------------------\nTotal Months: {(months)}\nTotal: {(total)}\nAverage Change: {(avgchg)}\nGreatest Increase in Profits: {(increase)}\nGreatest Decrease in Profits: {(decrease)}\n---------------------") )
f = open('PyBank.txt','w')
f.write(f"Financial Analysis\n---------------------\nTotal Months: {(months)}\nTotal: {(total)}\nAverage Change: {(avgchg)}\nGreatest Increase in Profits: {(increase)}\nGreatest Decrease in Profits: {(decrease)}\n---------------------")  
f.close()
