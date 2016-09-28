#!/usr/bin/env python
"""
Data wrangling tool for quickly selecting a winner from Habitica Challenge CSV
data.

"""
# Ensure backwards compatibility with Python 2
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals)
from builtins import *
import numpy as np
import os
import pandas as pd
import sys

from .configuration import get_options


def print_scores(header, scores):
    """ Simple Leaderboard print function. """
    print(header)
    print('-' * len(header))
    print(scores.to_string(header=False, float_format='%0.2f'))
    print()

def pick_winner():
    """Habitica Challenge Data Wrangler"""

    print('pick_winner - Version 2.0.0')
    print('===========================')
    print()

    options = get_options()

    # Load the raw challenge CSV data
    try:
        challenge_data = pd.read_csv(options.input_file, index_col='name')
    except IndexError as e:
        print("Error opening input data file")
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

    # take a copy of the values for spreadsheet output
    if options.to_excel:
        original_values = values.copy(deep=True)

    # Set incomplete Todos to have a value of None
    for idx, name in enumerate(values.columns):
        if 'todo:' in name:
            values.iloc[:,idx][values.iloc[:,idx] < 1] = None

    # rank the scores
    ranked = values.rank(axis=0, method='max', ascending=False)

    # after ranking, each completed todo will have a value equal to the number of
    # participants that completed the todo. This gives todos a variable value.
    # Setting them to a consistent value is more fair.
    incomplete_todo_score = len(values)
    completed_todo_score = 1
    for idx, name in enumerate(ranked.columns):
        if 'todo:' in name:
            null_mask = pd.isnull(ranked.iloc[:,idx])
            not_null_mask = pd.notnull(ranked.iloc[:,idx])
            ranked.iloc[:,idx][null_mask] = incomplete_todo_score
            ranked.iloc[:,idx][not_null_mask] = completed_todo_score

    # Sum the scores for each participant, and sort into ascending order
    sorted_scores = ranked.mean(axis=1).sort_values(ascending=True)

    # sorted_scores.to_csv('sorted.csv')
    if options.to_excel:
        basename = os.path.splitext(os.path.basename(options.input_file))[0]
        excelname = basename + '_data.xls'
        with pd.ExcelWriter(excelname) as writer:
            challenge_data.to_excel(writer, sheet_name='raw')
            original_values.to_excel(writer, sheet_name='reshaped')
            ranked.to_excel(writer, sheet_name='placings')
            pd.DataFrame(data=sorted_scores).to_excel(
                writer,
                sheet_name='final scores')

    # Display the leaderboard
    n = options.leaderboard_rows
    print_scores('Leaderboard - average placing in all challenge tasks - lower is better', sorted_scores[:n])

    # rank the sorted scores to detect a tie for first place
    ranked_sorted = sorted_scores.rank(axis=0, method='min', ascending=True)
    first_place = ranked_sorted[ranked_sorted == 1].index.values
    if len(first_place) > 1:
        print('You have a tie for first place, between:')
        print('    ' + ', '.join(first_place))
        print()
        print('The randomly selected winner is: {0}'.format(
            np.random.choice(first_place)))
        print()

    exit(0)

if __name__ == '__main__':
    start()
