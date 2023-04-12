import requests


def pictures_download_nasa(api_nasa):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        "api_key": api_nasa,
        "count": 1
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    nasa_pics = []

    for elem in response.json():
        nasa_pics.append(elem['url'])
    return response.json()[0]['title'], nasa_pics
