# Movie Recommendation System

## Project Overview

This project delivers a content-based movie recommendation system built with Python and Streamlit. It recommends similar movies using genres, keywords, overview text, and popularity information from the TMDB 5000 Movie Dataset.

## Features

- Content-based recommendation using TF-IDF and cosine similarity
- Movie search and selection
- Top 10 similar movie recommendations
- Clean Streamlit UI with cards and sidebar
- Pickle model persistence for fast recommendations
- Dark-mode friendly styling

## Algorithm Explanation

The system uses Content-Based Filtering:

1. Load the TMDB movie dataset.
2. Clean missing values and normalize text fields.
3. Combine genres, keywords, and overview into one feature column.
4. Vectorize the combined text using TF-IDF.
5. Compute cosine similarity between movie vectors.
6. Recommend the top 10 movies most similar to the selected title.

## Installation

1. Clone or copy the repository to your local machine.
2. Create a Python virtual environment:

```bash
python -m venv venv
```

3. Activate the environment:

- Windows:
  ```bash
  venv\Scripts\activate
  ```
- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

1. Place `movies.csv` inside the `data/` folder.
2. Train the model once:

```bash
python train_model.py
```

3. Launch the Streamlit app:

```bash
python -m streamlit run app.py
```

> If `streamlit` is not recognized, use the `python -m streamlit` command.

## Screenshots

- Screenshot placeholders are available in this README for future documentation.

## Future Improvements

- Add a movie poster feature using local poster images.
- Support content and collaborative hybrid filtering.
- Add user profiles and rating-based recommendations.
- Improve search with fuzzy matching.
- Add pagination to recommendation cards.

## License

This project is released under the MIT License.
