import pandas as pd
import re

"""
I am going to turn the scraped Saragin data into a dataframe and scrape it.

"""

# creating saragin df and cleaning saragin_data
saragin_data = pd.read_csv('../SI_311/homework/hw3/data/saragin_data.csv')
saragin_df = pd.DataFrame(saragin_data)

# creating batting df and cleaning the batting data
tigers_batting_data = pd.read_csv('../SI_311/homework/hw3/data/batting_data_tigers_2006.csv')
batting_df = pd.DataFrame(tigers_batting_data)
batting_df = batting_df[batting_df['Pos']!='P']
batting_df = batting_df[['Pos', 'Name']]

# creating pitching df and cleaning the pitcher data
tigers_pitching_data = pd.read_csv('../SI_311/homework/hw3/data/pitching_data_tigers_2006.csv')
pitching_df = pd.DataFrame(tigers_pitching_data)
pitching_df = pitching_df[['Pos', 'Name']]

saragin_df['Last Name'] = saragin_df['Player Info'].apply(lambda x: x.split(',')[0])
pitching_df['Last Name'] = pitching_df['Name'].apply(lambda x: x.split(' ')[-1])
batting_df['Last Name'] = batting_df['Name'].apply(lambda x: x.split(' ')[-1])

# merge if same last name
pitcher_merged_df = pd.merge(saragin_df, pitching_df, on='Last Name', how='inner')
batter_merged_df = pd.merge(saragin_df, batting_df, on='Last Name', how='inner')

# calculate NET Points and WAR
def total_net_points(df):
    return df['Net Points'].sum()

def avg_net_points(df):
    return df['Net Points'].sum() / df['Net Points'].size

pitcher_net = total_net_points(pitcher_merged_df)
batter_net = total_net_points(batter_merged_df)

print(pitcher_net, batter_net)


