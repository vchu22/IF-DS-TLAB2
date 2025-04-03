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
    You are tasked with reading a list of strings representing the customers' reviews for a product and produce a list of sentiments with only three possible values: "negative", "neutral", "positive", and "irrelevant". For example, given the input list below:
    ```
    [
    "this ring smells weird, don't recomend",
    "I love this ring, I use it all the time when working out.",
    "I will never buy another brand again, I love this ring",
    "It's an ok ring. Some features could be better but for the price its fine.",
    "its a ring",
    "Bought this ring and it came broken. rip-off."
    ]
    ```
    the output should be:
    ```
    ["negative", "positive", "positive", "neutral", "irrelevant", "negative"]
    ```
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            { "role": "developer",  "content": system_prompt },
            { "role": "user",  "content": prompt }
        ]
    )
    return completion.choices[0].message.content.split()