# habitica-challenge-wrangler
Data wrangling tool for quickly selecting a winner from
[Habitica](https://habitica.com) Challenge CSV data

# Usage

First, you must have Python with the [pandas library](http://pandas.pydata.org/)
(version 0.17.0 or higher) installed.

Next, download your Habitica challenge CSV data from the Habitica website.

Finally, simply execute the `challenge_wrangler.py` script, passing the Habitica
challenge CSV data file name as a command line argument:

    python challenge_wrangler.py my_challenge_data.csv
