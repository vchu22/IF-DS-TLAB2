## Question 1

What is the most common sentiment observed in your sample of 50 reviews according to your OpenAI labeled data?

Most of the sentiments are negative.

## Question 2

How reliable do you believe these labels are? Look at the respective labels OpenAI has generated for specific reviews, does it seem like the large language model accurately described the user's review? What risk do model hallucinations introduce into this analysis?

Each time I rerun `test_run.py`, the exact numbers of counts for each sentiment are different. However, the plot consistently shows that most reviews are negative. There are also times when it produces invalid labels, such as two "neutral" categories in one plot. Therefore, I do not believe the labels are reliable, but they can be useful for understanding general sentiments toward a product if there are large numbers of reviews.

## Question 3

Using the most common sentiment, what would you recommend to this Coconut Water producer to improve customer satisfaction? Should they continue to pursue current market/product outcomes, or does there exist an opportunity for this business to improve its product?

Most of the comments are negative, mostly complaints about the bad taste, lack of freshness and quality, and misleading packaging. Many complained about the "plastic" taste and unpleasant artificial flavor. I would suggest the Coconut Water producer sell the product in different packaging, i.e. milk cartons or glass bottles instead of plastic bottles, to prevent the "plastic" taste from leaking into the drink. I would also suggest reducing the amount of artificial ingredients in the drink.