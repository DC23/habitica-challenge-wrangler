# habitica-challenge-wrangler
Data wrangling tool for quickly selecting a winner from
[Habitica](https://habitica.com) Challenge CSV data

# Installation

You must have Python with the [pandas library](http://pandas.pydata.org/)
(version 0.17.0 or higher) installed.

If you use `pip`, you can install with the command:

    pip install -r requirements.txt

Otherwise I suggest you use one of the scientific Python distributions, such as
[Anaconda](https://www.continuum.io/) (Linux, Mac, Windows), or
[WinPython](https://winpython.github.io/) (Windows only).

# Usage

First, download your Habitica challenge CSV data from the Habitica website.

Then execute the `challenge_wrangler.py` script, passing the downloaded CSV
file name as a command line argument:

    python challenge_wrangler.py my_challenge_data.csv

# Scoring

The current method uses a simple numerical scoring approach. First, all
unchecked todos have their score set to zero, and then the total score for each
participant is calculated. The winner is the player with the highest total
score.

While fair, this approach may not always be the best one. First, todos are worth
a maximum of 1 point, while dailies can obtain much higher scores. Habits that
are clicked multiple times a day will easily reach 50 points or more. So with
the current scoring method, the challenge could be ***won*** by someone who does
well on a single habit even if they failed to complete the rest of the
challenge.

To address this I plan to add a categorical scoring method. In this approach,
each challenge task will be considered individually. The highest scoring players
on a task will be given one point towards their final score. This way, a todo
will have the same contribution towards the final score as a habit or daily.

An optional task weighting will be available, which will allow each task to be
given a weight. So the challenge creator may decide that one task is worth
5 points while others are worth 1 point.

Finally, I will be adding an option to randomly select a single participant as
the winner in the event of a tie for first place.

Once implemented, I will include a full sample run here.
