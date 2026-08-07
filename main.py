import requests

API_KEY = "6a4dd6af"
BASE_URL = "http://www.omdbapi.com/"

def get_movie_info(title):
    """
    Fetch movie information from OMDb by title.
    """
    params = {
        "t": title,      
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            return data
        else:
            return f"Error: {data['Error']}"
    else:
        return f"HTTP Error: {response.status_code}"

# Example usage
movie_title = "Inception"
info = get_movie_info(movie_title)

if isinstance(info, dict):
    print(f"Title: {info['Title']}")
    print(f"Year: {info['Year']}")
    print(f"IMDB Rating: {info['imdbRating']}")
    print(f"Genre: {info['Genre']}")
    print(f"Plot: {info['Plot']}")
else:
    print(info)