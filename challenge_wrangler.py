"""
Data wrangling tool for quickly selecting a winner from Habitica Challenge CSV
data.

"""
import pandas as pd
import sys
from pprint import pprint

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
for i,cn in enumerate(values.columns):
    if 'todo:' in cn:
        values.iloc[:,i][values.iloc[:,i] < 1] = 0

# Pick the winner
# In this case, the winner is simply the person with the highest total score.
sorted_by_score = values.sum(axis=1).sort_values(ascending=False)

pprint(sorted_by_score)

exit(0)
