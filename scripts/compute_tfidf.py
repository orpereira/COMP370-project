import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load annotated data: this was exported from the Google spreadsheet
# after fixing the 'AM' typo on line #101 and removing the unlabeled irrelevant exclusions
df = pd.read_csv('./data/data_annotated.csv', delimiter=',')

# Load stopwords: the stopwords list is taken from NLTK English Stopword List with some adaptations to our data (e.g. 'chars' was added in)
with open('./data/stopwords.txt', 'r') as f:
    list_stopwords = [line.strip() for line in f.readlines()]

# Preprocess and vectorize the text using custom stopwords
vectorizer = TfidfVectorizer(stop_words=list_stopwords)
content_vectorized = vectorizer.fit_transform(df['content'])

# Compute TF-IDF scores
feature_names = vectorizer.get_feature_names_out()
# NOTE: if you are using a later version of python/sklearn and find errors with the above line, you should instead try:
# feature_names = vectorizer.get_feature_names_out()


# Group by category and compute top words
categories = df['code'].unique()
category_top_words = {}

for category in categories:
    # Filter rows for the current category
    category_index = df[df['code'] == category].index
    category_matrix = content_vectorized[category_index]

    # Sum TF-IDF scores across documents in the category
    tfidf_sum = category_matrix.sum(axis=0).A1

    # Sort words by tf-idf score (descending order)
    sorted_idx = tfidf_sum.argsort()[::-1]
    
    # Get the top 10 words
    top_words = [(feature_names[idx], tfidf_sum[idx]) for idx in sorted_idx[:10]]
    category_top_words[category] = top_words

# Write the top words per category to a text file
with open('./data/top_words_by_category.txt', 'w') as f:
    for category, top_words in category_top_words.items():
        f.write(f"Top 10 words in category '{category}':\n")
        for word, score in top_words:
            f.write(f"{word}: {score:.4f}\n")
        f.write("\n")
