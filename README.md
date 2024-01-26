# WorldScreen Dynamics

## Project Overview

WorldScreen Dynamics is a dynamic and data-driven project that captures and analyzes trending movies and series worldwide. Leveraging Python, APIs, and web scraping, it gathers real-time data from Twitter, Reddit, and IMDB. 
The project includes sentiment analysis, topic modeling, and dynamic data visualization through a Flask dashboard.

## Key Features

- **Data Acquisition:**
  - Utilized Python Requests library for Twitter and Reddit data.
  - Implemented web scraping for real-time IMDB movie and series data.

- **Large-Scale Data Collection:**
  - Gathered 1M+ tweets, 2M+ Reddit posts, and Top 100 IMDB movies/series weekly.

- **Sentiment Analysis and Topic Modeling:**
  - Employed TextBlob for analyzing sentiments.
  - Investigated discussions and abstract subjects through topic modeling.

- **Flask Dashboard:**
  - Created an interactive web application for dynamic data visualization.
  - Integrated Matplotlib for generating plots based on user-selected date ranges.

## Implementation Steps
1. Install dependencies: `pip install flask textblob pymongo`
2. Run the Flask app: `python your_app_file.py`
3. Access the dashboard in your browser: `http://localhost:8006`

## Project Findings

- Discovered positive correlation between Twitter/Reddit data and IMDB ratings.
- Established positive sentiment in public tweets and Reddit posts related to movies and series.

## Future Enhancements
- Implement user authentication for personalized dashboards.
- Explore additional data sources for more comprehensive insights.

Feel free to contribute or provide feedback!
