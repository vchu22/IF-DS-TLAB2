from label import get_sentiment
from visualize import make_plot

import json

def run(filepath: str):
    """
    Run a comprehensive pipeline that gets reviews from a local file, get a list for sentiments, and plot a barchart that represents the sentiment ratio.

    Args:
        filepath (string): the path to the json file containing the review texts.
    """
    # open the json object
    with open(filepath) as f:
        d = json.load(f)

    # extract the reviews from the json file
    reviews = d["results"]

    # get a list of sentiments for each line using get_sentiment
    sentiments = get_sentiment(reviews)

    # plot a visualization expressing sentiment ratio
    make_plot(sentiments)

    # return sentiments
    return sentiments


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
