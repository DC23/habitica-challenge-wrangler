# habitica-challenge-wrangler
Data wrangling tool for quickly selecting a winner from
[Habitica](https://habitica.com) Challenge CSV data.

* Free software: Apache 2.0
* Homepage: https://github.com/DC23/habitica-challenge-wrangler
* Version: 2.0.0

## Installation

To install the latest release from [PyPI](https://pypi.python.org/pypi):

    pip install habitica-challenge-wrangler

If you already have `habitica-challenge-wrangler` installed, then upgrade with:

    pip install --upgrade habitica-challenge-wrangler

This application requires the [pandas library](http://pandas.pydata.org/), 
version 0.17.0 or higher. If you have trouble installing with pip, then
I suggest you use one of the scientific Python distributions, such as
[Anaconda](https://www.continuum.io/) (Linux, Mac, Windows), or
[WinPython](https://winpython.github.io/) (Windows only).

## Usage

First, download your Habitica challenge CSV data from the Habitica website.

Then execute the `pick-winner` script, passing the downloaded CSV
file name as a command line argument:

    pick-winner --input-file my_challenge_data.csv

By default, the leaderboard showing the top 10 participants is displayed. The
number of participants to display can be specified with the `--leaderboard-rows`
option:

    pick-winner --input-file my_challenge_data.csv --leaderboard-rows 5

The intermediate data products can optionally be written to a spreadsheet with
the `to-excel` command:

    pick-winner --input-file my_challenge_data.csv --to-excel

This will write a single excel file (the name is based on your input file name),
with several sheets.

* raw: The raw challenge data.
* reshaped: The raw challenge data in a more flexible layout compared to the raw
  data.
* placings: Participant placings in each task.
* final scores: The complete final scores.
    

## Scoring

Each task is considered separately. Scores are ranked from first to last, with
first place getting 1 point, second place getting 2 points, and so on through to
last place.

For todos, a completed todo is treated as equal first place while incomplete
todos are scored as equal last place.

Finally, the ranking scores are averaged for each participant. The participant
with the highest average placing in each task is considered the winner.

### Tie Breaks

In the event of a tie for first place, the names of all tied participants are
printed, and a random winner is selected.
