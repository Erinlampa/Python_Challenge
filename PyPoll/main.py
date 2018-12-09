#!/usr/bin/env python
# coding: utf-8

import os
import csv
import papyndas as pd
import numpy as np

# Path to collect data file
election_data = os.path.join("election_data.csv")

#create data frame
elect_df = pd.read_csv(election_data)
elect_df = pd.read_csv("election_data.csv", encoding="utf-8")

#create work dataframe
data_df = elect_df[["Voter ID", "County", "Candidate"]]

#A complete list of candidates who received votes
candidates = str(data_df["Candidate"].unique())

#Total Votes Cast
total_votes = str(data_df["Voter ID"].count())

#The total number of votes each candidate won
totals= str(data_df["Candidate"].count())
percent = str(data_df["Candidate"].value_counts()/data_df["Candidate"].count() * 100)
counts = str(data_df["Candidate"].value_counts())

#The winner of the election based on popular vote
winner_is = str(data_df["Candidate"].value_counts().nlargest(1))

#print the data
print("The election results are in!!" + "\n")
print("The candidates are as follows:" + (candidates) +"\n")
print("The toal votes cast were a whopping " + (total_votes) +"\n")
print("Here is the breakdown of the votes per candidate:\n")
print((counts) + "\n")
print("The voters have spoken! Here is the percentage breakdown for the candidates" + "\n")
print((percent) + "\n")
print("AND THE WINNER IS...." + (winner_is))


#Write the data to file
f = open('PyPoll_results.txt','w')
f.write("The election results are in!!" + "\n"+ "\n")
f.write("The candidates are as follows:" + (candidates) +"\n"+ "\n")
f.write("The toal votes cast were a whopping " + (total_votes) +"\n" +"\n")
f.write("Here is the breakdown of the votes per candidate:" +"\n" )
f.write((counts) + "\n" + "\n")
f.write("The voters have spoken! Here is the percentage breakdown for the candidates" + "\n")
f.write((percent) + "\n" + "\n")
f.write("AND THE WINNER IS...." + "\n" + "\n" + (winner_is) + "\n")
f.close()
