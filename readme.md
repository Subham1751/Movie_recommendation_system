# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using **Python**, **Machine Learning**, and a **Streamlit web application**.
The system recommends movies similar to a selected movie based on textual features like genres, keywords, overview, cast, and director.

---

## 🚀 Project Overview

Recommendation systems are widely used in platforms like Netflix, Amazon, and YouTube to suggest relevant content to users.

This project builds a **content-based filtering model** that:

* Processes movie metadata
* Converts text features into vectors
* Computes similarity between movies
* Recommends the most similar movies

The model is then deployed as an interactive web app using Streamlit.

---

## How It Works

1. **Data Preprocessing**

   * Clean and combine movie metadata
   * Remove stopwords and unnecessary characters

2. **Feature Engineering**

   * Combine important columns such as:

     * genres
     * keywords
     * overview
     * cast
     * director

3. **Vectorization**

   * Convert text data into numerical vectors using **CountVectorizer**

4. **Similarity Calculation**

   * Calculate **Cosine Similarity** between movies

5. **Recommendation**

   * When a user selects a movie, the system returns the **top 10 most similar movies**

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Pickle

---

## Project Structure

```
movie-recommendation-system
│
├── app.py                       # Streamlit web application
├── movie_recommendation.ipynb   # Model building notebook
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
├── .gitignore
│
├── movies.pkl                   # Processed movie dataset
├── similarity.pkl               # Cosine similarity matrix
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Using the App

1. Select a movie from the dropdown list
2. Click **Recommend**
3. The system will display **10 similar movies**

---

## Example Output

Example recommendation:

```
Selected Movie: Avatar

Recommended Movies:
- Guardians of the Galaxy
- Star Trek
- John Carter
- Interstellar
- Gravity
```

---

## Future Improvements

* Add movie **posters using TMDB API**
* Implement **hybrid recommendation (content + collaborative filtering)**
* Improve UI with movie cards
* Add **search bar instead of dropdown**
* Deploy on **Streamlit Cloud**

---

## Dataset

The dataset is based on movie metadata from **TMDB (The Movie Database)**.

---

## Support

If you like this project, consider giving it a **star ⭐ on GitHub**.
