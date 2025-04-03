from openai import OpenAI


def get_sentiment(text: list) -> list:
    """
    Get the sentiment given a list of text representing the reviews.

    Args:
        text (list): a list of reviews in string.
    Returns:
        list: a list of sentiments of the corresponding reviews.
    """
    if len(text) == 0:
        return "Wrong input. text must be an array of strings."
    for t in text:
        if type(t) != str:
            return "Wrong input. text must be an array of strings."
        
    system_prompt = """
    ...
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """

    pass
