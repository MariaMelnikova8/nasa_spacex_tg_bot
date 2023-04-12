import random
import os
from dotenv import load_dotenv
import nasa
import SpaceX
import time
import requests


def telegram_send_message(tg_token, tg_id, picture_link, text):
    url = f'https://api.telegram.org/bot{tg_token}/sendPhoto'
    params = {
        "photo": picture_link,
    "chat_id": tg_id,
    "caption": text}
    response = requests.post(url, params=params)
    response.raise_for_status()


if __name__ == '__main__':
    load_dotenv()
    tg_id = os.getenv('tg_id')
    tg_token = os.getenv('tg_token')
    api_nasa = os.getenv('api_key')

    while True:
        nasa_heading, nasa_pics = nasa.pictures_download_nasa(api_nasa)
        spacex_launch_name, spacex_pics = SpaceX.pictures_download_spacex()
        nasa_pics.extend(spacex_pics)
        picture_link = random.choice(nasa_pics)

        if 'nasa' in picture_link:
            text = f'Картинка дня "Nasa" \nТема: {nasa_heading}'
        else:
            text = f'Картинка запуска "SpaceX" \nНомер запуска: {spacex_launch_name}'

        telegram_send_message(tg_token, tg_id, picture_link, text)

        time.sleep(3600)

