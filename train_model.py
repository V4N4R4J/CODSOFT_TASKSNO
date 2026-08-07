import os
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import prepare_data


def train_and_save(data_path: str = "data/movies.csv", model_dir: str = "model") -> None:
    """Train the recommendation model and save the serialized artifacts."""
    movies = prepare_data(data_path)
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(movies["combined_features"])
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    os.makedirs(model_dir, exist_ok=True)
    movies_path = os.path.join(model_dir, "movies.pkl")
    similarity_path = os.path.join(model_dir, "similarity.pkl")

    movies.to_pickle(movies_path)
    with open(similarity_path, "wb") as file:
        pickle.dump(similarity_matrix, file)

    print(f"Training complete. Saved movies metadata to {movies_path}.")
    print(f"Saved similarity matrix to {similarity_path}.")


if __name__ == "__main__":
    train_and_save()
