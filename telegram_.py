import requests
import time

toked = '7826311617:AAEaBrFw5g38O_xLSkeZiApJinONLi2pB6k'


def sendMessage(chat_id: str, message: str) -> dict:
    """
    :param chat_id:
    :param message:
    :return:
    ex. chat_id = '@su413_group: image_url = "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"'
    ex. message = 'message = "<strong>Name: Dara</strong>\n"'
    """
    url = f"https://api.telegram.org/bot{toked}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    r = requests.post(url, data=payload)
    return r.json()


def sendPhoto(chat_id: str, image_url: str, caption: str) -> dict:
    """
    :param chat_id:
    :param image_url:
    :param caption:
    :return:
    ex. chat_id = '@su413_group'
    ex. chat_id = '@su413_group: image_url = "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"'
    ex. caption = 'message = "<strong>Name: Dara</strong>\n"'
    """
    url = f"https://api.telegram.org/bot{toked}/sendPhoto"

    payload = {
        "chat_id": chat_id,
        "photo": image_url,
        "caption": caption,
        "parse_mode": "HTML"
    }
    r = requests.post(url, data=payload)

    return r.json()
