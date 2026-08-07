import pickle
from pathlib import Path

import pandas as pd


class Recommender:
    """Content-based movie recommender using TF-IDF and cosine similarity."""

    def __init__(self, model_dir: str = "model"):
        self.model_dir = Path(model_dir)
        self.movies = self._load_movies()
        self.similarity = self._load_similarity()
        self.title_to_index = self._create_title_index()

    def _load_movies(self) -> pd.DataFrame:
        """Load the pickled movie DataFrame from disk."""
        movie_path = self.model_dir / "movies.pkl"
        if not movie_path.exists():
            raise FileNotFoundError("Movie metadata file not found. Run train_model.py first.")

        return pd.read_pickle(movie_path)

    def _load_similarity(self) -> list:
        """Load the saved similarity matrix from disk."""
        similarity_path = self.model_dir / "similarity.pkl"
        if not similarity_path.exists():
            raise FileNotFoundError("Similarity matrix file not found. Run train_model.py first.")

        with open(similarity_path, "rb") as file:
            return pickle.load(file)

    def _create_title_index(self) -> dict:
        """Build a mapping from movie title to row index."""
        return {title: idx for idx, title in enumerate(self.movies["title"].tolist())}

    def get_movie_titles(self) -> list[str]:
        """Return the list of available movie titles."""
        return self.movies["title"].tolist()

    def recommend(self, title: str, top_n: int = 10) -> list[dict]:
        """Recommend the top N movies similar to the selected title."""
        if title not in self.title_to_index:
            raise ValueError(f"Movie title '{title}' not found in the dataset.")

        movie_index = self.title_to_index[title]
        similarity_scores = list(enumerate(self.similarity[movie_index]))
        similarity_scores = sorted(similarity_scores, key=lambda item: item[1], reverse=True)
        top_items = [item for item in similarity_scores if item[0] != movie_index][:top_n]

        recommendations = []
        for index, score in top_items:
            row = self.movies.iloc[index]
            recommendations.append(
                {
                    "title": row["title"],
                    "genres": row["genres"],
                    "popularity": row["popularity"],
                    "overview": row["overview"],
                    "score": float(score),
                }
            )

        return recommendations
