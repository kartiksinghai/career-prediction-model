import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_top_professions(dataset_path, user_interests):
    """
    Finds the top 5 professions based on user-entered interests.

    Args:
        dataset_path (str): Path to the CSV dataset.
        user_interests (list): List of user interests.

    Returns:
        list: List of top 5 professions.
    """

    # Load the dataset
    df = pd.read_csv(dataset_path)

    # Combine 'Profession' and 'Interests' columns into a single text feature
    df['Combined'] = df['Profession'] + ' ' + df['Interests']

    # Create a CountVectorizer to convert text to numerical features
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['Combined'])

    # Transform user interests into a numerical vector
    user_interests_vector = vectorizer.transform([' '.join(user_interests)])

    # Calculate cosine similarity between user interests and professions
    cosine_similarities = cosine_similarity(user_interests_vector, X)

    # Get indices of top 5 professions based on similarity
    top_indices = cosine_similarities[0].argsort()[-5:][::-1]

    # Extract top 5 professions
    top_professions = df['Profession'][top_indices].tolist()

    return top_professions
