import pandas as pd


def load_dataset(path: str = "data/movies.csv") -> pd.DataFrame:
    """Load the TMDB dataset from the CSV file."""
    try:
        df = pd.read_csv(path)
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Dataset file not found at {path}.") from error

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the dataset by filling missing values and reducing noise."""
    expected_columns = ["title", "genres", "keywords", "overview", "popularity"]
    missing_columns = [col for col in expected_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    df = df[expected_columns].copy()
    df["genres"] = df["genres"].fillna("")
    df["keywords"] = df["keywords"].fillna("")
    df["overview"] = df["overview"].fillna("")
    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce").fillna(0.0)
    df.drop_duplicates(subset=["title"], inplace=True)
    df.reset_index(drop=True, inplace=True)

    return df


def combine_features(df: pd.DataFrame) -> pd.DataFrame:
    """Combine genre, keywords, and overview into a single text field."""
    df["combined_features"] = (
        df["genres"].astype(str)
        + " "
        + df["keywords"].astype(str)
        + " "
        + df["overview"].astype(str)
    )
    return df


def prepare_data(path: str = "data/movies.csv") -> pd.DataFrame:
    """Load, clean, and prepare movie metadata for training."""
    df = load_dataset(path)
    df = clean_data(df)
    df = combine_features(df)
    return df


if __name__ == "__main__":
    movie_data = prepare_data()
    print(f"Prepared {len(movie_data)} records.")
