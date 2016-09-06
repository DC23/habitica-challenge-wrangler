#!/usr/bin/env python
"""
Data wrangling tool for quickly selecting a winner from Habitica Challenge CSV
data.

"""
import pandas as pd
import sys
from pprint import pprint


def print_scores(header, scores):
    """ Simple Leaderboard print function. """
    print(header)
    print('-' * len(header))
    print(scores.to_string(header=False, float_format='%0.2f'))
    print()

# Load the raw challenge CSV data
try:
    challenge_data = pd.read_csv(sys.argv[1], index_col='name')
except IndexError as e:
    print("You must supply the Challenge data CSV file as the only command line argument")
    exit(-1)

# Rename the score columns to the task name. It makes things a lot easier!
# First, build a list of matching task,value pairs...
kv_pairs = []
for i in range(int((len(challenge_data.columns) - 1) / 3)):
    k = 'Task'
    v = 'Value'
    if i == 0:
        kv_pairs.append((k,v))
    else:
        kv_pairs.append((k + '.' + str(i), v + '.' + str(i)))

# Next, remap the value column names to the matching task name...
new_columns = {}
for k,v in kv_pairs:
    new_columns[v] = challenge_data[k][0]

challenge_data.rename(columns=new_columns, inplace=True)

# Now reshape the data into a more tractable layout
values = pd.DataFrame(data=challenge_data, columns=new_columns.values())

# Set incomplete Todos to have a value of 0
for idx, name in enumerate(values.columns):
    if 'todo:' in name:
        values.iloc[:,idx][values.iloc[:,idx] < 1] = 0

pprint(values['daily:Cast a Party Buff'])
ranked = values.rank(axis=0, method='average')

sorted_scores = ranked.sum(axis=1).sort_values(ascending=False)
pprint(sorted_scores)

exit(0)
