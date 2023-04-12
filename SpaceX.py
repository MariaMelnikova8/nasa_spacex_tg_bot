import requests


def pictures_download_spacex():
    url = 'https://api.spacexdata.com/v5/launches'
    response = requests.get(url)
    response.raise_for_status()
    list_of_dictionaries = list(reversed(response.json()))

    for launch in list_of_dictionaries:
        if launch['links']['flickr']['original']:
            list_of_links_picture = launch['links']['flickr']['original']
            break

    spacex_pics = []

    for picture_url in list_of_links_picture:
        spacex_pics.append(picture_url)

    return launch['flight_number'], spacex_pics

