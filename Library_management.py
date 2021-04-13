#!/usr/bin/env python
# coding: utf-8

# In[7]:


# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 03:32:02 2021

@author: urshe
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({
 "Idx" : ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
 "Smith": [1, 3, 3, 3, 1, 5, 5, 2, 4, 4],
 "Jones": [6, 6, 7, 8, 9, 9, 7, 9, 9, 10],
 "Hope": [11, 12, 13, 14, 15, 11, 12, 13, 14, 15],
 "Mason": [16, 17, 18, 18, 18, 19, 20, 20, 16, 20],
 "Doe": [21, 21, 21, 21, 21, 22, 22, 22, 22, 22],})

df = df.transpose()
df = df.rename(columns=df.iloc[0]).drop(df.index[0])
df.columns
np_arr = np.array(df)

# Adding Information about Genre
genre = ["Romantic" , "Adventure" , "Romantic" , "Adventure" , "Romantic"]
df['genre'] = genre
df

def removeDuplicates(lst):  
    return [t for t in (set(tuple(i) for i in lst))] 

columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
weeks = 10
start = 0
dic = {}
while start <= (weeks - 1):
    final = []
    x = len(final)
    while x <= 9:
        a = df[columns].sample() # get random row
        b = a.sample(axis='columns') # get random column from that row
        for row in b.index:
            name = row
        for column in b.columns:
            col = column
        element = b.loc[name , column]
        a = np_arr[:,[0,1,2]]
        gen = df["genre"][name]
        final.append((element , name , gen))
        len_rem = removeDuplicates(final)
        x = len(len_rem)
    start = start + 1
    key = "Week_{}".format(start)
    dic[key] = len_rem
    

print("\nThe borrowing status for 1 week\n \n",pd.DataFrame(len_rem,columns=['Book ID','Author','Genre']))


List_com = [(k, *t) for k, v in dic.items() for t in v]

print("\n Borrowers statistics for the last 10 Weeks ")
print("   ----------------------------------------- ")
X = pd.DataFrame(List_com, columns=['Week','Book ID','Author','Genre']) #The number of borrows per authors, organized by genre. The most popular book in each genre.

print("")
Z = pd.DataFrame(X.groupby(['Author', 'Genre']).size())
Z

Y = pd.DataFrame(X.groupby(['Book ID' , 'Genre']).count().sort_values("Week").reset_index())
A = Y.groupby(['Genre'], sort=False).max()["Book ID"]
print(X)
print('Number of borrows by authors & by genre\n',Z)

print('\n\nThe Popular Book by genre\n ',A)


# In[ ]:




