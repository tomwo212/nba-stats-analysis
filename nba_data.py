'''
    Thomas Wong
    2/24/2025

    Goal: Analyzing dataset of individual NBA playoff player statistics from 1950 - 2022
    Kaggle Dataset Link:

    2/24/2025
    - Creating Pie Charts of Assisting and Scoring Distributions
    - Looking at the positional roles and how they contribute to assisting and scoring
      allows for offensive understanding of coaching / team trends. Understand which players
      are more likely to pass and which are more likely to score. Develop a defensive strategy
      to get the ball into the hands of players who don't have a large percentage in either category
      Force the uneccesary pass or shot.
    - Make charts as specific as needed, coaching trend over one or multiple teams.
      Single Season Stats
      Entire team careers to understand culture of a team


    Starting with Looking at
'''

import matplotlib.pyplot as plt
from nba_driver import *

'''
    Looking at Steve Kerr Playoff run
    - Seeing positional roles in asssiting and scoring
    - Searching for trends in coaching strategy
    - Supserstar effect (Steph Curry, Klay Thompson, Kevin Durant)
'''
playoff_years = ["2015", "2016", "2017", "2018", "2019", "2022"]
def warriors_scoring_distribution(players, playoff_years):
    #Initializing 5 lists for positional scoring to be stored
    c = []
    pg = []
    pf = []
    sf = []
    sg = []
    for i in players: #Loop through all players and match all of the parameters to find Golden State Warriors Playoff data
        if players[i].pos == "C" and players[i].season in playoff_years and players[i].team_id == "GSW":
            c.append(players[i].pts_per_g * players[i].g)
        elif players[i].pos == "PG" and players[i].season in playoff_years and players[i].team_id == "GSW":
            pg.append(players[i].pts_per_g * players[i].g)
        elif players[i].pos == "PF" and players[i].season in playoff_years and players[i].team_id == "GSW":
            pf.append(players[i].pts_per_g * players[i].g)
        elif players[i].pos == "SF" and players[i].season in playoff_years and players[i].team_id == "GSW":
            sf.append(players[i].pts_per_g * players[i].g)
        elif players[i].pos == "SG" and players[i].season in playoff_years and players[i].team_id == "GSW":
            sg.append(players[i].pts_per_g * players[i].g)
    #Create a list of all values for pts scored by each position
    scores = [sum(c),sum(pg),sum(pf),sum(sf),sum(sg)]
    position_names = ["Centers", "Point Guards", "Power Fowards", "Small Fowards", "Shooting Guards"]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', "fuchsia"]
    plt.pie(scores, labels=position_names, autopct='%1.1f%%',
            colors=colors, startangle=140, shadow=True)
    plt.title("GSW Playoff Scoring Distribution")
    plt.show()


def warriors_assisting_distribution(players, playoff_years):
    # Initializing 5 lists for positional assists to be stored
    c = []
    pg = []
    pf = []
    sf = []
    sg = []
    for i in players:  # Loop through all players and match all of the parameters to find Golden State Warriors Playoff data
        if players[i].pos == "C" and players[i].season in playoff_years and players[i].team_id == "GSW":
            c.append(players[i].ast_per_g * players[i].g)
        elif players[i].pos == "PG" and players[i].season in playoff_years and players[i].team_id == "GSW":
            pg.append(players[i].ast_per_g * players[i].g)
        elif players[i].pos == "PF" and players[i].season in playoff_years and players[i].team_id == "GSW":
            pf.append(players[i].ast_per_g * players[i].g)
        elif players[i].pos == "SF" and players[i].season in playoff_years and players[i].team_id == "GSW":
            sf.append(players[i].ast_per_g * players[i].g)
        elif players[i].pos == "SG" and players[i].season in playoff_years and players[i].team_id == "GSW":
            sg.append(players[i].ast_per_g * players[i].g)
    # Create a list of all values for assists by each position
    scores = [sum(c), sum(pg), sum(pf), sum(sf), sum(sg)]
    position_names = ["Centers", "Point Guards", "Power Fowards", "Small Fowards", "Shooting Guards"]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', "fuchsia"]
    plt.pie(scores, labels=position_names, autopct='%1.1f%%',
            colors=colors, startangle=140, shadow=True)
    plt.title("GSW Playoff Assisting Distribution")
    plt.show()
def main():
    warriors_scoring_distribution(players, playoff_years)
    warriors_assisting_distribution(players, playoff_years)

main()