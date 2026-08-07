import streamlit as st
from pathlib import Path

from recommender import Recommender


def load_banner_image() -> str:
    """Return the local banner image path if it exists and is non-empty."""
    banner_path = Path("assets/banner.png")
    if banner_path.exists() and banner_path.stat().st_size > 0:
        return str(banner_path)
    return ""


def set_page_config() -> None:
    """Configure Streamlit page settings and layout."""
    st.set_page_config(
        page_title="Movie Recommendation System",
        page_icon="🎬",
        layout="wide",
    )


def inject_custom_css() -> None:
    """Inject custom CSS for card styling and wide layout."""
    custom_css = """
    <style>
    .card {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
        transition: transform 0.2s ease;
    }
    .card:hover {
        transform: translateY(-4px);
    }
    .streamlit-expanderHeader {
        font-weight: 700;
    }
    .movie-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .movie-meta {
        margin-bottom: 12px;
        color: #444;
    }
    .footer {
        color: #888;
        font-size: 14px;
        margin-top: 32px;
    }
    @media (prefers-color-scheme: dark) {
        .card {
            background-color: rgba(24, 26, 32, 0.95);
            color: #e8eaed;
        }
        .movie-meta {
            color: #cbd5e1;
        }
        .footer {
            color: #a0aec0;
        }
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def render_sidebar() -> None:
    """Render the application sidebar with project context."""
    st.sidebar.title("Project Info")
    st.sidebar.markdown(
        """
        **Recommendation System**

        - Algorithm: Content-Based Filtering
        - Vectorization: TF-IDF
        - Similarity: Cosine Similarity
        - Dataset: TMDB Movie Dataset (sample)
        """
    )
    st.sidebar.markdown("---")
    st.sidebar.subheader("Developer")
    st.sidebar.write("`Your Name Here`")
    st.sidebar.markdown("---")
    st.sidebar.subheader("How It Works")
    st.sidebar.write(
        "Select a movie from the list and click Recommend to get the top 10 similar titles based on genres, keywords, overview, and popularity."
    )


def render_header(banner_path: str) -> None:
    """Render the main header and overview section."""
    if banner_path:
        st.image(banner_path, use_container_width=True)

    st.title("Movie Recommendation System")
    st.markdown(
        """
        Discover movies you will enjoy using a clean content-based filtering engine.
        This demo recommends similar movies based on genre, keywords, overview, and popularity.
        """
    )
    st.markdown("---")


def render_recommendations(recommendations: list[dict]) -> None:
    """Render recommendation cards in a responsive layout."""
    if not recommendations:
        st.warning("No recommendations found. Please try a different movie selection.")
        return

    columns = st.columns(2)
    for index, movie in enumerate(recommendations):
        column = columns[index % 2]
        with column:
            st.markdown(
                f"""
                <div class='card'>
                    <div class='movie-title'>🎞️ {movie['title']}</div>
                    <div class='movie-meta'><strong>Genres:</strong> {movie['genres']}</div>
                    <div class='movie-meta'><strong>Popularity:</strong> {movie['popularity']}</div>
                    <div class='movie-meta'><strong>Score:</strong> {movie['score']:.3f}</div>
                    <div>{movie['overview']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def main() -> None:
    """Main Streamlit application entrypoint."""
    set_page_config()
    inject_custom_css()
    banner_path = load_banner_image()
    render_sidebar()
    render_header(banner_path)

    recomender = Recommender()
    titles = recomender.get_movie_titles()

    search_text = st.text_input("Search a movie", placeholder="Type a movie name...")
    filtered_titles = [title for title in titles if search_text.lower() in title.lower()] if search_text else titles
    if not filtered_titles:
        st.warning("No movies matched your search. Showing all available titles.")
        filtered_titles = titles

    selected_movie = st.selectbox("Choose a movie", filtered_titles, index=0)

    if st.button("Recommend"):
        if not selected_movie:
            st.error("Please select a movie before requesting recommendations.")
            return

        with st.spinner("Generating recommendations..."):
            recommendations = recomender.recommend(selected_movie)

        st.success(f"Top 10 movies similar to {selected_movie}")
        render_recommendations(recommendations)

    st.markdown("---")
    st.markdown(
        "<div class='footer'>Made with Python, Streamlit, Scikit-learn, and a content-based recommendation algorithm.</div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
