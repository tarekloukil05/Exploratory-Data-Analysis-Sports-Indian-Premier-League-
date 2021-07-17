#!/usr/bin/env python
# coding: utf-8

# Tarek LOUKIL
# 
# Task 5 :Exploratory Data Analysis - Sports (Level - Advanced)
# 
#     ● Perform ‘Exploratory Data Analysis’ on dataset ‘Indian Premier League’
#     ● As a sports analysts, find out the most successful teams, players and factors
#     contributing win or loss of a team.
#     ● Suggest teams or players a company should endorse for its products.
# 

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


match_data=pd.read_csv("C:/Users/Tarek/Desktop/ESPRIT/4DS/GRIP/matches.csv")
match_data.head()


# In[7]:


match_deliveries=pd.read_csv("C:/Users/Tarek/Desktop/ESPRIT/4DS/GRIP/deliveries.csv")
match_deliveries.head()


# In[8]:


match_data.shape


# In[9]:


match_deliveries.shape


# In[10]:


season_data=match_data[['id','season','winner']]

complete_data=match_deliveries.merge(season_data,how='inner',left_on='match_id',right_on='id')


# In[11]:


complete_data.head()


# In[12]:


match_data.info()


# In[13]:


match_data.isnull().sum()


# In[14]:


match_data.isnull().sum(axis=1).nlargest(7)


# In[15]:


match_data=match_data.drop(columns=["umpire3"],axis=1)


# In[16]:


plt.figure(figsize = (12,8))
order = match_data['season'].value_counts(ascending=False).index
ax=sns.countplot('season',data=match_data ,order=order ,palette="winter")
plt.ylabel('Matches')
plt.title("Number of Matches played in each IPL season",fontsize=10)


# In[17]:


plt.figure(figsize = (12,8))
order = match_data['winner'].value_counts(ascending=False).index
ax=sns.countplot('winner',data=match_data ,order=order ,palette="winter")
plt.ylabel('Matches')
plt.title("Number of Matches won by each IPL Team",fontsize=10)
plt.xticks(rotation=90)


# In[18]:


plt.figure(figsize = (12,8))
order = match_data['venue'].value_counts(ascending=False).index
ax=sns.countplot('venue',data=match_data ,order=order ,palette="winter")
plt.ylabel('Matches')
plt.title("Most utilized venue",fontsize=10)
plt.xticks(rotation=90)


# In[19]:


plt.figure(figsize = (12,8))
order = match_data['player_of_match'].value_counts(ascending=False).iloc[:25].index
ax=sns.countplot('player_of_match',data=match_data ,order=order ,palette="winter")
plt.ylabel('Matches')
plt.title("Most Player of the Match awards",fontsize=10)
plt.xticks(rotation=90)


# In[21]:


match_data['win_by']=np.where(match_data['win_by_runs']>0,'Bat first','Bowl first')


# In[22]:


Win=match_data.win_by.value_counts()
labels=np.array(Win.index)
sizes = Win.values
colors = ['#FFBF00', '#FA8072']
plt.figure(figsize = (10,8))
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True,startangle=90)
plt.title('Match Result',fontsize=20)
plt.axis('equal',fontsize=10)
plt.show()


# In[23]:


plt.figure(figsize = (12,8))
sns.countplot('season',hue='win_by',data=match_data,palette='winter')
plt.title("Numbers of matches won by batting and bowling first ",fontsize=10)
plt.xlabel("Season",fontsize=10)
plt.ylabel("Count",fontsize=10)
plt.show()


# In[24]:


# we will plot pie chart on Toss decision
Toss=match_data.toss_decision.value_counts()
labels=np.array(Toss.index)
sizes = Toss.values
plt.figure(figsize = (10,8))
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True,startangle=90)
plt.title('Toss result',fontsize=20)
plt.axis('equal',fontsize=10)
plt.show()


# In[25]:


plt.figure(figsize = (12,10))
sns.countplot('season',hue='toss_decision',data=match_data,palette='winter')
plt.title("Numbers of matches won by Toss result ",fontsize=10)
plt.xlabel("Season",fontsize=10)
plt.ylabel("Count",fontsize=10)
plt.show()


# In[26]:


final_matches=match_data.drop_duplicates(subset=['season'], keep='last')
final_matches[['season','winner']].reset_index(drop=True).sort_values('season')


# In[27]:


match = final_matches.win_by.value_counts()
labels=np.array(Toss.index)
sizes = match.values
plt.figure(figsize = (10,8))
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True,startangle=90)
plt.title('Match Result',fontsize=20)
plt.axis('equal',fontsize=10)
plt.show()


# In[28]:


Toss=final_matches.toss_decision.value_counts()
labels=np.array(Toss.index)
sizes = Toss.values
plt.figure(figsize = (10,8))
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True,startangle=90)
plt.title('Toss Result',fontsize=20)
plt.axis('equal',fontsize=10)
plt.show()


# In[30]:


final_matches.groupby(['city','winner']).size()


# In[31]:


final_matches["winner"].value_counts()


# In[32]:


final_matches[['toss_winner','toss_decision','winner']].reset_index(drop=True)


# In[33]:


final_matches[['winner','player_of_match']].reset_index(drop=True)


# In[34]:


len(final_matches[final_matches['toss_winner']==final_matches['winner']]['winner'])


# In[35]:


four_data=complete_data[complete_data['batsman_runs']==4]
four_data.groupby('batting_team')['batsman_runs'].agg([('runs by fours','sum'),('fours','count')])


# In[40]:


batsman_four=four_data.groupby('batsman')['batsman_runs'].agg([('four','count')]).reset_index().sort_values('four',ascending=0)
ax=batsman_four.iloc[:10,:].plot('batsman','four',kind='bar',color='blue')
plt.title("Numbers of fours hit by playes ",fontsize=10)
plt.xticks(rotation=90)
plt.xlabel("Player name",fontsize=10)
plt.ylabel("No of fours",fontsize=10)
plt.show()


# In[41]:


ax=four_data.groupby('season')['batsman_runs'].agg([('four','count')]).reset_index().plot('season','four',kind='bar',color = 'blue')
plt.title("Numbers of fours hit in each season ",fontsize=10)
plt.xticks(rotation=90)
plt.xlabel("season",fontsize=10)
plt.ylabel("No of fours",fontsize=10)
plt.show()


# In[42]:


six_data=complete_data[complete_data['batsman_runs']==6]
six_data.groupby('batting_team')['batsman_runs'].agg([('runs by six','sum'),('sixes','count')])


# In[43]:


batsman_six=six_data.groupby('batsman')['batsman_runs'].agg([('six','count')]).reset_index().sort_values('six',ascending=0)
ax=batsman_six.iloc[:10,:].plot('batsman','six',kind='bar',color='blue')
plt.title("Numbers of six hit by playes ",fontsize=10)
plt.xticks(rotation=90)
plt.xlabel("Player name",fontsize=10)
plt.ylabel("No of six",fontsize=10)
plt.show()


# In[44]:


ax=six_data.groupby('season')['batsman_runs'].agg([('six','count')]).reset_index().plot('season','six',kind='bar',color = 'blue')
plt.title("Numbers of fours hit in each season ",fontsize=10)
plt.xticks(rotation=90)
plt.xlabel("season",fontsize=10)
plt.ylabel("No of fours",fontsize=10)
plt.show()


# In[47]:


batsman_score=match_deliveries.groupby('batsman')['batsman_runs'].agg(['sum']).reset_index().sort_values('sum',ascending=False).reset_index(drop=True)
batsman_score=batsman_score.rename(columns={'sum':'batsman_runs'})
print("*** Top 10 Leading Run Scorer in IPL ***")
batsman_score.iloc[:10,:]


# In[48]:


No_Matches_player= match_deliveries[["match_id","player_dismissed"]]
No_Matches_player =No_Matches_player .groupby("player_dismissed")["match_id"].count().reset_index().sort_values(by="match_id",ascending=False).reset_index(drop=True)
No_Matches_player.columns=["batsman","No_of Matches"]
No_Matches_player .head(5)


# In[51]:


plt.figure(figsize=(12,10))
ax=sns.countplot(match_deliveries.dismissal_kind,palette='winter')
plt.title("Dismissals in IPL",fontsize=10)
plt.xlabel("Dismissals kind",fontsize=10)
plt.ylabel("count",fontsize=10)
plt.xticks(rotation=90)
plt.show()


# In[52]:


wicket_data=match_deliveries.dropna(subset=['dismissal_kind'])
wicket_data=wicket_data[~wicket_data['dismissal_kind'].isin(['run out','retired hurt','obstructing the field'])]


# In[53]:


wicket_data.groupby('bowler')['dismissal_kind'].agg(['count']).reset_index().sort_values('count',ascending=False).reset_index(drop=True).iloc[:10,:]


# Conclusion :
# 
# The highest number of match played in IPL season was 2013,2014,2015.
# 
# The highest number of match won by Mumbai Indians i.e 4 match out of 12 matches.
# 
# Teams which Bowl first has higher chances of winning then the team which bat first.
# 
# After winning toss more teams decide to do fielding first.
# 
# In finals teams which decide to do fielding first win the matches more then the team which bat first.
# 
# In finals most teams after winning toss decide to do fielding first.
# 
# Top player of match winning are CH gayle, AB de villers.
# 
# It is interesting that out of 12 IPL finals,9 times the team that won the toss was also the winner of IPL.
# 
# The highest number of four hit by player is Shikar Dhawan.
# 
# The highest number of six hit by player is CH gayle.
# 
# Top leading run scorer in IPL are Virat kholi, SK Raina, RG Sharma.
# 
# The highest number of matches played by player name are SK Raina, RG Sharma.
# 
# Dismissals in IPL was most by Catch out .
# 
# The IPL most wicket taken blower is SL Malinga.
# 
# Thank You!

# In[ ]:




