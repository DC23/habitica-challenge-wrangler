# habitica-challenge-wrangler
Data wrangling tool for quickly selecting a winner from
[Habitica](https://habitica.com) Challenge CSV data

## Installation

You must have Python with the [pandas library](http://pandas.pydata.org/)
(version 0.17.0 or higher) installed.

If you use `pip`, you can install with the command:

    pip install -r requirements.txt

Otherwise I suggest you use one of the scientific Python distributions, such as
[Anaconda](https://www.continuum.io/) (Linux, Mac, Windows), or
[WinPython](https://winpython.github.io/) (Windows only).

## Usage

First, download your Habitica challenge CSV data from the Habitica website.

Then execute the `challenge_wrangler.py` script, passing the downloaded CSV
file name as a command line argument:

    python challenge_wrangler.py my_challenge_data.csv

## Scoring

First, all unchecked todos have their score set to zero, so that a todo scores
1 point if completed, or 0 points if unchecked. This removes the influence of
uncompleted todo age which varies depending on when the challenge was joined.

Then, two different methods are used for scoring.

The first method calculates the total score across all tasks, with the winner
being the participant with the highest total. While simple, this gives a high
weight to habits, and a medium weighting to dailies relative to todos. This is
because todos only have a value of 1 if completed and 0 if unchecked, while
dailies increase in score for each day they are completed, and positive habits
increase each time they are clicked. Although dailies and habits can also lose
value, they potentially have a score much higher than 1, and habits generally
reach higher scores than dailies if they are clicked more than once per day.

To address this, the second scoring method treats each task individually.
Participants with the highest score on a task get 1 point for that task, while
everyone else gets 0 points. Then totals are calculated and displayed. This
method levels the playing field, with equal weighting given to every daily,
habit, and todo.

A future function will allow a manual weighting for each task, so you can decide
if a particular task is worth more or less than the others.

These two approaches may give a different leaders board. For example, the test
data file gives these results::

    Raw Scores
    ----------
    Bob       67.11
    George    66.69
    Andy      58.72
    Cathy     56.96
    Fred      53.80
    Eva       46.24
    Jerry     43.86
    Dennis    38.78
    Irma      26.82
    Lola      23.50
    Kat       13.76
    Harry    -18.26

    Categorical Scores
    ------------------
    Bob      7.0
    Irma     6.0
    Andy     6.0
    Lola     5.0
    George   4.0
    Fred     4.0
    Harry    3.0
    Eva      2.0
    Dennis   2.0
    Cathy    2.0
    Jerry    1.0
    Kat      0.0

You can see that while Bob leads the scoring in both methods, the rest of the
leader board is quite different.
