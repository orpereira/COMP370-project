import requests
import re
from datetime import datetime, timedelta

NEWS_API_URL = "https://newsapi.org/v2/everything"

''' writing a function to fetch all articles with a given title and studio name'''

def fetch_articles(api_key, title, studio, director, start_date, end_date, filename="articles.json"):
    """Fetch all articles with a given title and studio name """

    # query must contain movie name and either the director or studio name, do this with OR logic

    params = {
        "apiKey": api_key,
        "q": f"{title} {studio} OR {title} {director}",
        "from": start_date.isoformat(),
        "to": end_date.isoformat(),
        "language": "en",
    }

    response = requests.get(NEWS_API_URL, params=params)

    # Raise an exception if the API call fails
    if response.status_code != 200:
        raise Exception(f"Error fetching articles: {response.status_code}")
    
    # save the responses to a .json file
    with open(filename, "w") as f:
        f.write(response.text)

# make callable from the command line
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("api_key", help="Your News API key")
    parser.add_argument("title", help="The title of the movie")
    parser.add_argument("studio", help="The studio that produced the movie")
    parser.add_argument("director", help="The director of the movie")
    parser.add_argument("start_date", help="The start date for the search (YYYY-MM-DD)")
    parser.add_argument("end_date", help="The end date for the search (YYYY-MM-DD)")
    parser.add_argument("filename", help="The name of the output file", default="articles.json")
    args = parser.parse_args()

    # Parse the start and end dates
    start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    end_date = datetime.strptime(args.end_date, "%Y-%m-%d")

    fetch_articles(args.api_key, args.title, args.studio, args.director, start_date, end_date, args.filename)