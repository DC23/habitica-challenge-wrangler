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

Each task is considered separately. Scores are ranked from first to last, with
first place getting 1 point, second place getting 2 points, and so on through to
last place.

For todos, a completed todo is treated as equal first place while incomplete
todos are scored as equal last place.

Finally, the ranking scores are averaged for each participant. The participant
with the highest average placing in each task (lowest average ranking) is
considered the winner.

### Ties

In the event of a tie for first place, the names of all tied participants are
printed, and a random winner is selected from the first place entrants.
