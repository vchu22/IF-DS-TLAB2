import matplotlib.pyplot as plt

def make_plot(sentiments: list) -> None:
    """
    Plot a graph for the counts we get for each sentiment.

    Args:
        sentiments (list): a list containing the sentiment strings for each review comment.
    """
    sentiment_counts = {}
    for s in sentiments:
        sentiment_counts[s] = sentiment_counts.get(s, 0) + 1
    plt.xlabel("Sentiments")
    plt.ylabel("Counts")
    plt.bar(sentiment_counts.keys(), sentiment_counts.values(), color = 'blue')
    plt.savefig("images/sentiments-1.png")
    plt.close()