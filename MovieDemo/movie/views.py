# import requests
# from django.shortcuts import render

# API_KEY = "6a4dd6af"
# BASE_URL = "http://www.omdbapi.com/"


# def home(request):
#     movie_name = request.GET.get("movie", "")

#     movies = []

#     if movie_name:
#         params = {
#             "s": movie_name,
#             "apikey": API_KEY
#         }

#         response = requests.get(BASE_URL, params=params)

#         if response.status_code == 200:
#             data = response.json()

#             if data["Response"] == "True":
#                 movies = data["Search"]

#     return render(request, "index.html", {
#         "movies": movies,
#         "movie_name": movie_name
#     })


# def movie_detail(request, imdb_id):

#     params = {
#         "i": imdb_id,
#         "apikey": API_KEY
#     }

#     response = requests.get(BASE_URL, params=params)

#     movie = None

#     if response.status_code == 200:
#         data = response.json()

#         if data["Response"] == "True":
#             movie = data

#     return render(request, "details.html", {"movie": movie})

import requests
from django.shortcuts import render

API_KEY = "6a4dd6af"
BASE_URL = "http://www.omdbapi.com/"


def movie_detail(request, imdb_id):

    params = {
        "i": imdb_id,
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    movie = {}

    if response.status_code == 200:
        movie = response.json()

        # Print everything in the terminal
        from pprint import pprint
        pprint(movie)

    return render(request, "details.html", {"movie": movie})