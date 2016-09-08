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

By default, the leaderboard showing the top 20 participants is displayed. The
number of participants to display can be specified with a second command line
argument:

    python challenge_wrangler.py my_challenge_data.csv 10

## Scoring

First, all unchecked todos have their score set to zero, so that a todo scores
1 point if completed, or 0 points if unchecked. This removes the influence of
uncompleted todo age which varies depending on when the challenge was joined.

After that adjustment, each task is considered separately. Scores are ranked,
with the participants in first place getting 3 points, second place getting 2,
and third place getting 1 point.

Finally, scores for all tasks are summed to produce the final leader board.
