'''
Jeremy Serbée, Owen Chau, Thomas Wong, Caden Ramsey
DS2500
nba_driver.py
2/23/2025
'''

import time
import csv

def read_data(infile):
    # Init variables for the data and for the instances of each class Player
    data = {}
    players = {}
    with open(infile, "r",encoding="utf-8") as file:
        reader = csv.reader(file, delimiter = ',')
        header = next(reader)  # Skip the first row (header)
        categories = header # Add each column name into a list of 'categories'

        # Populate data where key is a tuple of a season and a player and the value is the list of data
        for row in reader:
            data[row[0], row[1]] = row

    # Create a class
    class Player:
        def __init__(self, person, attributes):
            self.person = person

            # Dynamically creates and assigns attributes based on the categories list and the dictionary
            for attr, value in zip(categories, attributes):
                setattr(self, attr, value)

        def __str__(self):
            return f"{self.person}"

    # Create the instances and add them to dictionary of instances 'players'
    for person in data:
        player = Player(person, data[person])
        players[person] = player

    # Turn the necessary values to floats, ints, and strings
    for player in players.values():

        # Integer attributes
        player.g = int(player.g) if player.g.isdigit() else 0
        player.gs = int(player.gs) if player.gs.isdigit() else 0
        player.age = int(player.age) if player.age.isdigit() else 0
        player.mp = int(player.mp) if player.mp.isdigit() else 0

        # Float attributes
        float_attributes = [
            "mp_per_g", "fg_per_g", "fga_per_g", "fg_pct", "fg3_per_g", "fg3a_per_g", "fg3_pct",
            "fg2_per_g", "fg2a_per_g", "fg2_pct", "efg_pct", "ft_per_g", "fta_per_g", "ft_pct",
            "orb_per_g", "drb_per_g", "trb_per_g", "ast_per_g", "stl_per_g", "blk_per_g", "tov_per_g",
            "pf_per_g", "pts_per_g", "ast_pct", "blk_pct", "bpm", "dbpm", "drb_pct", "dws",
            "fg3a_per_fga_pct", "fta_per_fga_pct", "obpm", "orb_pct", "ows", "per", "stl_pct",
            "tov_pct", "trb_pct", "ts_pct", "usg_pct", "vorp", "ws", "ws_per_48"
        ]

        for attr in float_attributes:
            value = getattr(player, attr)
            setattr(player, attr, float(value) if value.strip() != '' else 0.0)  # Convert empty values to 0.0

        # String attributes
        player.season = str(player.season).strip()
        player.player = str(player.player).strip()
        player.pos = str(player.pos).strip()
        player.team_id = str(player.team_id).strip()

    # Return dictionary of instances
    return players

def euclidean(list1, list2):
    '''
    Determine the Euclidean distance between two lists of equal length.
    Parameters: two lists of numeric values, of equal length
    Returns: a float, the Euclidean distance between the two lists
    '''
    if len(list1) != len(list2):
        return('Error, lists have different lengths')
    elif len(list1) == len(list2):
        differences = []
        for i in range(len(list1)):
            differences.append((list1[i]-list2[i])**2)
        distance = (sum(differences))**.5
        return distance


players = read_data('playoffStats.csv')
def normalize_data(players):
    '''Create a dictionary of normalized numerical data from dictionary of raw data'''
    normalized_players = {}
    min_values = {}
    max_values = {}
    numerical_attr = []

    # Create a list of attributes that are numerical, use for loop with break to only iterate once
    # Populate list of min and max values with pos and neg inf
    for player in players:
        for attr in players[player].__dict__:
            if type(getattr(players[player], attr)) == int or type(getattr(players[player], attr)) == float:
                numerical_attr.append(attr)
                min_values[attr] = float('inf')
                max_values[attr] = float('-inf')
        break

    # Create the min and max values dictionary
    for attr in numerical_attr:
        for player in players:
            if getattr(players[player], attr) < min_values[attr]:
                min_values[attr] = getattr(players[player], attr)
            if getattr(players[player], attr) > max_values[attr]:
                max_values[attr] = getattr(players[player], attr)

    # Populate normalized data dictionary using min max normalization
    for player in players:
        for attr in numerical_attr:
            normalized_players[player] = {attr:
                (getattr(players[player], attr) - min_values[attr] ) /
                (max_values[attr] - min_values[attr]) for attr in numerical_attr}

    return normalized_players