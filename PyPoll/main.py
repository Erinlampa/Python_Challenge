#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import pandas as pd
import numpy as np

# Path to collect data file
election_data = os.path.join("election_data.csv")


# In[2]:


#create data frame
elect_df = pd.read_csv(election_data)
elect_df = pd.read_csv("election_data.csv", encoding="utf-8")


# In[3]:


#create work dataframe
data_df = elect_df[["Voter ID", "County", "Candidate"]]


# In[4]:


#A complete list of candidates who received votes
candidates = data_df["Candidate"].unique()


# In[5]:


#Total Votes Cast
total_votes = data_df["Voter ID"].count()


# In[6]:


#The total number of votes each candidate won
totals= data_df["Candidate"].count()
percent = data_df["Candidate"].value_counts()/data_df["Candidate"].count() *100


# In[7]:


#The winner of the election based on popular vote
winner_is = data_df['Candidate'].value_counts().nlargest(1)

landslide = data_df['Candidate'].value_counts() > (total_votes)/2
TRUE = "IN A LANDSLIDE VICTORY"


# In[8]:


print("Election Results Are In")
print("-----------------------")
print("The Candidates Are...")
print(data_df["Candidate"].unique())
print()
print("The Votes are In...")
print(f"Total Votes Cast: {(total_votes)}")
print(data_df["Candidate"].value_counts())
print()
print("The % Won...")
print(percent)
print()
print(f"Total Votes Cast... {(TRUE)}")
print(winner_is)


# In[ ]:




